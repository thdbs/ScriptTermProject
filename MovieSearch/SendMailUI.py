# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_mail.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sendMail

currentDetailData = None

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        self.dialog = Dialog

        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 155)
        self.myMailAddr = QtWidgets.QLineEdit(Dialog)
        self.myMailAddr.setGeometry(QtCore.QRect(100, 20, 251, 20))
        self.myMailAddr.setObjectName("myMailAddr")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label_2.setObjectName("label_2")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(100, 50, 251, 20))
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.targetMailAddr = QtWidgets.QLineEdit(Dialog)
        self.targetMailAddr.setGeometry(QtCore.QRect(100, 80, 251, 20))
        self.targetMailAddr.setObjectName("targetMailAddr")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(14, 110, 341, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked['bool'].connect(self.PushSendMailBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "메일 보내기"))
        self.label.setText(_translate("Dialog", "내 이메일"))
        self.label_2.setText(_translate("Dialog", "비밀번호"))
        self.label_3.setText(_translate("Dialog", "받는 주소"))
        self.pushButton.setText(_translate("Dialog", "메일 보내기"))

    def PushSendMailBtn(self):
        global currentDetailData
        if len(self.myMailAddr.text()) > 0 and len(self.password.text()) > 0 and len(self.targetMailAddr.text()) > 0:
            if currentDetailData != None:
                sendMail.sendMail(currentDetailData, self.myMailAddr.text(), self.password.text(), self.targetMailAddr.text())
                self.dialog.destroy()
        pass
