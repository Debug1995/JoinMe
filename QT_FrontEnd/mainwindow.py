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
        MainWindow.setStyleSheet("border-image: url(./bg.png)")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.SignUpButton = QtWidgets.QPushButton(self.centralWidget)
        self.SignUpButton.setGeometry(QtCore.QRect(420, 209, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("border-image: \\*url();")
        self.SignUpButton.setObjectName("SignUpButton")
        self.NoAccount = QtWidgets.QLabel(self.centralWidget)
        self.NoAccount.setGeometry(QtCore.QRect(320, 214, 101, 20))
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
        self.SignInButton = QtWidgets.QPushButton(self.centralWidget)
        self.SignInButton.setGeometry(QtCore.QRect(340, 174, 191, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SignInButton.setFont(font)
        self.SignInButton.setStyleSheet("border-image: \\*url();")
        self.SignInButton.setObjectName("SignInButton")
        self.QuitButton = QtWidgets.QPushButton(self.centralWidget)
        self.QuitButton.setGeometry(QtCore.QRect(0, 0, 111, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.QuitButton.setFont(font)
        self.QuitButton.setStyleSheet("border-image: \\*url();")
        self.QuitButton.setObjectName("QuitButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 180, 21, 18))
        self.graphicsView.setStyleSheet("border-image: url(:/POP_Gmail.png)")
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.NoAccount.setText(_translate("MainWindow", "No Account?"))
        self.JoinMeLabel.setText(_translate("MainWindow", "JoinMe"))
        self.SignInButton.setText(_translate("MainWindow", "Sign in with google"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))

