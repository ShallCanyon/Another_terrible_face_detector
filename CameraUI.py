# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CameraUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(631, 509)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.videoFrame = QtWidgets.QLabel(self.gridLayoutWidget)
        self.videoFrame.setMinimumSize(QtCore.QSize(320, 240))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.videoFrame.setFont(font)
        self.videoFrame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.videoFrame.setAutoFillBackground(False)
        self.videoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.videoFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.videoFrame.setWordWrap(True)
        self.videoFrame.setObjectName("videoFrame")
        self.gridLayout.addWidget(self.videoFrame, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_rec = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_rec.setFont(font)
        self.btn_rec.setObjectName("btn_rec")
        self.horizontalLayout.addWidget(self.btn_rec)
        self.btn_pth = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_pth.setFont(font)
        self.btn_pth.setObjectName("btn_pth")
        self.horizontalLayout.addWidget(self.btn_pth)
        self.btn_sav = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_sav.setFont(font)
        self.btn_sav.setObjectName("btn_sav")
        self.horizontalLayout.addWidget(self.btn_sav)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_pathDisp = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_pathDisp.setFont(font)
        self.label_pathDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pathDisp.setWordWrap(True)
        self.label_pathDisp.setObjectName("label_pathDisp")
        self.verticalLayout.addWidget(self.label_pathDisp)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 26))
        self.menubar.setObjectName("menubar")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Port1 = QtWidgets.QAction(MainWindow)
        self.Port1.setObjectName("Port1")
        self.Port0 = QtWidgets.QAction(MainWindow)
        self.Port0.setObjectName("Port0")
        self.Port2 = QtWidgets.QAction(MainWindow)
        self.Port2.setObjectName("Port2")
        self.actionChange_Confidence = QtWidgets.QAction(MainWindow)
        self.actionChange_Confidence.setObjectName("actionChange_Confidence")
        self.actionChange_Port = QtWidgets.QAction(MainWindow)
        self.actionChange_Port.setObjectName("actionChange_Port")
        self.menuOption.addAction(self.actionChange_Confidence)
        self.menuOption.addAction(self.actionChange_Port)
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CameraFaceDetecter"))
        self.videoFrame.setText(_translate("MainWindow", "Camera not activated"))
        self.btn_rec.setText(_translate("MainWindow", "Record"))
        self.btn_pth.setText(_translate("MainWindow", "SavingPath"))
        self.btn_sav.setText(_translate("MainWindow", "Capture"))
        self.label_pathDisp.setText(_translate("MainWindow", "Current path:"))
        self.menuOption.setTitle(_translate("MainWindow", "option"))
        self.menuAbout.setTitle(_translate("MainWindow", "about"))
        self.Port1.setText(_translate("MainWindow", "1"))
        self.Port0.setText(_translate("MainWindow", "0"))
        self.Port2.setText(_translate("MainWindow", "2"))
        self.actionChange_Confidence.setText(_translate("MainWindow", "Change Confidence"))
        self.actionChange_Port.setText(_translate("MainWindow", "Change Port"))
