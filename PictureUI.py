# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PictureUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 600, 568, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_sel = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_sel.setObjectName("btn_sel")
        self.horizontalLayout.addWidget(self.btn_sel)
        self.btn_detect = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_detect.setEnabled(False)
        self.btn_detect.setObjectName("btn_detect")
        self.horizontalLayout.addWidget(self.btn_detect)
        self.label_pic = QtWidgets.QLabel(self.centralwidget)
        self.label_pic.setGeometry(QtCore.QRect(30, 30, 851, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic.sizePolicy().hasHeightForWidth())
        self.label_pic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_pic.setFont(font)
        self.label_pic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_pic.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_pic.setLineWidth(1)
        self.label_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic.setObjectName("label_pic")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuSave = QtWidgets.QMenu(self.menuOption)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSelect_db = QtWidgets.QAction(MainWindow)
        self.actionSelect_db.setObjectName("actionSelect_db")
        self.actionSave_detected_picture = QtWidgets.QAction(MainWindow)
        self.actionSave_detected_picture.setObjectName("actionSave_detected_picture")
        self.actionSave_detected_face = QtWidgets.QAction(MainWindow)
        self.actionSave_detected_face.setObjectName("actionSave_detected_face")
        self.actionDetected_picture = QtWidgets.QAction(MainWindow)
        self.actionDetected_picture.setObjectName("actionDetected_picture")
        self.actionDetected_faces = QtWidgets.QAction(MainWindow)
        self.actionDetected_faces.setObjectName("actionDetected_faces")
        self.actionDetected_faces_data = QtWidgets.QAction(MainWindow)
        self.actionDetected_faces_data.setObjectName("actionDetected_faces_data")
        self.menuSave.addAction(self.actionDetected_picture)
        self.menuSave.addAction(self.actionDetected_faces)
        self.menuSave.addAction(self.actionDetected_faces_data)
        self.menuOption.addAction(self.actionSelect_db)
        self.menuOption.addAction(self.menuSave.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Picture Face Detector"))
        self.btn_sel.setText(_translate("MainWindow", "Select"))
        self.btn_detect.setText(_translate("MainWindow", "Detect"))
        self.label_pic.setText(_translate("MainWindow", "Select a picture with face"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.menuSave.setTitle(_translate("MainWindow", "save"))
        self.actionSelect_db.setText(_translate("MainWindow", "select db"))
        self.actionSave_detected_picture.setText(_translate("MainWindow", "save detected picture"))
        self.actionSave_detected_face.setText(_translate("MainWindow", "save detected face"))
        self.actionDetected_picture.setText(_translate("MainWindow", "picture"))
        self.actionDetected_faces.setText(_translate("MainWindow", "faces"))
        self.actionDetected_faces_data.setText(_translate("MainWindow", "faces data"))
