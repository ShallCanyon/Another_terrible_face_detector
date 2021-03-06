from imutils import paths
import numpy as np
import imutils
import sqlite3 as sql
import json
import cv2
import os


if __name__ == '__main__':
    print("[INFO] loading face detectors...")
    prototxt = './face_detection_model/deploy.prototxt'
    caffemodel = './face_detection_model/res10_300x300_ssd_iter_140000.caffemodel'
    detector = cv2.dnn.readNetFromCaffe(prototxt, caffemodel)

    print("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch('./face_detection_model/openface_nn4.small2.v1.t7')

    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images('./dataset'))

    knownEmbeddings = []
    knownNames = []

    total = 0
    length = len(imagePaths)
    conf = 0.8

    for (i, imagePath) in enumerate(imagePaths):
        print("[INFO] processing image {}/{}".format(i + 1, length))
        name = imagePath.split(os.path.sep)[-2]

        # format image
        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=600)
        (h, w) = image.shape[:2]

        # dnn face reconize
        imageBlob = cv2.dnn.blobFromImage(
            cv2.resize(image, (300, 300)), 1.0, (300, 300),
            (104.0, 177.0, 123.0), swapRB=False, crop=False)
        detector.setInput(imageBlob)
        detections = detector.forward()

        # get detected faces positions
        if len(detections) > 0:
            i = np.argmax(detections[0, 0, :, 2])
            confidence = detections[0, 0, i, 2]

            if confidence > conf:
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x0, y0, x1, y1) = box.astype("int")
                face = image[y0:y1, x0:x1]

                (fH, fW) = face.shape[:2]
                if fH < 20 or fW < 20:
                    print("[INFO] face too small, skip...")
                    continue

                # dnn face characteristic gain
                faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                                                 (96, 96), (0, 0, 0),
                                                 swapRB=True, crop=False)
                embedder.setInput(faceBlob)
                vec = embedder.forward()

                knownNames.append(name)
                knownEmbeddings.append(vec.flatten())
                # print(type(vec.flatten()))
                total += 1

    print("[INFO] {} images processed...".format(total + 1))
    data = {"embeddings": knownEmbeddings, "names": knownNames}

    # put into database
    conn = sql.connect("test.db", detect_types=sql.PARSE_DECLTYPES)
    cur = conn.cursor()
    # cur.execute("DROP TABLE faces")
    # cur.execute("CREATE TABLE faces (name TEXT, embeddings BLOB)")
    ins = "INSERT INTO faces (name, embeddings) VALUES(?,?)"
    for i in range(0, total):
        cur.execute(ins, (knownNames[i], json.dumps(knownEmbeddings[i].tolist())))
        conn.commit()  # important
        print("Executed NO.{}".format(i + 1))
    cur.close()
    conn.close()


