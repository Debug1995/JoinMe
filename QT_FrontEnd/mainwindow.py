# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 453)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("border-image: url(:/bg.png)")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SignUpButton = QtWidgets.QPushButton(self.centralWidget)
        self.SignUpButton.setGeometry(QtCore.QRect(430, 245, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("border-image: \\*url();")
        self.SignUpButton.setObjectName("SignUpButton")
        self.NoAccount = QtWidgets.QLabel(self.centralWidget)
        self.NoAccount.setGeometry(QtCore.QRect(330, 250, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NoAccount.setFont(font)
        self.NoAccount.setStyleSheet("border-image: \\*url();")
        self.NoAccount.setTextFormat(QtCore.Qt.AutoText)
        self.NoAccount.setObjectName("NoAccount")
        self.JoinMeLabel = QtWidgets.QLabel(self.centralWidget)
        self.JoinMeLabel.setGeometry(QtCore.QRect(160, 180, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(40)
        self.JoinMeLabel.setFont(font)
        self.JoinMeLabel.setStyleSheet("border-image: \\*url();")
        self.JoinMeLabel.setObjectName("JoinMeLabel")
        self.UserNameInput = QtWidgets.QLineEdit(self.centralWidget)
        self.UserNameInput.setGeometry(QtCore.QRect(420, 150, 113, 21))
        self.UserNameInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.UserNameInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px\n"
"")
        self.UserNameInput.setText("")
        self.UserNameInput.setClearButtonEnabled(False)
        self.UserNameInput.setObjectName("UserNameInput")
        self.UserName = QtWidgets.QLabel(self.centralWidget)
        self.UserName.setGeometry(QtCore.QRect(330, 150, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("border-image: \\*url();")
        self.UserName.setObjectName("UserName")
        self.PasswordInput = QtWidgets.QLineEdit(self.centralWidget)
        self.PasswordInput.setGeometry(QtCore.QRect(420, 180, 113, 21))
        self.PasswordInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PasswordInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.PasswordInput.setText("")
        self.PasswordInput.setClearButtonEnabled(False)
        self.PasswordInput.setObjectName("PasswordInput")
        self.Password = QtWidgets.QLabel(self.centralWidget)
        self.Password.setGeometry(QtCore.QRect(330, 180, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Password.setFont(font)
        self.Password.setStyleSheet("border-image: \\*url();")
        self.Password.setObjectName("Password")
        self.SignInButton = QtWidgets.QPushButton(self.centralWidget)
        self.SignInButton.setGeometry(QtCore.QRect(320, 210, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SignInButton.setFont(font)
        self.SignInButton.setStyleSheet("border-image: \\*url();")
        self.SignInButton.setObjectName("SignInButton")
        self.QuitButton = QtWidgets.QPushButton(self.centralWidget)
        self.QuitButton.setGeometry(QtCore.QRect(430, 210, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QuitButton.setFont(font)
        self.QuitButton.setStyleSheet("border-image: \\*url();")
        self.QuitButton.setObjectName("QuitButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.NoAccount.setText(_translate("MainWindow", "No Account?"))
        self.JoinMeLabel.setText(_translate("MainWindow", "JoinMe"))
        self.UserName.setText(_translate("MainWindow", "User Name"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.SignInButton.setText(_translate("MainWindow", "Sign In"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))

