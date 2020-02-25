# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_main(object):
    def setupUi(self, Form_main):
        Form_main.setObjectName("Form_main")
        Form_main.resize(419, 561)
        Form_main.setMinimumSize(QtCore.QSize(419, 460))
        Form_main.setMaximumSize(QtCore.QSize(1000, 1000))
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form_main)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 401, 441))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(401, 441))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(1000, 1000))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel(Form_main)
        self.label.setGeometry(QtCore.QRect(20, 470, 111, 16))
        self.label.setObjectName("label")
        self.lineEdit_message = QtWidgets.QLineEdit(Form_main)
        self.lineEdit_message.setGeometry(QtCore.QRect(20, 490, 391, 20))
        self.lineEdit_message.setObjectName("lineEdit_message")
        self.pushButton_enter = QtWidgets.QPushButton(Form_main)
        self.pushButton_enter.setGeometry(QtCore.QRect(20, 520, 75, 23))
        self.pushButton_enter.setObjectName("pushButton_enter")

        self.retranslateUi(Form_main)
        QtCore.QMetaObject.connectSlotsByName(Form_main)

    def retranslateUi(self, Form_main):
        _translate = QtCore.QCoreApplication.translate
        Form_main.setWindowTitle(_translate("Form_main", "Общение"))
        self.label.setText(_translate("Form_main", "Введите сообщение"))
        self.pushButton_enter.setText(_translate("Form_main", "Отправить"))
