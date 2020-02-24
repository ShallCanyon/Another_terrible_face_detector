from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QImage
import FaceFunctions
import PictureUI
import cv2


class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = PictureUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_sel.clicked.connect(self.selectPicture)
        self.ui.btn_detect.clicked.connect(self.detectFaces)

    def selectPicture(self):
        file = QFileDialog()
        self.filename, filetype = file.getOpenFileName(self, "Select a picture", "",
                                                       "image Files (*.jpg;*.jpeg;*.bmp;*.png;);;"
                                                       "All Files (*)")
        self.pic = QPixmap(self.filename)
        self.ui.label_pic.setScaledContents(True)
        self.ui.label_pic.setPixmap(self.pic)
        self.ui.btn_detect.setEnabled(True)

    def detectFaces(self):
        frame = cv2.imread(self.filename)
        height, width = frame.shape[:2]
        fun = FaceFunctions.Faces()
        img, detections = fun.faceDetect(frame, fun.confidence, fun.idenRecog)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = QImage(img, width, height, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)
        self.ui.label_pic.setPixmap(img)
