import cv2
import time
import pickle
import numpy as np
from configparser import ConfigParser
from PyQt5.QtGui import QPixmap, QImage


class Video:
    # capture传入cv2.VideoCapture()
    def __init__(self, capture):
        cfg = ConfigParser()
        cfg.read('./scripts/config.ini')
        # cfg.sections()
        '''caffeModel = './scripts/detectModel/res10_300x300_ssd_iter_140000.caffemodel'
        prototxt = './scripts/detectModel/deploy.prototxt'
        embeddings = './scripts/detectModel/openface_nn4.small2.v1.t7'
        recog_path = './scripts/recognizeModel/recognizer_sc.pickle'
        le_path = './scripts/recognizeModel/le_sc.pickle' '''

        caffeModel = cfg.get('scripts', 'caffeModel')
        prototxt = cfg.get('scripts', 'prototxt')
        embeddings = cfg.get('scripts', 'embeddings')
        recog_path = cfg.get('scripts', 'recognizer')
        le_path = cfg.get('scripts', 'labelEncoder')

        # initialize dnn modules
        self.net = cv2.dnn.readNetFromCaffe(prototxt, caffeModel)
        self.embedder = cv2.dnn.readNetFromTorch(embeddings)
        self.recognizer = pickle.loads(open(recog_path, "rb").read())
        self.le = pickle.loads(open(le_path, "rb").read())

        self.capture = capture
        self.minimalHeight = cfg.getint('faceRecognition', 'minimalHeight')
        self.minimalWidth = cfg.getint('faceRecognition', 'minimalWidth')
        self.suffix = cfg.get('default', 'picSuffix')
        self.currentFrame = np.array([])
        self.count = 1

    def captureFrame(self):
        ret, readFrame = self.capture.read()
        if ret:
            self.currentFrame = cv2.cvtColor(readFrame, cv2.COLOR_BGR2RGB)
            # self.currentFrame = readFrame
            self.height, self.width = self.currentFrame.shape[:2]

    # TODO: function is not done well
    def captureStop(self):
        self.capture.release()

    # 将摄像头视频帧进行人脸识别并返回识别帧
    def getDetectedFrame(self, confidence, idenRecog=False):
        # 复制视频帧：copiedImg 进行矩形渲染并显示到UI上，而不对源视频帧做任何改动
        # 直接用 = 是引用而非复制，需要使用copy函数
        self.copiedImg = self.currentFrame.copy()
        markedImg, self.detectedFaces = self.faceDetect(self.copiedImg, confidence, idenRecog)
        return markedImg

    # 转换为QPixmap
    def toPixmap(self, markedImg):
        img = QImage(markedImg, self.width, self.height, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)
        return img

    '''
    侦测人脸并框中
    @:param
    img: one frame that may contain at least one face
    confidence: confidence of face detection
    idenRecog: turn on or off identity recognition
    '''
    def faceDetect(self, image, confidence=0.5, idenRecog=False):
        # deep neutral network face detect
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
                        [self.width, self.height, self.width, self.height])
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
                                  (0, 255, 0), 1)
                    cv2.putText(image, text, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        return image, detections

    # frame为当前视频帧，path为选取的路径，suffix为图片文件的后缀，xywh为人脸区域的矩形数据
    def faceStorage(self, frame, x, y, w, h, path):  # 保存人脸
        listStr = [str(int(time.time())), "_", str(self.count)]
        nameStr = ''.join(listStr)
        filename = path + nameStr + self.suffix

        face = cv2.resize(frame[y:(y + h), x:(x + w)], (300, 300))
        # cv2.imwrite()不能选择中文路径
        # write = cv2.imwrite(filename, face)
        try:
            cv2.imencode(self.suffix, face)[1].tofile(filename)
            print("[INFO] Face captured named %s." % filename)
            self.count += 1
        except IOError:
            print("[ERROR]Saved unsuccessfully at %s" % path)
