# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startup.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(626, 308)
        Dialog.setSizeGripEnabled(False)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.icon_pic = QtWidgets.QLabel(Dialog)
        self.icon_pic.setObjectName("icon_pic")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.icon_pic)
        self.btn_pic = QtWidgets.QPushButton(Dialog)
        self.btn_pic.setObjectName("btn_pic")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_pic)
        self.icon_cam = QtWidgets.QLabel(Dialog)
        self.icon_cam.setObjectName("icon_cam")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.icon_cam)
        self.btn_cam = QtWidgets.QPushButton(Dialog)
        self.btn_cam.setObjectName("btn_cam")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.btn_cam)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Start"))
        self.icon_pic.setText(_translate("Dialog", "icon1"))
        self.btn_pic.setText(_translate("Dialog", "Picture"))
        self.icon_cam.setText(_translate("Dialog", "icon2"))
        self.btn_cam.setText(_translate("Dialog", "Camera"))
