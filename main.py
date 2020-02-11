import Unused_MainUI
import mainFunction
import sys
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # win = MainUI.win()
    win = mainFunction.win()
    win.show()
    sys.exit(app.exec_())
