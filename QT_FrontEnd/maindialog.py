# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(745, 453)
        MainDialog.setStyleSheet("border-image: url(./bg.png)")
        self.UserImage = QtWidgets.QGraphicsView(MainDialog)
        self.UserImage.setGeometry(QtCore.QRect(650, 10, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UserImage.setFont(font)
        self.UserImage.setStyleSheet("border-radius: 30px;\n"
"")
        self.UserImage.setObjectName("UserImage")
        self.line = QtWidgets.QFrame(MainDialog)
        self.line.setGeometry(QtCore.QRect(610, 0, 2, 453))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line.setFont(font)
        self.line.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(19, 35, 255);\n"
"")
        self.line.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.NickName = QtWidgets.QLabel(MainDialog)
        self.NickName.setGeometry(QtCore.QRect(645, 76, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NickName.setFont(font)
        self.NickName.setStyleSheet("border-image: \\*url();")
        self.NickName.setObjectName("NickName")
        self.UpdateProfileButton = QtWidgets.QPushButton(MainDialog)
        self.UpdateProfileButton.setGeometry(QtCore.QRect(640, 100, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UpdateProfileButton.setFont(font)
        self.UpdateProfileButton.setStyleSheet("border-image: \\*url();")
        self.UpdateProfileButton.setObjectName("UpdateProfileButton")
        self.line_2 = QtWidgets.QFrame(MainDialog)
        self.line_2.setGeometry(QtCore.QRect(610, 151, 140, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(19, 35, 255);\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(MainDialog)
        self.label_5.setGeometry(QtCore.QRect(623, 154, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-image: \\*url();")
        self.label_5.setObjectName("label_5")
        self.AttendEvent1 = QtWidgets.QLabel(MainDialog)
        self.AttendEvent1.setGeometry(QtCore.QRect(643, 180, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AttendEvent1.setFont(font)
        self.AttendEvent1.setStyleSheet("border-image: \\*url();")
        self.AttendEvent1.setObjectName("AttendEvent1")
        self.AttendEvent2 = QtWidgets.QLabel(MainDialog)
        self.AttendEvent2.setGeometry(QtCore.QRect(643, 208, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AttendEvent2.setFont(font)
        self.AttendEvent2.setStyleSheet("border-image: \\*url();")
        self.AttendEvent2.setObjectName("AttendEvent2")
        self.AttendEvent3 = QtWidgets.QLabel(MainDialog)
        self.AttendEvent3.setGeometry(QtCore.QRect(643, 238, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AttendEvent3.setFont(font)
        self.AttendEvent3.setStyleSheet("border-image: \\*url();")
        self.AttendEvent3.setObjectName("AttendEvent3")
        self.HostAttendSeeMoreButton = QtWidgets.QPushButton(MainDialog)
        self.HostAttendSeeMoreButton.setGeometry(QtCore.QRect(635, 263, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostAttendSeeMoreButton.setFont(font)
        self.HostAttendSeeMoreButton.setStyleSheet("border-image: \\*url();")
        self.HostAttendSeeMoreButton.setObjectName("HostAttendSeeMoreButton")
        self.line_3 = QtWidgets.QFrame(MainDialog)
        self.line_3.setGeometry(QtCore.QRect(610, 301, 140, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(19, 35, 255);\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.HostEvent2 = QtWidgets.QLabel(MainDialog)
        self.HostEvent2.setGeometry(QtCore.QRect(643, 365, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEvent2.setFont(font)
        self.HostEvent2.setStyleSheet("border-image: \\*url();")
        self.HostEvent2.setObjectName("HostEvent2")
        self.HostEventSeeMoreButton = QtWidgets.QPushButton(MainDialog)
        self.HostEventSeeMoreButton.setGeometry(QtCore.QRect(635, 416, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEventSeeMoreButton.setFont(font)
        self.HostEventSeeMoreButton.setStyleSheet("border-image: \\*url();")
        self.HostEventSeeMoreButton.setObjectName("HostEventSeeMoreButton")
        self.HostEvent3 = QtWidgets.QLabel(MainDialog)
        self.HostEvent3.setGeometry(QtCore.QRect(643, 395, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEvent3.setFont(font)
        self.HostEvent3.setStyleSheet("border-image: \\*url();")
        self.HostEvent3.setObjectName("HostEvent3")
        self.HostEvent1 = QtWidgets.QLabel(MainDialog)
        self.HostEvent1.setGeometry(QtCore.QRect(643, 337, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEvent1.setFont(font)
        self.HostEvent1.setStyleSheet("border-image: \\*url();")
        self.HostEvent1.setObjectName("HostEvent1")
        self.label_12 = QtWidgets.QLabel(MainDialog)
        self.label_12.setGeometry(QtCore.QRect(631, 311, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-image: \\*url();")
        self.label_12.setObjectName("label_12")
        self.scrollArea = QtWidgets.QScrollArea(MainDialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 80, 611, 381))
        self.scrollArea.setStyleSheet("border-image: \\*url();\n"
"background-color: rgba(43, 230, 255,50)\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 609, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(594, 0, 16, 371))
        self.verticalScrollBar.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(24, 97, 255,50)\n"
"\n"
"\n"
"")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.SearchButton = QtWidgets.QPushButton(MainDialog)
        self.SearchButton.setGeometry(QtCore.QRect(4, 40, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("border-image: \\*url();")
        self.SearchButton.setObjectName("SearchButton")
        self.label_2 = QtWidgets.QLabel(MainDialog)
        self.label_2.setGeometry(QtCore.QRect(10, -3, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(34)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: \\*url();")
        self.label_2.setObjectName("label_2")
        self.TimeComboBox = QtWidgets.QComboBox(MainDialog)
        self.TimeComboBox.setGeometry(QtCore.QRect(223, 40, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TimeComboBox.setFont(font)
        self.TimeComboBox.setStyleSheet("border-image: \\*url();")
        self.TimeComboBox.setEditable(False)
        self.TimeComboBox.setObjectName("TimeComboBox")
        self.TimeComboBox.addItem("")
        self.TimeComboBox.addItem("")
        self.TimeComboBox.addItem("")
        self.TimeComboBox.addItem("")
        self.TimeComboBox.addItem("")
        self.TimeComboBox.addItem("")
        self.CatagoryComboBox = QtWidgets.QComboBox(MainDialog)
        self.CatagoryComboBox.setGeometry(QtCore.QRect(90, 40, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CatagoryComboBox.setFont(font)
        self.CatagoryComboBox.setStyleSheet("border-image: \\*url();")
        self.CatagoryComboBox.setEditable(False)
        self.CatagoryComboBox.setObjectName("CatagoryComboBox")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.CatagoryComboBox.addItem("")
        self.PlaceComboBox = QtWidgets.QComboBox(MainDialog)
        self.PlaceComboBox.setGeometry(QtCore.QRect(367, 40, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PlaceComboBox.setFont(font)
        self.PlaceComboBox.setStyleSheet("border-image: \\*url();")
        self.PlaceComboBox.setEditable(False)
        self.PlaceComboBox.setObjectName("PlaceComboBox")
        self.PlaceComboBox.addItem("")
        self.KeywordInput = QtWidgets.QLineEdit(MainDialog)
        self.KeywordInput.setGeometry(QtCore.QRect(472, 44, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.KeywordInput.setFont(font)
        self.KeywordInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.KeywordInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.KeywordInput.setText("")
        self.KeywordInput.setClearButtonEnabled(False)
        self.KeywordInput.setObjectName("KeywordInput")
        self.PostEventButton = QtWidgets.QPushButton(MainDialog)
        self.PostEventButton.setGeometry(QtCore.QRect(630, 122, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PostEventButton.setFont(font)
        self.PostEventButton.setStyleSheet("border-image: \\*url();")
        self.PostEventButton.setObjectName("PostEventButton")

        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Dialog"))
        self.NickName.setText(_translate("MainDialog", "Nickname"))
        self.UpdateProfileButton.setText(_translate("MainDialog", "Update"))
        self.label_5.setText(_translate("MainDialog", "Event Attended"))
        self.AttendEvent1.setText(_translate("MainDialog", "Event Title1"))
        self.AttendEvent2.setText(_translate("MainDialog", "Event Title2"))
        self.AttendEvent3.setText(_translate("MainDialog", "Event Title3"))
        self.HostAttendSeeMoreButton.setText(_translate("MainDialog", "See More"))
        self.HostEvent2.setText(_translate("MainDialog", "Event Title2"))
        self.HostEventSeeMoreButton.setText(_translate("MainDialog", "See More"))
        self.HostEvent3.setText(_translate("MainDialog", "Event Title3"))
        self.HostEvent1.setText(_translate("MainDialog", "Event Title1"))
        self.label_12.setText(_translate("MainDialog", "Event Hosted"))
        self.SearchButton.setText(_translate("MainDialog", "Search"))
        self.label_2.setText(_translate("MainDialog", "JoinMe"))
        self.TimeComboBox.setItemText(0, _translate("MainDialog", "Time"))
        self.TimeComboBox.setItemText(1, _translate("MainDialog", "In One Day"))
        self.TimeComboBox.setItemText(2, _translate("MainDialog", "In Three Days"))
        self.TimeComboBox.setItemText(3, _translate("MainDialog", "In One Week"))
        self.TimeComboBox.setItemText(4, _translate("MainDialog", "In One Month"))
        self.TimeComboBox.setItemText(5, _translate("MainDialog", "Any Time"))
        self.CatagoryComboBox.setItemText(0, _translate("MainDialog", "Catagory"))
        self.CatagoryComboBox.setItemText(1, _translate("MainDialog", "Sports"))
        self.CatagoryComboBox.setItemText(2, _translate("MainDialog", "Social"))
        self.CatagoryComboBox.setItemText(3, _translate("MainDialog", "Outdoors"))
        self.CatagoryComboBox.setItemText(4, _translate("MainDialog", "Indoors"))
        self.CatagoryComboBox.setItemText(5, _translate("MainDialog", "Sightseeing"))
        self.CatagoryComboBox.setItemText(6, _translate("MainDialog", "Exhibitions"))
        self.CatagoryComboBox.setItemText(7, _translate("MainDialog", "Entertaining"))
        self.CatagoryComboBox.setItemText(8, _translate("MainDialog", "Charity"))
        self.CatagoryComboBox.setItemText(9, _translate("MainDialog", "Business"))
        self.CatagoryComboBox.setItemText(10, _translate("MainDialog", "Anything"))
        self.PlaceComboBox.setItemText(0, _translate("MainDialog", "Place"))
        self.PostEventButton.setText(_translate("MainDialog", "Post Event"))

