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
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.JoinMeLabel = QtWidgets.QLabel(self.centralWidget)
        self.JoinMeLabel.setGeometry(QtCore.QRect(170, 180, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(40)
        self.JoinMeLabel.setFont(font)
        self.JoinMeLabel.setStyleSheet("border-image: \\*url();")
        self.JoinMeLabel.setObjectName("JoinMeLabel")
        self.SignInButton = QtWidgets.QPushButton(self.centralWidget)
        self.SignInButton.setGeometry(QtCore.QRect(383, 177, 191, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
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
        self.graphicsView.setGeometry(QtCore.QRect(330, 185, 41, 31))
        self.graphicsView.setStyleSheet("border-image: url(./POP_Gmail.png)")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralWidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 745, 453))
        self.graphicsView_2.setStyleSheet("border-image: url(./bg.png)\n"
"\n"
"")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.JoinMeLabel_2 = QtWidgets.QLabel(self.centralWidget)
        self.JoinMeLabel_2.setGeometry(QtCore.QRect(310, 420, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(10)
        self.JoinMeLabel_2.setFont(font)
        self.JoinMeLabel_2.setStyleSheet("border-image: \\*url();")
        self.JoinMeLabel_2.setObjectName("JoinMeLabel_2")
        self.graphicsView_2.raise_()
        self.JoinMeLabel.raise_()
        self.SignInButton.raise_()
        self.QuitButton.raise_()
        self.graphicsView.raise_()
        self.JoinMeLabel_2.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.JoinMeLabel.setText(_translate("MainWindow", "JoinMe"))
        self.SignInButton.setText(_translate("MainWindow", "Sign in with Google"))
        self.QuitButton.setText(_translate("MainWindow", "Quit"))
        self.JoinMeLabel_2.setText(_translate("MainWindow", "@ Columbia University"))

