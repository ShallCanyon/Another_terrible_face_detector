import camera_detect
import startupDialog
import sys
from PyQt5.QtWidgets import QApplication, QDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # win = camera_detect.win()
    win = startupDialog.win()
    win.show()
    sys.exit(app.exec_())
