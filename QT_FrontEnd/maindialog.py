# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
import PyQt5.QtWidgets as QtWidgets


class EventPushButton(QtWidgets.QPushButton):
    def enterEvent(self, *args, **kwargs):
        self.setStyleSheet("color: rgb(28, 0, 255);")
    
    def leaveEvent(self, *args, **kwargs):
        self.setStyleSheet(";")


class EventPushLeftButton(QtWidgets.QPushButton):
    def enterEvent(self, *args, **kwargs):
        self.setStyleSheet("border-image: url(./left2.png);")

    def leaveEvent(self, *args, **kwargs):
        self.setStyleSheet("border-image: url(./left.png);")


class EventPushRightButton(QtWidgets.QPushButton):
    def enterEvent(self, *args, **kwargs):
        self.setStyleSheet("border-image: url(./right2.png);")

    def leaveEvent(self, *args, **kwargs):
        self.setStyleSheet("border-image: url(./right.png);")
  

class Ui_MainDialog(object):
    def setupUi(self, MainDialog):
        MainDialog.setObjectName("MainDialog")
        MainDialog.resize(745, 453)
        MainDialog.setStyleSheet("")
        self.UserImage = QtWidgets.QLabel(MainDialog)
        self.UserImage.setGeometry(QtCore.QRect(650, 10, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UserImage.setFont(font)
        image_profile = QtGui.QImage('./DefaultUser.png')
        self.UserImage.setPixmap(QtGui.QPixmap.fromImage(image_profile).scaled(self.UserImage.width(),
                                                                               self.UserImage.height()))
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
        self.UpdateProfileButton.setStyleSheet("")
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
        self.HostEventSeeMoreButton = QtWidgets.QPushButton(MainDialog)
        self.HostEventSeeMoreButton.setGeometry(QtCore.QRect(635, 416, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEventSeeMoreButton.setFont(font)
        self.HostEventSeeMoreButton.setStyleSheet("border-image: \\*url();")
        self.HostEventSeeMoreButton.setObjectName("HostEventSeeMoreButton")
        self.label_12 = QtWidgets.QLabel(MainDialog)
        self.label_12.setGeometry(QtCore.QRect(631, 311, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-image: \\*url();")
        self.label_12.setObjectName("label_12")
        
        self.SearchButton = QtWidgets.QPushButton(MainDialog)
        self.SearchButton.setGeometry(QtCore.QRect(4, 40, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("border-image: \\*url();")
        self.SearchButton.setObjectName("SearchButton")

        self.LogOutButton = QtWidgets.QPushButton(MainDialog)
        self.LogOutButton.setGeometry(QtCore.QRect(495, 10, 116, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LogOutButton.setFont(font)
        self.LogOutButton.setStyleSheet("border-image: \\*url();")
        self.LogOutButton.setObjectName("LogOutButton")
        
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
        self.PlaceComboBox.setGeometry(QtCore.QRect(367, 40, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PlaceComboBox.setFont(font)
        self.PlaceComboBox.setStyleSheet("border-image: \\*url();")
        self.PlaceComboBox.setEditable(False)
        self.PlaceComboBox.setObjectName("PlaceComboBox")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")
        self.PlaceComboBox.addItem("")

        self.KeywordInput = QtWidgets.QLineEdit(MainDialog)
        self.KeywordInput.setGeometry(QtCore.QRect(502, 44, 101, 21))
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
        self.AttendEvent1 = QtWidgets.QPushButton(MainDialog)
        self.AttendEvent1.setGeometry(QtCore.QRect(623, 173, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AttendEvent1.setFont(font)
        self.AttendEvent1.setStyleSheet("border-image: \\*url();\n"
"background: transparent;\n"
"")
        self.AttendEvent1.setFlat(True)
        self.AttendEvent1.setObjectName("AttendEvent1")
        self.AttendEvent2 = QtWidgets.QPushButton(MainDialog)
        self.AttendEvent2.setGeometry(QtCore.QRect(623, 201, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AttendEvent2.setFont(font)
        self.AttendEvent2.setStyleSheet("border-image: \\*url();\n"
"background: transparent;\n"
"")
        self.AttendEvent2.setFlat(True)
        self.AttendEvent2.setObjectName("AttendEvent2")
        self.AttendEvent3 = QtWidgets.QPushButton(MainDialog)
        self.AttendEvent3.setGeometry(QtCore.QRect(623, 230, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AttendEvent3.setFont(font)
        self.AttendEvent3.setStyleSheet("border-image: \\*url();\n"
"background: transparent;\n"
"")
        self.AttendEvent3.setFlat(True)
        self.AttendEvent3.setObjectName("AttendEvent3")
        self.HostEvent1 = QtWidgets.QPushButton(MainDialog)
        self.HostEvent1.setGeometry(QtCore.QRect(623, 330, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEvent1.setFont(font)
        self.HostEvent1.setStyleSheet("border-image: \\*url();\n"
"background: transparent;\n"
"")
        self.HostEvent1.setFlat(True)
        self.HostEvent1.setObjectName("HostEvent1")
        self.HostEvent2 = QtWidgets.QPushButton(MainDialog)
        self.HostEvent2.setGeometry(QtCore.QRect(623, 360, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEvent2.setFont(font)
        self.HostEvent2.setStyleSheet("border-image: \\*url();\n"
"background: transparent;\n"
"")
        self.HostEvent2.setFlat(True)
        self.HostEvent2.setObjectName("HostEvent2")
        self.HostEvent3 = QtWidgets.QPushButton(MainDialog)
        self.HostEvent3.setGeometry(QtCore.QRect(623, 388, 113, 32))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.HostEvent3.setFont(font)
        self.HostEvent3.setStyleSheet("border-image: \\*url();\n"
"background: transparent;\n"
"")
        self.HostEvent3.setFlat(True)
        self.HostEvent3.setObjectName("HostEvent3")

        self.ScrollAreaAddress1 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaAddress1.setGeometry(QtCore.QRect(302, 146, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaAddress1.setFont(font)
        self.ScrollAreaAddress1.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaAddress1.setObjectName("ScrollAreaAddress1")
        self.ScrollAreaImage1 = QtWidgets.QGraphicsView(MainDialog)
        self.ScrollAreaImage1.setGeometry(QtCore.QRect(43, 106, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaImage1.setFont(font)
        self.ScrollAreaImage1.setStyleSheet("background-color: \\*rgba(43, 230, 255,50);\n"
                                            "background-color: rgba(255, 255, 255)")
        self.ScrollAreaImage1.setObjectName("ScrollAreaImage1")
        self.ScrollAreaEvent1 = EventPushButton(MainDialog)
        self.ScrollAreaEvent1.setGeometry(QtCore.QRect(160, 108, 421, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaEvent1.setFont(font)
        self.ScrollAreaEvent1.setStyleSheet("background-color: rgba(43, 230, 255,0);\n"
                                            "\n"
                                            "")
        self.ScrollAreaEvent1.setFlat(True)
        self.ScrollAreaEvent1.setObjectName("ScrollAreaEvent1")
        self.ScrollAreaDate1 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaDate1.setGeometry(QtCore.QRect(174, 147, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaDate1.setFont(font)
        self.ScrollAreaDate1.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaDate1.setObjectName("ScrollAreaDate1")
        self.ScrollAreaAddress2 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaAddress2.setGeometry(QtCore.QRect(303, 213, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaAddress2.setFont(font)
        self.ScrollAreaAddress2.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaAddress2.setObjectName("ScrollAreaAddress2")
        self.ScrollAreaImage2 = QtWidgets.QGraphicsView(MainDialog)
        self.ScrollAreaImage2.setGeometry(QtCore.QRect(43, 176, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaImage2.setFont(font)
        self.ScrollAreaImage2.setStyleSheet("background-color: \\*rgba(43, 230, 255,50);\n"
                                            "background-color: rgba(255, 255, 255)")
        self.ScrollAreaImage2.setObjectName("ScrollAreaImage2")
        self.ScrollAreaEvent2 = EventPushButton(MainDialog)
        self.ScrollAreaEvent2.setGeometry(QtCore.QRect(160, 178, 421, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaEvent2.setFont(font)
        self.ScrollAreaEvent2.setStyleSheet("background-color: rgba(43, 230, 255,0);\n"
                                            "background: transparent;\n"
                                            "")
        self.ScrollAreaEvent2.setFlat(True)
        self.ScrollAreaEvent2.setObjectName("ScrollAreaEvent2")
        self.ScrollAreaDate2 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaDate2.setGeometry(QtCore.QRect(175, 216, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaDate2.setFont(font)
        self.ScrollAreaDate2.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaDate2.setObjectName("ScrollAreaDate2")
        self.ScrollAreaAddress3 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaAddress3.setGeometry(QtCore.QRect(303, 283, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaAddress3.setFont(font)
        self.ScrollAreaAddress3.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaAddress3.setObjectName("ScrollAreaAddress3")
        self.ScrollAreaEvent3 = EventPushButton(MainDialog)
        self.ScrollAreaEvent3.setGeometry(QtCore.QRect(160, 248, 421, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaEvent3.setFont(font)
        self.ScrollAreaEvent3.setStyleSheet("background-color: rgba(43, 230, 255,0);\n"
                                            "background: transparent;\n"
                                            "")
        self.ScrollAreaEvent3.setFlat(True)
        self.ScrollAreaEvent3.setObjectName("ScrollAreaEvent3")
        self.ScrollAreaImage3 = QtWidgets.QGraphicsView(MainDialog)
        self.ScrollAreaImage3.setGeometry(QtCore.QRect(43, 245, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaImage3.setFont(font)
        self.ScrollAreaImage3.setStyleSheet("background-color: \\*rgba(43, 230, 255,50);\n"
                                            "background-color: rgba(255, 255, 255)")
        self.ScrollAreaImage3.setObjectName("ScrollAreaImage3")
        self.ScrollAreaDate3 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaDate3.setGeometry(QtCore.QRect(175, 285, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaDate3.setFont(font)
        self.ScrollAreaDate3.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaDate3.setObjectName("ScrollAreaDate3")
        self.ScrollAreaAddress4 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaAddress4.setGeometry(QtCore.QRect(303, 353, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaAddress4.setFont(font)
        self.ScrollAreaAddress4.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaAddress4.setObjectName("ScrollAreaAddress4")
        self.ScrollAreaImage4 = QtWidgets.QGraphicsView(MainDialog)
        self.ScrollAreaImage4.setGeometry(QtCore.QRect(43, 316, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaImage4.setFont(font)
        self.ScrollAreaImage4.setStyleSheet("background-color: \\*rgba(43, 230, 255,50);\n"
                                            "background-color: rgba(255, 255, 255)")
        self.ScrollAreaImage4.setObjectName("ScrollAreaImage4")
        self.ScrollAreaEvent4 = EventPushButton(MainDialog)
        self.ScrollAreaEvent4.setGeometry(QtCore.QRect(160, 318, 421, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaEvent4.setFont(font)
        self.ScrollAreaEvent4.setStyleSheet("background-color: rgba(43, 230, 255,0);\n"
                                            "background: transparent;\n"
                                            "")
        self.ScrollAreaEvent4.setFlat(True)
        self.ScrollAreaEvent4.setObjectName("ScrollAreaEvent4")
        self.ScrollAreaDate4 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaDate4.setGeometry(QtCore.QRect(175, 356, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaDate4.setFont(font)
        self.ScrollAreaDate4.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaDate4.setObjectName("ScrollAreaDate4")
        self.ScrollAreaAddress5 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaAddress5.setGeometry(QtCore.QRect(303, 421, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaAddress5.setFont(font)
        self.ScrollAreaAddress5.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaAddress5.setObjectName("ScrollAreaAddress5")
        self.ScrollAreaImage5 = QtWidgets.QGraphicsView(MainDialog)
        self.ScrollAreaImage5.setGeometry(QtCore.QRect(43, 385, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaImage5.setFont(font)
        self.ScrollAreaImage5.setStyleSheet("background-color: \\*rgba(43, 230, 255,50);\n"
                                            "background-color: rgba(255, 255, 255)")
        self.ScrollAreaImage5.setObjectName("ScrollAreaImage5")
        self.ScrollAreaDate5 = QtWidgets.QLabel(MainDialog)
        self.ScrollAreaDate5.setGeometry(QtCore.QRect(175, 423, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaDate5.setFont(font)
        self.ScrollAreaDate5.setStyleSheet("background-color: rgba(43, 230, 255,0)")
        self.ScrollAreaDate5.setObjectName("ScrollAreaDate5")
        self.ScrollAreaEvent5 = EventPushButton(MainDialog)
        self.ScrollAreaEvent5.setGeometry(QtCore.QRect(160, 387, 421, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ScrollAreaEvent5.setFont(font)
        self.ScrollAreaEvent5.setStyleSheet("background-color: rgba(43, 230, 255,100);\n"
                                            "\n"
                                            "")
        self.ScrollAreaEvent5.setFlat(True)
        self.ScrollAreaEvent5.setObjectName("ScrollAreaEvent5")
        self.LastPage = EventPushLeftButton(MainDialog)
        self.LastPage.setGeometry(QtCore.QRect(500, 70, 41, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LastPage.setFont(font)
        self.LastPage.setStyleSheet("border-image: url(./left.png);\n"
                                    "")
        self.LastPage.setText("")
        self.LastPage.setObjectName("LastPage")
        self.NextPage = EventPushRightButton(MainDialog)
        self.NextPage.setGeometry(QtCore.QRect(540, 70, 41, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NextPage.setFont(font)
        self.NextPage.setStyleSheet("border-image: url(./right.png);\n"
                                    "")
        self.NextPage.setText("")
        self.NextPage.setObjectName("NextPage")
        
        
        
        self.graphicsView = QtWidgets.QLabel(MainDialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 751, 461))
        self.graphicsView.setStyleSheet("border-image: url(./bg.png)\n"
"\n"
"")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.UserImage.raise_()
        self.line.raise_()
        self.NickName.raise_()
        self.UpdateProfileButton.raise_()
        self.line_2.raise_()
        self.label_5.raise_()
        self.HostAttendSeeMoreButton.raise_()
        self.line_3.raise_()
        self.HostEventSeeMoreButton.raise_()
        self.label_12.raise_()
        self.SearchButton.raise_()
        self.LogOutButton.raise_()
        self.label_2.raise_()
        self.TimeComboBox.raise_()
        self.CatagoryComboBox.raise_()
        self.PlaceComboBox.raise_()
        self.KeywordInput.raise_()
        self.PostEventButton.raise_()
        self.AttendEvent1.raise_()
        self.AttendEvent2.raise_()
        self.AttendEvent3.raise_()
        self.HostEvent1.raise_()
        self.HostEvent2.raise_()
        self.HostEvent3.raise_()
        self.ScrollAreaAddress1.raise_()
        self.ScrollAreaImage1.raise_()
        self.ScrollAreaEvent1.raise_()
        self.ScrollAreaDate1.raise_()
        self.ScrollAreaAddress2.raise_()
        self.ScrollAreaImage2.raise_()
        self.ScrollAreaEvent2.raise_()
        self.ScrollAreaDate2.raise_()
        self.ScrollAreaAddress3.raise_()
        self.ScrollAreaEvent3.raise_()
        self.ScrollAreaImage3.raise_()
        self.ScrollAreaDate3.raise_()
        self.ScrollAreaAddress4.raise_()
        self.ScrollAreaImage4.raise_()
        self.ScrollAreaEvent4.raise_()
        self.ScrollAreaDate4.raise_()
        self.ScrollAreaAddress5.raise_()
        self.ScrollAreaImage5.raise_()
        self.ScrollAreaDate5.raise_()
        self.ScrollAreaEvent5.raise_()
        self.LastPage.raise_()
        self.NextPage.raise_()
        self.AttendEventList = [self.AttendEvent1, self.AttendEvent2, self.AttendEvent3]
        self.HostEventList = [self.HostEvent1, self.HostEvent2, self.HostEvent3]
        self.ScrollAreaList = [{'title':self.ScrollAreaEvent1,
                                'date':self.ScrollAreaDate1,
                                'address':self.ScrollAreaAddress1,
                                'image':self.ScrollAreaImage1},
                               {'title': self.ScrollAreaEvent2,
                                'date': self.ScrollAreaDate2,
                                'address': self.ScrollAreaAddress2,
                                'image': self.ScrollAreaImage2},
                               {'title': self.ScrollAreaEvent3,
                                'date': self.ScrollAreaDate3,
                                'address': self.ScrollAreaAddress3,
                                'image': self.ScrollAreaImage3},
                               {'title': self.ScrollAreaEvent4,
                                'date': self.ScrollAreaDate4,
                                'address': self.ScrollAreaAddress4,
                                'image': self.ScrollAreaImage4},
                               {'title': self.ScrollAreaEvent5,
                                'date': self.ScrollAreaDate5,
                                'address': self.ScrollAreaAddress5,
                                'image': self.ScrollAreaImage5},
                               ]
        self.retranslateUi(MainDialog)
        QtCore.QMetaObject.connectSlotsByName(MainDialog)

    def retranslateUi(self, MainDialog):
        _translate = QtCore.QCoreApplication.translate
        MainDialog.setWindowTitle(_translate("MainDialog", "Dialog"))
        self.NickName.setText(_translate("MainDialog", "Nickname"))
        self.UpdateProfileButton.setText(_translate("MainDialog", "Update"))
        self.label_5.setText(_translate("MainDialog", "Event Attended"))
        self.HostAttendSeeMoreButton.setText(_translate("MainDialog", "Refresh"))
        self.HostEventSeeMoreButton.setText(_translate("MainDialog", "Refresh"))
        self.label_12.setText(_translate("MainDialog", "Event Hosted"))
        self.SearchButton.setText(_translate("MainDialog", "Search"))
        self.LogOutButton.setText(_translate("MainDialog", "Log Out"))
        self.label_2.setText(_translate("MainDialog", "JoinMe"))
        self.TimeComboBox.setItemText(0, _translate("MainDialog", "Time"))
        self.TimeComboBox.setItemText(1, _translate("MainDialog", "In One Day"))
        self.TimeComboBox.setItemText(2, _translate("MainDialog", "In Three Days"))
        self.TimeComboBox.setItemText(3, _translate("MainDialog", "In One Week"))
        self.TimeComboBox.setItemText(4, _translate("MainDialog", "In One Month"))
        self.CatagoryComboBox.setItemText(0, _translate("MainDialog", "Category"))
        self.CatagoryComboBox.setItemText(1, _translate("MainDialog", "sports"))
        self.CatagoryComboBox.setItemText(2, _translate("MainDialog", "social"))
        self.CatagoryComboBox.setItemText(3, _translate("MainDialog", "outdoors"))
        self.CatagoryComboBox.setItemText(4, _translate("MainDialog", "indoors"))
        self.CatagoryComboBox.setItemText(5, _translate("MainDialog", "sightseeing"))
        self.CatagoryComboBox.setItemText(6, _translate("MainDialog", "exhibitions"))
        self.CatagoryComboBox.setItemText(7, _translate("MainDialog", "entertaining"))
        self.CatagoryComboBox.setItemText(8, _translate("MainDialog", "charity"))
        self.CatagoryComboBox.setItemText(9, _translate("MainDialog", "business"))
        self.CatagoryComboBox.setItemText(10, _translate("MainDialog", "anything"))
        self.PlaceComboBox.setItemText(0, _translate("MainDialog", "Your Place"))

        us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
                     'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
                     'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
                     'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland',
                     'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri',
                     'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
                     'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
                     'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',
                     'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
                     'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

        for i, state in enumerate(us_states):
            self.PlaceComboBox.setItemText(i+1, _translate("MainDialog", state))

        self.KeywordInput.setPlaceholderText(_translate("MainDialog", "Keyword"))
        self.PostEventButton.setText(_translate("MainDialog", "Post Event"))
        
        AttendEventLength = len(self.AttendEventList)
        for i in range(AttendEventLength):
            self.AttendEventList[i].setText(_translate("MainDialog", "Event Title"+str(i+1)))

        HostEventLength = len(self.HostEventList)
        for i in range(HostEventLength):
            self.HostEventList[i].setText(_translate("MainDialog", "Event Title" + str(i + 1)))
        
        ScrollEventLength = len(self.ScrollAreaList)
        for i in range(ScrollEventLength):
            currentEvent = self.ScrollAreaList[i]
            currentEvent['title'].setText(_translate("MainDialog", "Event Title"+str(i+1)))
            currentEvent['date'].setText(_translate("MainDialog", "Date"))
            currentEvent['address'].setText(_translate("MainDialog", "Address"))
            
        
        '''
        self.AttendEvent1.setText(_translate("MainDialog", "Event Title1"))
        self.AttendEvent2.setText(_translate("MainDialog", "Event Title2"))
        self.AttendEvent3.setText(_translate("MainDialog", "Event Title3"))
        self.HostEvent1.setText(_translate("MainDialog", "Event Title1"))
        self.HostEvent2.setText(_translate("MainDialog", "Event Title2"))
        self.HostEvent3.setText(_translate("MainDialog", "Event Title3"))
        '''
        
        '''
        self.ScrollAreaEvent1.setText(_translate("MainDialog", "Event Title1"))
        self.ScrollAreaDate1.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaAddress1.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaDate2.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent2.setText(_translate("MainDialog", "Event Title2"))
        self.ScrollAreaAddress2.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaDate3.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent3.setText(_translate("MainDialog", "Event Title3"))
        self.ScrollAreaAddress3.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaAddress6.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaDate6.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent5.setText(_translate("MainDialog", "Event Title5"))
        self.ScrollAreaDate5.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent6.setText(_translate("MainDialog", "Event Title6"))
        self.ScrollAreaDate4.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaAddress5.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaEvent4.setText(_translate("MainDialog", "Event Title4"))
        self.ScrollAreaAddress4.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaAddress9.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaDate9.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent8.setText(_translate("MainDialog", "Event Title8"))
        self.ScrollAreaDate8.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent9.setText(_translate("MainDialog", "Event Title9"))
        self.ScrollAreaDate7.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaAddress8.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaEvent7.setText(_translate("MainDialog", "Event Title7"))
        self.ScrollAreaAddress7.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaAddress12.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaDate12.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent11.setText(_translate("MainDialog", "Event Title11"))
        self.ScrollAreaDate11.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent12.setText(_translate("MainDialog", "Event Title12"))
        self.ScrollAreaDate10.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaAddress11.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaEvent10.setText(_translate("MainDialog", "Event Title10"))
        self.ScrollAreaAddress10.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaAddress14.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaEvent13.setText(_translate("MainDialog", "Event Title13"))
        self.ScrollAreaAddress15.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaEvent14.setText(_translate("MainDialog", "Event Title14"))
        self.ScrollAreaDate15.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaAddress13.setText(_translate("MainDialog", "Address"))
        self.ScrollAreaDate14.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaDate13.setText(_translate("MainDialog", "Date"))
        self.ScrollAreaEvent15.setText(_translate("MainDialog", "Event Title15"))

        '''
        
