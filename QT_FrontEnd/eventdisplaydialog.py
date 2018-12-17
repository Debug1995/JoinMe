# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventdisplaydialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class EyePushButton(QtWidgets.QPushButton):
    def enterEvent(self, *args, **kwargs):
        self.setStyleSheet("border-image: url(./eye.png);")
        
    def leaveEvent(self, *args, **kwargs):
        self.setStyleSheet("background: transparent;")

class EventPushButton(QtWidgets.QPushButton):
    def enterEvent(self, *args, **kwargs):
        self.setStyleSheet("border-image: url(./pin-22.png);")

    def leaveEvent(self, *args, **kwargs):
        self.setStyleSheet("border-image: url(./pin-2.png);")

class Ui_EventDisplayDialog(object):
    def setupUi(self, EventDisplayDialog):
        EventDisplayDialog.setObjectName("EventDisplayDialog")
        EventDisplayDialog.resize(745, 453)
        EventDisplayDialog.setStyleSheet("")
        self.label_2 = QtWidgets.QLabel(EventDisplayDialog)
        self.label_2.setGeometry(QtCore.QRect(8, 3, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(34)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: \\*url();")
        self.label_2.setObjectName("label_2")
        self.SendEmailButton = QtWidgets.QPushButton(EventDisplayDialog)
        self.SendEmailButton.setGeometry(QtCore.QRect(510, 390, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SendEmailButton.setFont(font)
        self.SendEmailButton.setStyleSheet("border-image: \\*url();")
        self.SendEmailButton.setObjectName("SendEmailButton")
        self.line_2 = QtWidgets.QFrame(EventDisplayDialog)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 600, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(19, 35, 255);\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(EventDisplayDialog)
        self.line_3.setGeometry(QtCore.QRect(0, 80, 600, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(19, 35, 255);\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.UserNameOutput = QtWidgets.QLabel(EventDisplayDialog)
        self.UserNameOutput.setGeometry(QtCore.QRect(8, 55, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.UserNameOutput.setFont(font)
        self.UserNameOutput.setStyleSheet("border-image: \\*url();")
        self.UserNameOutput.setObjectName("UserNameOutput")
        self.UserName_2 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_2.setGeometry(QtCore.QRect(9, 90, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_2.setFont(font)
        self.UserName_2.setStyleSheet("border-image: \\*url();")
        self.UserName_2.setObjectName("UserName_2")
        self.UserName_3 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_3.setGeometry(QtCore.QRect(10, 180, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_3.setFont(font)
        self.UserName_3.setStyleSheet("border-image: \\*url();")
        self.UserName_3.setObjectName("UserName_3")
        self.DescriptionOutput = QtWidgets.QLabel(EventDisplayDialog)
        self.DescriptionOutput.setGeometry(QtCore.QRect(10, 120, 551, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DescriptionOutput.setFont(font)
        self.DescriptionOutput.setStyleSheet("border-image: \\*url();")
        self.DescriptionOutput.setWordWrap(True)
        self.DescriptionOutput.setObjectName("DescriptionOutput")
        self.UserName_5 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_5.setGeometry(QtCore.QRect(300, 180, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_5.setFont(font)
        self.UserName_5.setStyleSheet("border-image: \\*url();")
        self.UserName_5.setObjectName("UserName_5")
        self.AddressOutput = QtWidgets.QLabel(EventDisplayDialog)
        self.AddressOutput.setGeometry(QtCore.QRect(90, 180, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AddressOutput.setFont(font)
        self.AddressOutput.setStyleSheet("border-image: \\*url();")
        self.AddressOutput.setObjectName("AddressOutput")
        self.CityOutput = QtWidgets.QLabel(EventDisplayDialog)
        self.CityOutput.setGeometry(QtCore.QRect(340, 180, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CityOutput.setFont(font)
        self.CityOutput.setStyleSheet("border-image: \\*url();")
        self.CityOutput.setObjectName("CityOutput")
        self.UserName_8 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_8.setGeometry(QtCore.QRect(10, 220, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_8.setFont(font)
        self.UserName_8.setStyleSheet("border-image: \\*url();")
        self.UserName_8.setObjectName("UserName_8")
        self.HostIDOutput = QtWidgets.QLabel(EventDisplayDialog)
        self.HostIDOutput.setGeometry(QtCore.QRect(60, 220, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.HostIDOutput.setFont(font)
        self.HostIDOutput.setStyleSheet("border-image: \\*url();")
        self.HostIDOutput.setObjectName("HostIDOutput")
        self.UserName_10 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_10.setGeometry(QtCore.QRect(10, 260, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_10.setFont(font)
        self.UserName_10.setStyleSheet("border-image: \\*url();")
        self.UserName_10.setObjectName("UserName_10")
        self.UserName_11 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_11.setGeometry(QtCore.QRect(10, 340, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_11.setFont(font)
        self.UserName_11.setStyleSheet("border-image: \\*url();")
        self.UserName_11.setObjectName("UserName_11")
        self.AttendEventButton = QtWidgets.QPushButton(EventDisplayDialog)
        self.AttendEventButton.setGeometry(QtCore.QRect(608, 60, 81, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AttendEventButton.setFont(font)
        self.AttendEventButton.setStyleSheet("border-image: \\*url();")
        self.AttendEventButton.setObjectName("AttendEventButton")
        self.UserName_12 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_12.setGeometry(QtCore.QRect(620, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_12.setFont(font)
        self.UserName_12.setStyleSheet("border-image: \\*url();")
        self.UserName_12.setObjectName("UserName_12")
        self.EventIamge1 = QtWidgets.QLabel(EventDisplayDialog)
        self.EventIamge1.setGeometry(QtCore.QRect(580, 112, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EventIamge1.setFont(font)
        self.EventIamge1.setStyleSheet("")
        self.EventIamge1.setObjectName("EventIamge1")
        self.EventIamge2 = QtWidgets.QLabel(EventDisplayDialog)
        self.EventIamge2.setGeometry(QtCore.QRect(580, 200, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EventIamge2.setFont(font)
        self.EventIamge2.setStyleSheet("")
        self.EventIamge2.setObjectName("EventIamge2")
        self.EventIamge3 = QtWidgets.QLabel(EventDisplayDialog)
        self.EventIamge3.setGeometry(QtCore.QRect(580, 290, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EventIamge3.setFont(font)
        self.EventIamge3.setStyleSheet("")
        self.EventIamge3.setObjectName("EventIamge3")
        self.UserName_13 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_13.setGeometry(QtCore.QRect(630, 380, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_13.setFont(font)
        self.UserName_13.setStyleSheet("border-image: \\*url();")
        self.UserName_13.setObjectName("UserName_13")
        


        self.mapView = EventPushButton(EventDisplayDialog)
        self.mapView.setGeometry(QtCore.QRect(630, 402, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mapView.setFont(font)
        self.mapView.setStyleSheet("border-image: url(./pin-2.png)")
        self.mapView.setText("")
        self.mapView.setObjectName("mapView")
        
        self.UserName_9 = QtWidgets.QLabel(EventDisplayDialog)
        self.UserName_9.setGeometry(QtCore.QRect(300, 220, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_9.setFont(font)
        self.UserName_9.setStyleSheet("border-image: \\*url();")
        self.UserName_9.setObjectName("UserName_9")
        self.DateOutput = QtWidgets.QLabel(EventDisplayDialog)
        self.DateOutput.setGeometry(QtCore.QRect(344, 220, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DateOutput.setFont(font)
        self.DateOutput.setStyleSheet("border-image: \\*url();")
        self.DateOutput.setObjectName("DateOutput")
        self.graphicsView = QtWidgets.QGraphicsView(EventDisplayDialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 745, 453))
        self.graphicsView.setStyleSheet("border-image: url(./bg.png)\n"
"\n"
"")
        self.graphicsView.setObjectName("graphicsView")
        self.ToEmailInput = QtWidgets.QTextEdit(EventDisplayDialog)
        self.ToEmailInput.setGeometry(QtCore.QRect(10, 362, 501, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ToEmailInput.setFont(font)
        self.ToEmailInput.setAutoFillBackground(False)
        self.ToEmailInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.ToEmailInput.setObjectName("ToEmailInput")
        self.BackButton = QtWidgets.QPushButton(EventDisplayDialog)
        self.BackButton.setGeometry(QtCore.QRect(608, 37, 81, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackButton.setFont(font)
        self.BackButton.setStyleSheet("border-image: \\*url();")
        self.BackButton.setObjectName("BackButton")
        self.Attendee1 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee1.setGeometry(QtCore.QRect(28, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee1.setFont(font)
        self.Attendee1.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee1.setText("")
        self.Attendee1.setObjectName("Attendee1")
        self.Attendee2 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee2.setGeometry(QtCore.QRect(78, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee2.setFont(font)
        self.Attendee2.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee2.setText("")
        self.Attendee2.setObjectName("Attendee2")
        self.Attendee3 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee3.setGeometry(QtCore.QRect(128, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee3.setFont(font)
        self.Attendee3.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee3.setText("")
        self.Attendee3.setObjectName("Attendee3")
        self.Attendee5 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee5.setGeometry(QtCore.QRect(228, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee5.setFont(font)
        self.Attendee5.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee5.setText("")
        self.Attendee5.setObjectName("Attendee5")
        self.Attendee10 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee10.setGeometry(QtCore.QRect(478, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee10.setFont(font)
        self.Attendee10.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee10.setText("")
        self.Attendee10.setObjectName("Attendee10")
        self.Attendee4 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee4.setGeometry(QtCore.QRect(178, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee4.setFont(font)
        self.Attendee4.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee4.setText("")
        self.Attendee4.setObjectName("Attendee4")
        self.Attendee9 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee9.setGeometry(QtCore.QRect(428, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee9.setFont(font)
        self.Attendee9.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee9.setText("")
        self.Attendee9.setObjectName("Attendee9")
        self.Attendee7 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee7.setGeometry(QtCore.QRect(328, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee7.setFont(font)
        self.Attendee7.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee7.setText("")
        self.Attendee7.setObjectName("Attendee7")
        self.Attendee8 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee8.setGeometry(QtCore.QRect(378, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee8.setFont(font)
        self.Attendee8.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee8.setText("")
        self.Attendee8.setObjectName("Attendee8")
        self.Attendee6 = QtWidgets.QLabel(EventDisplayDialog)
        self.Attendee6.setGeometry(QtCore.QRect(278, 295, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee6.setFont(font)
        self.Attendee6.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee6.setText("")
        self.Attendee6.setObjectName("Attendee6")

        

        self.eye1 = EyePushButton(EventDisplayDialog)
        self.eye1.setGeometry(QtCore.QRect(41, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye1.setFont(font)
        self.eye1.setStyleSheet("background: transparent;")
        self.eye1.setText("")
        self.eye1.setObjectName("eye1")

        self.eye2 = EyePushButton(EventDisplayDialog)
        self.eye2.setGeometry(QtCore.QRect(91, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye2.setFont(font)
        self.eye2.setStyleSheet("background: transparent;")
        self.eye2.setText("")
        self.eye2.setObjectName("eye2")

        self.eye3 = EyePushButton(EventDisplayDialog)
        self.eye3.setGeometry(QtCore.QRect(141, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye3.setFont(font)
        self.eye3.setStyleSheet("background: transparent;")
        self.eye3.setText("")
        self.eye3.setObjectName("eye3")

        self.eye4 = EyePushButton(EventDisplayDialog)
        self.eye4.setGeometry(QtCore.QRect(191, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye4.setFont(font)
        self.eye4.setStyleSheet("background: transparent;")
        self.eye4.setText("")
        self.eye4.setObjectName("eye4")

        self.eye5 = EyePushButton(EventDisplayDialog)
        self.eye5.setGeometry(QtCore.QRect(241, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye5.setFont(font)
        self.eye5.setStyleSheet("background: transparent;")
        self.eye5.setText("")
        self.eye5.setObjectName("eye5")

        self.eye6 = EyePushButton(EventDisplayDialog)
        self.eye6.setGeometry(QtCore.QRect(291, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye6.setFont(font)
        self.eye6.setStyleSheet("background: transparent;")
        self.eye6.setText("")
        self.eye6.setObjectName("eye6")

        self.eye7 = EyePushButton(EventDisplayDialog)
        self.eye7.setGeometry(QtCore.QRect(341, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye7.setFont(font)
        self.eye7.setStyleSheet("background: transparent;")
        self.eye7.setText("")
        self.eye7.setObjectName("eye7")

        self.eye8 = EyePushButton(EventDisplayDialog)
        self.eye8.setGeometry(QtCore.QRect(391, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye8.setFont(font)
        self.eye8.setStyleSheet("background: transparent;")
        self.eye8.setText("")
        self.eye8.setObjectName("eye8")

        self.eye9 = EyePushButton(EventDisplayDialog)
        self.eye9.setGeometry(QtCore.QRect(441, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye9.setFont(font)
        self.eye9.setStyleSheet("background: transparent;")
        self.eye9.setText("")
        self.eye9.setObjectName("eye9")

        self.eye10 = EyePushButton(EventDisplayDialog)
        self.eye10.setGeometry(QtCore.QRect(491, 290, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eye10.setFont(font)
        self.eye10.setStyleSheet("background: transparent;")
        self.eye10.setText("")
        self.eye10.setObjectName("eye10")
        self.eyeList = [
                self.eye1,
                self.eye2,
                self.eye3,
                self.eye4,
                self.eye5,
                self.eye6,
                self.eye7,
                self.eye8,
                self.eye9,
                self.eye10,
                ]
        
        self.AttendeeList = [self.Attendee1,
                             self.Attendee2,
                             self.Attendee3,
                             self.Attendee4,
                             self.Attendee5,
                             self.Attendee6,
                             self.Attendee7,
                             self.Attendee8,
                             self.Attendee9,
                             self.Attendee10,
                             ]
        
        self.Hostimage = QtWidgets.QLabel(EventDisplayDialog)
        self.Hostimage.setGeometry(QtCore.QRect(221, 215, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Hostimage.setFont(font)
        self.Hostimage.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Hostimage.setText("")
        self.Hostimage.setObjectName("Hostimage")

        self.eyeHost = EyePushButton(EventDisplayDialog)
        self.eyeHost.setGeometry(QtCore.QRect(235, 210, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.eyeHost.setFont(font)
        self.eyeHost.setStyleSheet("background: transparent;")
        self.eyeHost.setText("")
        self.eyeHost.setObjectName("eyeHost")
        
        self.graphicsView.raise_()
        self.label_2.raise_()
        self.SendEmailButton.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.UserNameOutput.raise_()
        self.UserName_2.raise_()
        self.UserName_3.raise_()
        self.DescriptionOutput.raise_()
        self.UserName_5.raise_()
        self.AddressOutput.raise_()
        self.CityOutput.raise_()
        self.UserName_8.raise_()
        self.HostIDOutput.raise_()
        self.UserName_10.raise_()
        self.UserName_11.raise_()
        self.AttendEventButton.raise_()
        self.UserName_12.raise_()
        self.EventIamge1.raise_()
        self.EventIamge2.raise_()
        self.EventIamge3.raise_()
        self.UserName_13.raise_()
        self.mapView.raise_()
        self.UserName_9.raise_()
        self.DateOutput.raise_()
        self.ToEmailInput.raise_()
        self.BackButton.raise_()
        self.Attendee1.raise_()
        self.Attendee2.raise_()
        self.Attendee3.raise_()
        self.Attendee5.raise_()
        self.Attendee10.raise_()
        self.Attendee4.raise_()
        self.Attendee9.raise_()
        self.Attendee7.raise_()
        self.Attendee8.raise_()
        self.Attendee6.raise_()
        self.Hostimage.raise_()
        self.eye1.raise_()
        self.eye2.raise_()
        self.eye3.raise_()
        self.eye4.raise_()
        self.eye5.raise_()
        self.eye6.raise_()
        self.eye7.raise_()
        self.eye8.raise_()
        self.eye9.raise_()
        self.eye10.raise_()
        self.eyeHost.raise_()

        self.retranslateUi(EventDisplayDialog)
        QtCore.QMetaObject.connectSlotsByName(EventDisplayDialog)

    def retranslateUi(self, EventDisplayDialog):
        _translate = QtCore.QCoreApplication.translate
        EventDisplayDialog.setWindowTitle(_translate("EventDisplayDialog", "Dialog"))
        self.label_2.setText(_translate("EventDisplayDialog", "JoinMe"))
        self.SendEmailButton.setText(_translate("EventDisplayDialog", "Send"))
        self.UserNameOutput.setText(_translate("EventDisplayDialog", "Title of the event"))
        self.UserName_2.setText(_translate("EventDisplayDialog", "Description"))
        self.UserName_3.setText(_translate("EventDisplayDialog", "Address"))
        self.DescriptionOutput.setText(_translate("EventDisplayDialog", "I\'m a description. I\'m a description. I\'m a description. I\'m a description. I\'m a description. I\'m a description. I\'m a description.I\'m a description.I\'m a description.I\'m a description.I\'m a description.I\'m a description."))
        self.UserName_5.setText(_translate("EventDisplayDialog", "City"))
        self.AddressOutput.setText(_translate("EventDisplayDialog", "I\'m address I\'m address"))
        self.CityOutput.setText(_translate("EventDisplayDialog", "I\'m city I\'m city"))
        self.UserName_8.setText(_translate("EventDisplayDialog", "Host"))
        self.HostIDOutput.setText(_translate("EventDisplayDialog", "I\'m Host Nickname"))
        self.UserName_10.setText(_translate("EventDisplayDialog", "Attendee"))
        self.UserName_11.setText(_translate("EventDisplayDialog", "Contact"))
        self.AttendEventButton.setText(_translate("EventDisplayDialog", "Attend"))
        self.UserName_12.setText(_translate("EventDisplayDialog", "Images"))
        self.UserName_13.setText(_translate("EventDisplayDialog", "map"))
        self.UserName_9.setText(_translate("EventDisplayDialog", "Date"))
        self.DateOutput.setText(_translate("EventDisplayDialog", "I\'m Date I\'m Date"))
        self.ToEmailInput.setWhatsThis(_translate("EventDisplayDialog", "ddd"))
        self.ToEmailInput.setPlaceholderText(_translate("EventDisplayDialog", "Please input your email content..."))
        self.BackButton.setText(_translate("EventDisplayDialog", "Back"))

