import cv2
import time
import pickle
import FaceFunctions
import numpy as np
from configparser import ConfigParser
from PyQt5.QtGui import QPixmap, QImage


class Video(FaceFunctions.Faces):
    # capture传入cv2.VideoCapture()
    def __init__(self, capture):
        super(Video, self).__init__()
        # FaceFunctions.Faces.__init__(self)

        self.suffix = self.cfg.get('default', 'picSuffix')
        self.capture = capture
        self.currentFrame = np.array([])
        self.count = 1

    def captureFrame(self):
        ret, readFrame = self.capture.read()
        if ret:
            self.currentFrame = cv2.cvtColor(readFrame, cv2.COLOR_BGR2RGB)
            self.height, self.width = self.currentFrame.shape[:2]

    # TODO: function is not working well
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
    def toPixmap(self, img):
        img = QImage(img, self.width, self.height, QImage.Format_RGB888)
        return QPixmap.fromImage(img)

    # frame为当前视频帧，path为选取的路径，suffix为图片文件的后缀，xywh为人脸区域的矩形数据
    def faceSave(self, frame, x, y, w, h, path):  # 保存人脸
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
