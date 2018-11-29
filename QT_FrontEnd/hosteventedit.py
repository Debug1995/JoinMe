# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hosteventedit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HostEventEdit(object):
    def setupUi(self, HostEventEdit):
        HostEventEdit.setObjectName("HostEventEdit")
        HostEventEdit.resize(745, 453)
        HostEventEdit.setStyleSheet("")
        self.line_2 = QtWidgets.QFrame(HostEventEdit)
        self.line_2.setGeometry(QtCore.QRect(0, 47, 640, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(19, 35, 255);\n"
"")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.UserName_5 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_5.setGeometry(QtCore.QRect(430, 170, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_5.setFont(font)
        self.UserName_5.setStyleSheet("border-image: \\*url();")
        self.UserName_5.setObjectName("UserName_5")
        self.SaveEventButton = QtWidgets.QPushButton(HostEventEdit)
        self.SaveEventButton.setGeometry(QtCore.QRect(651, 46, 81, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SaveEventButton.setFont(font)
        self.SaveEventButton.setStyleSheet("border-image: \\*url();")
        self.SaveEventButton.setObjectName("SaveEventButton")
        self.label_2 = QtWidgets.QLabel(HostEventEdit)
        self.label_2.setGeometry(QtCore.QRect(8, 0, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(34)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: \\*url();")
        self.label_2.setObjectName("label_2")
        self.UserName = QtWidgets.QLabel(HostEventEdit)
        self.UserName.setGeometry(QtCore.QRect(8, 52, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("border-image: \\*url();")
        self.UserName.setObjectName("UserName")
        self.EventImage1 = QtWidgets.QLabel(HostEventEdit)
        self.EventImage1.setGeometry(QtCore.QRect(97, 340, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EventImage1.setFont(font)
        image_profile = QtGui.QImage('./DefaultImage.png')
        self.EventImage1.setPixmap(QtGui.QPixmap.fromImage(image_profile).scaled(self.EventImage1.width(),
                                                                                 self.EventImage1.height()))
        self.EventImage1.setObjectName("EventImage1")
        self.line_3 = QtWidgets.QFrame(HostEventEdit)
        self.line_3.setGeometry(QtCore.QRect(0, 77, 640, 2))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("border-image: \\*url();\n"
"background-color: rgb(19, 35, 255);\n"
"")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.UserName_12 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_12.setGeometry(QtCore.QRect(50, 310, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_12.setFont(font)
        self.UserName_12.setStyleSheet("border-image: \\*url();")
        self.UserName_12.setObjectName("UserName_12")
        self.UserName_2 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_2.setGeometry(QtCore.QRect(49, 80, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_2.setFont(font)
        self.UserName_2.setStyleSheet("border-image: \\*url();")
        self.UserName_2.setObjectName("UserName_2")
        self.UserName_10 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_10.setGeometry(QtCore.QRect(50, 250, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_10.setFont(font)
        self.UserName_10.setStyleSheet("border-image: \\*url();")
        self.UserName_10.setObjectName("UserName_10")
        self.UserName_3 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_3.setGeometry(QtCore.QRect(50, 170, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_3.setFont(font)
        self.UserName_3.setStyleSheet("border-image: \\*url();")
        self.UserName_3.setObjectName("UserName_3")
        self.AddressInput = QtWidgets.QLineEdit(HostEventEdit)
        self.AddressInput.setGeometry(QtCore.QRect(120, 170, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AddressInput.setFont(font)
        self.AddressInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.AddressInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.AddressInput.setText("")
        self.AddressInput.setPlaceholderText("")
        self.AddressInput.setClearButtonEnabled(False)
        self.AddressInput.setObjectName("AddressInput")
        self.CityInput = QtWidgets.QLineEdit(HostEventEdit)
        self.CityInput.setGeometry(QtCore.QRect(470, 170, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CityInput.setFont(font)
        self.CityInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.CityInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.CityInput.setText("")
        self.CityInput.setPlaceholderText("")
        self.CityInput.setClearButtonEnabled(False)
        self.CityInput.setObjectName("CityInput")
        self.TitleInput = QtWidgets.QLineEdit(HostEventEdit)
        self.TitleInput.setGeometry(QtCore.QRect(50, 53, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TitleInput.setFont(font)
        self.TitleInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.TitleInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.TitleInput.setText("")
        self.TitleInput.setPlaceholderText("")
        self.TitleInput.setClearButtonEnabled(False)
        self.TitleInput.setObjectName("TitleInput")
        self.UploadImage1 = QtWidgets.QPushButton(HostEventEdit)
        self.UploadImage1.setGeometry(QtCore.QRect(120, 420, 81, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UploadImage1.setFont(font)
        self.UploadImage1.setStyleSheet("border-image: \\*url();")
        self.UploadImage1.setObjectName("UploadImage1")
        self.UserName_4 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_4.setGeometry(QtCore.QRect(50, 196, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_4.setFont(font)
        self.UserName_4.setStyleSheet("border-image: \\*url();")
        self.UserName_4.setObjectName("UserName_4")
        self.UserName_6 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_6.setGeometry(QtCore.QRect(50, 222, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_6.setFont(font)
        self.UserName_6.setStyleSheet("border-image: \\*url();")
        self.UserName_6.setObjectName("UserName_6")
        self.UserName_7 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_7.setGeometry(QtCore.QRect(410, 222, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_7.setFont(font)
        self.UserName_7.setStyleSheet("border-image: \\*url();")
        self.UserName_7.setObjectName("UserName_7")
        self.PeriodTimeInput = QtWidgets.QLineEdit(HostEventEdit)
        self.PeriodTimeInput.setGeometry(QtCore.QRect(510, 221, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PeriodTimeInput.setFont(font)
        self.PeriodTimeInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.PeriodTimeInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.PeriodTimeInput.setText("")
        self.PeriodTimeInput.setClearButtonEnabled(False)
        self.PeriodTimeInput.setObjectName("PeriodTimeInput")
        self.YearComboBox = QtWidgets.QComboBox(HostEventEdit)
        self.YearComboBox.setGeometry(QtCore.QRect(140, 220, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.YearComboBox.setFont(font)
        self.YearComboBox.setStyleSheet("border-image: \\*url();")
        self.YearComboBox.setEditable(False)
        self.YearComboBox.setObjectName("YearComboBox")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.YearComboBox.addItem("")
        self.MonthComboBox = QtWidgets.QComboBox(HostEventEdit)
        self.MonthComboBox.setGeometry(QtCore.QRect(220, 220, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MonthComboBox.setFont(font)
        self.MonthComboBox.setStyleSheet("border-image: \\*url();")
        self.MonthComboBox.setEditable(False)
        self.MonthComboBox.setObjectName("MonthComboBox")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.MonthComboBox.addItem("")
        self.DayComboBox = QtWidgets.QComboBox(HostEventEdit)
        self.DayComboBox.setGeometry(QtCore.QRect(310, 220, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DayComboBox.setFont(font)
        self.DayComboBox.setStyleSheet("border-image: \\*url();")
        self.DayComboBox.setEditable(False)
        self.DayComboBox.setObjectName("DayComboBox")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.DayComboBox.addItem("")
        self.CatagoryComboBox = QtWidgets.QComboBox(HostEventEdit)
        self.CatagoryComboBox.setGeometry(QtCore.QRect(90, 194, 131, 30))
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
        self.graphicsView = QtWidgets.QGraphicsView(HostEventEdit)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 745, 453))
        self.graphicsView.setStyleSheet("border-image: url(./bg.png)\n"
"\n"
"")
        self.graphicsView.setObjectName("graphicsView")
        self.UserName_8 = QtWidgets.QLabel(HostEventEdit)
        self.UserName_8.setGeometry(QtCore.QRect(588, 221, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.UserName_8.setFont(font)
        self.UserName_8.setStyleSheet("border-image: \\*url();")
        self.UserName_8.setObjectName("UserName_8")
        self.DescriptionInput = QtWidgets.QTextEdit(HostEventEdit)
        self.DescriptionInput.setGeometry(QtCore.QRect(50, 100, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DescriptionInput.setFont(font)
        self.DescriptionInput.setAutoFillBackground(False)
        self.DescriptionInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.DescriptionInput.setObjectName("DescriptionInput")
        self.Attendee4 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee4.setGeometry(QtCore.QRect(280, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee4.setFont(font)
        self.Attendee4.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee4.setText("")
        self.Attendee4.setObjectName("Attendee4")
        self.Attendee6 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee6.setGeometry(QtCore.QRect(380, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee6.setFont(font)
        self.Attendee6.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee6.setText("")
        self.Attendee6.setObjectName("Attendee6")
        self.Attendee2 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee2.setGeometry(QtCore.QRect(180, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee2.setFont(font)
        self.Attendee2.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee2.setText("")
        self.Attendee2.setObjectName("Attendee2")
        self.Attendee7 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee7.setGeometry(QtCore.QRect(430, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee7.setFont(font)
        self.Attendee7.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee7.setText("")
        self.Attendee7.setObjectName("Attendee7")
        self.Attendee8 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee8.setGeometry(QtCore.QRect(480, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee8.setFont(font)
        self.Attendee8.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee8.setText("")
        self.Attendee8.setObjectName("Attendee8")
        self.Attendee3 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee3.setGeometry(QtCore.QRect(230, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee3.setFont(font)
        self.Attendee3.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee3.setText("")
        self.Attendee3.setObjectName("Attendee3")
        self.Attendee9 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee9.setGeometry(QtCore.QRect(530, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee9.setFont(font)
        self.Attendee9.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee9.setText("")
        self.Attendee9.setObjectName("Attendee9")
        self.Attendee1 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee1.setGeometry(QtCore.QRect(130, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee1.setFont(font)
        self.Attendee1.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee1.setText("")
        self.Attendee1.setObjectName("Attendee1")
        self.Attendee10 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee10.setGeometry(QtCore.QRect(580, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee10.setFont(font)
        self.Attendee10.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee10.setText("")
        self.Attendee10.setObjectName("Attendee10")
        self.Attendee5 = QtWidgets.QPushButton(HostEventEdit)
        self.Attendee5.setGeometry(QtCore.QRect(330, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Attendee5.setFont(font)
        self.Attendee5.setStyleSheet("border-image: url(./DefaultUser.png);\n"
"")
        self.Attendee5.setText("")
        self.Attendee5.setObjectName("Attendee5")
        self.graphicsView.raise_()
        self.line_2.raise_()
        self.UserName_5.raise_()
        self.SaveEventButton.raise_()
        self.label_2.raise_()
        self.UserName.raise_()
        self.EventImage1.raise_()
        self.line_3.raise_()
        self.UserName_12.raise_()
        self.UserName_2.raise_()
        self.UserName_10.raise_()
        self.UserName_3.raise_()
        self.AddressInput.raise_()
        self.CityInput.raise_()
        self.TitleInput.raise_()
        self.UploadImage1.raise_()
        self.UserName_4.raise_()
        self.UserName_6.raise_()
        self.UserName_7.raise_()
        self.PeriodTimeInput.raise_()
        self.YearComboBox.raise_()
        self.MonthComboBox.raise_()
        self.DayComboBox.raise_()
        self.CatagoryComboBox.raise_()
        self.UserName_8.raise_()
        self.DescriptionInput.raise_()
        self.Attendee4.raise_()
        self.Attendee6.raise_()
        self.Attendee2.raise_()
        self.Attendee7.raise_()
        self.Attendee8.raise_()
        self.Attendee3.raise_()
        self.Attendee9.raise_()
        self.Attendee1.raise_()
        self.Attendee10.raise_()
        self.Attendee5.raise_()

        self.retranslateUi(HostEventEdit)
        QtCore.QMetaObject.connectSlotsByName(HostEventEdit)

    def retranslateUi(self, HostEventEdit):
        _translate = QtCore.QCoreApplication.translate
        HostEventEdit.setWindowTitle(_translate("HostEventEdit", "Dialog"))
        self.UserName_5.setText(_translate("HostEventEdit", "City"))
        self.SaveEventButton.setText(_translate("HostEventEdit", "Save"))
        self.label_2.setText(_translate("HostEventEdit", "JoinMe"))
        self.UserName.setText(_translate("HostEventEdit", "Title"))
        self.UserName_12.setText(_translate("HostEventEdit", "Images"))
        self.UserName_2.setText(_translate("HostEventEdit", "Description"))
        self.UserName_10.setText(_translate("HostEventEdit", "Attendee"))
        self.UserName_3.setText(_translate("HostEventEdit", "Address"))
        self.UploadImage1.setText(_translate("HostEventEdit", "Upload"))
        self.UserName_4.setText(_translate("HostEventEdit", "Tags"))
        self.UserName_6.setText(_translate("HostEventEdit", "Event Date"))
        self.UserName_7.setText(_translate("HostEventEdit", "Time Period"))
        self.PeriodTimeInput.setPlaceholderText(_translate("HostEventEdit", "Number"))
        self.YearComboBox.setItemText(0, _translate("HostEventEdit", "Year"))
        self.YearComboBox.setItemText(1, _translate("HostEventEdit", "2018"))
        self.YearComboBox.setItemText(2, _translate("HostEventEdit", "2019"))
        self.YearComboBox.setItemText(3, _translate("HostEventEdit", "2020"))
        self.YearComboBox.setItemText(4, _translate("HostEventEdit", "2021"))
        self.YearComboBox.setItemText(5, _translate("HostEventEdit", "2022"))
        self.YearComboBox.setItemText(6, _translate("HostEventEdit", "2023"))
        self.YearComboBox.setItemText(7, _translate("HostEventEdit", "2024"))
        self.YearComboBox.setItemText(8, _translate("HostEventEdit", "2025"))
        self.YearComboBox.setItemText(9, _translate("HostEventEdit", "2026"))
        self.YearComboBox.setItemText(10, _translate("HostEventEdit", "2027"))
        self.YearComboBox.setItemText(11, _translate("HostEventEdit", "2028"))
        self.MonthComboBox.setItemText(0, _translate("HostEventEdit", "Month"))
        self.MonthComboBox.setItemText(1, _translate("HostEventEdit", "01"))
        self.MonthComboBox.setItemText(2, _translate("HostEventEdit", "02"))
        self.MonthComboBox.setItemText(3, _translate("HostEventEdit", "03"))
        self.MonthComboBox.setItemText(4, _translate("HostEventEdit", "04"))
        self.MonthComboBox.setItemText(5, _translate("HostEventEdit", "05"))
        self.MonthComboBox.setItemText(6, _translate("HostEventEdit", "06"))
        self.MonthComboBox.setItemText(7, _translate("HostEventEdit", "07"))
        self.MonthComboBox.setItemText(8, _translate("HostEventEdit", "08"))
        self.MonthComboBox.setItemText(9, _translate("HostEventEdit", "09"))
        self.MonthComboBox.setItemText(10, _translate("HostEventEdit", "10"))
        self.MonthComboBox.setItemText(11, _translate("HostEventEdit", "11"))
        self.MonthComboBox.setItemText(12, _translate("HostEventEdit", "12"))
        self.DayComboBox.setItemText(0, _translate("HostEventEdit", "Day"))
        self.DayComboBox.setItemText(1, _translate("HostEventEdit", "01"))
        self.DayComboBox.setItemText(2, _translate("HostEventEdit", "02"))
        self.DayComboBox.setItemText(3, _translate("HostEventEdit", "03"))
        self.DayComboBox.setItemText(4, _translate("HostEventEdit", "04"))
        self.DayComboBox.setItemText(5, _translate("HostEventEdit", "05"))
        self.DayComboBox.setItemText(6, _translate("HostEventEdit", "06"))
        self.DayComboBox.setItemText(7, _translate("HostEventEdit", "07"))
        self.DayComboBox.setItemText(8, _translate("HostEventEdit", "08"))
        self.DayComboBox.setItemText(9, _translate("HostEventEdit", "09"))
        self.DayComboBox.setItemText(10, _translate("HostEventEdit", "10"))
        self.DayComboBox.setItemText(11, _translate("HostEventEdit", "11"))
        self.DayComboBox.setItemText(12, _translate("HostEventEdit", "12"))
        self.DayComboBox.setItemText(13, _translate("HostEventEdit", "13"))
        self.DayComboBox.setItemText(14, _translate("HostEventEdit", "14"))
        self.DayComboBox.setItemText(15, _translate("HostEventEdit", "15"))
        self.DayComboBox.setItemText(16, _translate("HostEventEdit", "16"))
        self.DayComboBox.setItemText(17, _translate("HostEventEdit", "17"))
        self.DayComboBox.setItemText(18, _translate("HostEventEdit", "18"))
        self.DayComboBox.setItemText(19, _translate("HostEventEdit", "19"))
        self.DayComboBox.setItemText(20, _translate("HostEventEdit", "20"))
        self.DayComboBox.setItemText(21, _translate("HostEventEdit", "21"))
        self.DayComboBox.setItemText(22, _translate("HostEventEdit", "22"))
        self.DayComboBox.setItemText(23, _translate("HostEventEdit", "23"))
        self.DayComboBox.setItemText(24, _translate("HostEventEdit", "24"))
        self.DayComboBox.setItemText(25, _translate("HostEventEdit", "25"))
        self.DayComboBox.setItemText(26, _translate("HostEventEdit", "26"))
        self.DayComboBox.setItemText(27, _translate("HostEventEdit", "27"))
        self.DayComboBox.setItemText(28, _translate("HostEventEdit", "28"))
        self.DayComboBox.setItemText(29, _translate("HostEventEdit", "29"))
        self.DayComboBox.setItemText(30, _translate("HostEventEdit", "30"))
        self.DayComboBox.setItemText(31, _translate("HostEventEdit", "31"))
        self.CatagoryComboBox.setItemText(0, _translate("HostEventEdit", "Tags"))
        self.CatagoryComboBox.setItemText(1, _translate("HostEventEdit", "sports"))
        self.CatagoryComboBox.setItemText(2, _translate("HostEventEdit", "social"))
        self.CatagoryComboBox.setItemText(3, _translate("HostEventEdit", "outdoors"))
        self.CatagoryComboBox.setItemText(4, _translate("HostEventEdit", "indoors"))
        self.CatagoryComboBox.setItemText(5, _translate("HostEventEdit", "sightseeing"))
        self.CatagoryComboBox.setItemText(6, _translate("HostEventEdit", "exhibitions"))
        self.CatagoryComboBox.setItemText(7, _translate("HostEventEdit", "entertaining"))
        self.CatagoryComboBox.setItemText(8, _translate("HostEventEdit", "charity"))
        self.CatagoryComboBox.setItemText(9, _translate("HostEventEdit", "business"))
        self.CatagoryComboBox.setItemText(10, _translate("HostEventEdit", "anything"))
        self.UserName_8.setText(_translate("HostEventEdit", "Day(s)"))
        self.DescriptionInput.setWhatsThis(_translate("HostEventEdit", "ddd"))

