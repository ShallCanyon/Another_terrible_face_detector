from PyQt5.QtWidgets import QMainWindow, QFileDialog

import PictureUI


class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = PictureUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_sel.clicked.connect(self.selectPicture)

    def selectPicture(self):
        file = QFileDialog()
        filename, filetype = file.getOpenFileName(self, "Select a picture", "./",
                                                  "All Files (*);;"
                                                  "image Files (*.jpg;*.jpeg;*.bmp;*.png;)")
        if filetype == "jpg" or filetype == "jpeg" or filetype == "bmp" or filetype == "png":
            self.ui.label_pic.setPixmap(filename)