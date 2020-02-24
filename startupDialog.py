from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
import startup
import camera_detect
import picture_detect


class win(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = startup.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_pic.clicked.connect(self.openPictureDetect)
        self.ui.btn_cam.clicked.connect(self.openCameraDetect)

    def openCameraDetect(self):
        self.close()
        self.camera_ui = camera_detect.win()
        self.camera_ui.show()

    def openPictureDetect(self):
        self.close()
        self.picture_ui = picture_detect.win()
        self.picture_ui.show()
