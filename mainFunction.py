import cv2
import numpy as np
import CameraUI
from VideoFaceDetect import Video
from configparser import ConfigParser
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QFileDialog, QInputDialog
from imutils.video import VideoStream


class win(QMainWindow):
    def __init__(self):
        super().__init__()
        # 加载UI文件
        self.ui = CameraUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.cfg = ConfigParser()
        self.cfg.read('./scripts/config.ini')
        self.savingPath = './Captured_faces/'
        self.cameraPort = self.cfg.getint('camera', 'port')
        self.confidence = self.cfg.getfloat('faceRecognition', 'confidence')
        self.idenRecog = self.cfg.getboolean('faceRecognition', 'identityRecognition')
        self.cameraIsOpen = False

        self.ui.btn_rec.clicked.connect(lambda: self.startRecord(self.ui.btn_rec))
        self.ui.btn_pth.clicked.connect(self.selectSavingPath)
        self.ui.btn_sav.clicked.connect(self.captureFaces)
        self.ui.label_pathDisp.setText('Current path: ' + self.savingPath)
        self.ui.actionChange_Confidence.triggered.connect(self.changeConfidence)
        self.ui.actionChange_Port.triggered.connect(self.changeCameraPort)

    # 获取摄像头视频
    def startRecord(self, button):
        if button.sender().text() == 'Record':
            self.video = Video(cv2.VideoCapture(self.cameraPort + cv2.CAP_DSHOW))
            self.cameraIsOpen = True
            # 无限循环计时器
            _timer = QTimer(self)
            # 链接QLabel
            _timer.timeout.connect(self.play)
            _timer.start(27)  # 影响帧数
            button.setText('Stop')
        elif button.sender().text() == 'Stop':
            # TODO: be able to stop the camera
            self.video.captureStop()
            # self.ui.videoFrame.clear()
            # self.videoFrame.setText('No Frame')
            button.setText('Record')
            self.cameraIsOpen = False

    # 将视频帧显示在label中
    def play(self):
        try:
            # 获取视频帧
            self.video.captureFrame()
            # 在getFrameData中转换格式并识别人脸
            self.ui.videoFrame.setPixmap(
                self.video.toPixmap(
                    self.video.getDetectedFrame(self.confidence, self.idenRecog)))
            self.ui.videoFrame.setScaledContents(True)
        except TypeError:
            print("[INFO] No Frame")

    def captureFaces(self):  # 按键后截取屏幕人脸
        if self.cameraIsOpen and len(self.video.detectedFaces) > 0:
            w = self.video.width
            h = self.video.height
            detections = self.video.detectedFaces
            self.video.count = 1

            # detections为人脸识别得到的各种信息
            # 利用信息内的人脸坐标对源视频帧进行截取
            # 若在getFrameData()中不copy视频帧，则截取的人脸边框会有矩形
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                if confidence > self.confidence:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    # (startX, startY, endX, endY) = box.astype("int")
                    (_startX, _startY, _endX, _endY) = box.astype("int")
                    centralX = int((_endX - _startX) / 2)
                    centralY = int((_endY - _startY) / 2)

                    startX = _startX - centralX if _startX - centralX >= 0 else _startX
                    startY = _startY - centralY if _startY - centralY >= 0 else _startY
                    endX = _endX + centralX  # if _endX-centralX >= 0 else _endX
                    endY = _endY + centralY  # if _endY-centralY >= 0 else _endY
                    # 没有这一步转换会导致截取的图片发蓝
                    img = cv2.cvtColor(self.video.currentFrame, cv2.COLOR_BGR2RGB)
                    self.video.faceStorage(img, startX, startY,
                                           endX - startX, endY - startY,
                                           self.savingPath)
        else:
            print("[INFO] Capture failed")

    def selectSavingPath(self):  # 选择截取人脸图的保存路径
        fName = QFileDialog()
        path = fName.getExistingDirectory(self, 'Select a Folder to save images', self.savingPath)
        fName.destroy()
        self.savingPath = path + '/'
        self.ui.label_pathDisp.setText('Current path: ' + self.savingPath)
        # print(self.path)

    def changeCameraPort(self):
        port, input = QInputDialog().getInt(self, "Input certain camera port", "Port: ", self.cameraPort)
        if input:
            self.cfg.set('camera', 'port', str(port))
            with open('./scripts/config.ini', 'w') as f:
                self.cfg.write(f)
            self.cameraPort = port

    def changeConfidence(self):
        confidence, input = QInputDialog().getDouble(self, "Input certain confidence",
                                                     "confidence: ", self.confidence * 100)
        if input:
            self.cfg.set('faceRecognition', 'confidence', str(self.confidence))
            with open('./scripts/config.ini', 'w') as f:
                self.cfg.write(f)
            self.confidence = confidence / 100
