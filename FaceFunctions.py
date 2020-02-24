import cv2
import pickle
import numpy as np
from configparser import ConfigParser
from PyQt5.QtGui import QPixmap, QImage

class Faces(object):
    def __init__(self):
        self.cfg = ConfigParser()
        self.cfg.read('./scripts/config.ini')
        caffeModel = self.cfg.get('scripts', 'caffeModel')
        prototxt = self.cfg.get('scripts', 'prototxt')
        embeddings = self.cfg.get('scripts', 'embeddings')
        recog_path = self.cfg.get('scripts', 'recognizer')
        le_path = self.cfg.get('scripts', 'labelEncoder')

        # initialize dnn modules
        self.net = cv2.dnn.readNetFromCaffe(prototxt, caffeModel)
        self.embedder = cv2.dnn.readNetFromTorch(embeddings)
        self.recognizer = pickle.loads(open(recog_path, "rb").read())
        self.le = pickle.loads(open(le_path, "rb").read())
        self.cameraPort = self.cfg.getint('camera', 'port')
        self.confidence = self.cfg.getfloat('faceRecognition', 'confidence')
        self.idenRecog = self.cfg.getboolean('faceRecognition', 'identityRecognition')
        self.minimalHeight = self.cfg.getint('faceRecognition', 'minimalHeight')
        self.minimalWidth = self.cfg.getint('faceRecognition', 'minimalWidth')
        self.lineWidth = self.cfg.getint('faceRecognition', 'rectangleLineWidth')
        self.textScale = self.cfg.getfloat('faceRecognition', 'textFontScale')

    '''
    侦测人脸并框中
    @:param
    img: one frame that may contain at least one face
    confidence: confidence of face detection
    idenRecog: turn on or off identity recognition
    '''
    def faceDetect(self, image, confidence=0.5, idenRecog=False):
        # deep neutral network face detect
        height, width = image.shape[:2]
        blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
                                     [104, 117, 123], False, False)
        self.net.setInput(blob)
        detections = self.net.forward()

        if len(detections) > 0:
            # execute every detected face
            for i in range(0, detections.shape[2]):
                conf = detections[0, 0, i, 2]
                if conf > confidence:
                    box = detections[0, 0, i, 3:7] * np.array(
                        [width, height, width, height])
                    (startX, startY, endX, endY) = box.astype("int")

                    face = image[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]
                    if fH < self.minimalHeight or fW < self.minimalWidth:
                        continue

                    # identity recognition
                    if idenRecog:
                        faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                         (96, 96), (0, 0, 0),
                                                         swapRB=True, crop=False)
                        self.embedder.setInput(faceBlob)
                        vec = self.embedder.forward()

                        preds = self.recognizer.predict_proba(vec)[0]
                        fit = np.argmax(preds)
                        match = preds[fit]
                        name = self.le.classes_[fit]

                    # set text onto frame
                    if idenRecog:
                        text = "{}: {:.2f}%".format(name, match * 100)
                    else:
                        text = "{:.2f}%".format(conf * 100)
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(image, (startX, startY), (endX, endY),
                                  (0, 255, 0), self.lineWidth)
                    cv2.putText(image, text, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, self.textScale,
                                (0, 0, 255), 2)
        return image, detections
