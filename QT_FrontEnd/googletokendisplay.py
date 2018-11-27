# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'googletokendisplay.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GoogleTokenDisplay(object):
    def setupUi(self, GoogleTokenDisplay):
        GoogleTokenDisplay.setObjectName("GoogleTokenDisplay")
        GoogleTokenDisplay.resize(745, 453)
        self.LoginButton = QtWidgets.QPushButton(GoogleTokenDisplay)
        self.LoginButton.setGeometry(QtCore.QRect(600, 201, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("border-image: \\*url();")
        self.LoginButton.setObjectName("LoginButton")
        self.graphicsView = QtWidgets.QGraphicsView(GoogleTokenDisplay)
        self.graphicsView.setGeometry(QtCore.QRect(160, 199, 41, 31))
        self.graphicsView.setStyleSheet("border-image: url(./POP_Gmail.png)")
        self.graphicsView.setObjectName("graphicsView")
        self.JoinMeLabel_2 = QtWidgets.QLabel(GoogleTokenDisplay)
        self.JoinMeLabel_2.setGeometry(QtCore.QRect(311, 420, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(10)
        self.JoinMeLabel_2.setFont(font)
        self.JoinMeLabel_2.setStyleSheet("border-image: \\*url();")
        self.JoinMeLabel_2.setObjectName("JoinMeLabel_2")
        self.JoinMeLabel = QtWidgets.QLabel(GoogleTokenDisplay)
        self.JoinMeLabel.setGeometry(QtCore.QRect(10, 190, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(40)
        self.JoinMeLabel.setFont(font)
        self.JoinMeLabel.setStyleSheet("border-image: \\*url();")
        self.JoinMeLabel.setObjectName("JoinMeLabel")
        self.graphicsView_2 = QtWidgets.QGraphicsView(GoogleTokenDisplay)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 745, 453))
        self.graphicsView_2.setStyleSheet("border-image: url(./bg.png)\n"
"\n"
"")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.TokenInput = QtWidgets.QLineEdit(GoogleTokenDisplay)
        self.TokenInput.setGeometry(QtCore.QRect(220, 200, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TokenInput.setFont(font)
        self.TokenInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.TokenInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.TokenInput.setText("")
        self.TokenInput.setClearButtonEnabled(False)
        self.TokenInput.setObjectName("TokenInput")
        self.BackButton = QtWidgets.QPushButton(GoogleTokenDisplay)
        self.BackButton.setGeometry(QtCore.QRect(0, 0, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackButton.setFont(font)
        self.BackButton.setStyleSheet("border-image: \\*url();")
        self.BackButton.setObjectName("BackButton")
        self.graphicsView_2.raise_()
        self.LoginButton.raise_()
        self.graphicsView.raise_()
        self.JoinMeLabel_2.raise_()
        self.JoinMeLabel.raise_()
        self.TokenInput.raise_()
        self.BackButton.raise_()

        self.retranslateUi(GoogleTokenDisplay)
        QtCore.QMetaObject.connectSlotsByName(GoogleTokenDisplay)

    def retranslateUi(self, GoogleTokenDisplay):
        _translate = QtCore.QCoreApplication.translate
        GoogleTokenDisplay.setWindowTitle(_translate("GoogleTokenDisplay", "Dialog"))
        self.LoginButton.setText(_translate("GoogleTokenDisplay", "Login in"))
        self.JoinMeLabel_2.setText(_translate("GoogleTokenDisplay", "@ Columbia University"))
        self.JoinMeLabel.setText(_translate("GoogleTokenDisplay", "JoinMe"))
        self.TokenInput.setPlaceholderText(_translate("GoogleTokenDisplay", "Please input your Google token!"))
        self.BackButton.setText(_translate("GoogleTokenDisplay", "Back"))

