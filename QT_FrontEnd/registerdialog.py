# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerdialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisterDialog(object):
    def setupUi(self, RegisterDialog):
        RegisterDialog.setObjectName("RegisterDialog")
        RegisterDialog.resize(745, 453)
        RegisterDialog.setStyleSheet("border-image: url(./bg.png)")
        self.label_4 = QtWidgets.QLabel(RegisterDialog)
        self.label_4.setGeometry(QtCore.QRect(290, 192, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border-image: \\*url();")
        self.label_4.setObjectName("label_4")
        self.EmailAddInput = QtWidgets.QLineEdit(RegisterDialog)
        self.EmailAddInput.setGeometry(QtCore.QRect(400, 221, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EmailAddInput.setFont(font)
        self.EmailAddInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.EmailAddInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.EmailAddInput.setClearButtonEnabled(False)
        self.EmailAddInput.setObjectName("EmailAddInput")
        self.AddressInput = QtWidgets.QLineEdit(RegisterDialog)
        self.AddressInput.setGeometry(QtCore.QRect(361, 192, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AddressInput.setFont(font)
        self.AddressInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.AddressInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.AddressInput.setText("")
        self.AddressInput.setClearButtonEnabled(False)
        self.AddressInput.setObjectName("AddressInput")
        self.label_2 = QtWidgets.QLabel(RegisterDialog)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Yuanti SC")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: \\*url();")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(RegisterDialog)
        self.label_3.setGeometry(QtCore.QRect(290, 164, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-image: \\*url();")
        self.label_3.setObjectName("label_3")
        self.NickNameInput = QtWidgets.QLineEdit(RegisterDialog)
        self.NickNameInput.setGeometry(QtCore.QRect(462, 134, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NickNameInput.setFont(font)
        self.NickNameInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.NickNameInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.NickNameInput.setText("")
        self.NickNameInput.setClearButtonEnabled(False)
        self.NickNameInput.setObjectName("NickNameInput")
        self.label_5 = QtWidgets.QLabel(RegisterDialog)
        self.label_5.setGeometry(QtCore.QRect(290, 104, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-image: \\*url();")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(RegisterDialog)
        self.label_6.setGeometry(QtCore.QRect(290, 134, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-image: \\*url();")
        self.label_6.setObjectName("label_6")
        self.LastNameInput = QtWidgets.QLineEdit(RegisterDialog)
        self.LastNameInput.setGeometry(QtCore.QRect(580, 104, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LastNameInput.setFont(font)
        self.LastNameInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.LastNameInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.LastNameInput.setText("")
        self.LastNameInput.setClearButtonEnabled(False)
        self.LastNameInput.setObjectName("LastNameInput")
        self.label_7 = QtWidgets.QLabel(RegisterDialog)
        self.label_7.setGeometry(QtCore.QRect(494, 107, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border-image: \\*url();")
        self.label_7.setObjectName("label_7")
        self.GenderComboBox = QtWidgets.QComboBox(RegisterDialog)
        self.GenderComboBox.setGeometry(QtCore.QRect(350, 162, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.GenderComboBox.setFont(font)
        self.GenderComboBox.setStyleSheet("border-image: \\*url();")
        self.GenderComboBox.setEditable(False)
        self.GenderComboBox.setObjectName("GenderComboBox")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.label_8 = QtWidgets.QLabel(RegisterDialog)
        self.label_8.setGeometry(QtCore.QRect(290, 220, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border-image: \\*url();")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(RegisterDialog)
        self.label_9.setGeometry(QtCore.QRect(514, 220, 16, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-image: \\*url();")
        self.label_9.setObjectName("label_9")
        self.EmailSuffixComboBox = QtWidgets.QComboBox(RegisterDialog)
        self.EmailSuffixComboBox.setGeometry(QtCore.QRect(530, 220, 151, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EmailSuffixComboBox.setFont(font)
        self.EmailSuffixComboBox.setStyleSheet("border-image: \\*url();")
        self.EmailSuffixComboBox.setEditable(False)
        self.EmailSuffixComboBox.setObjectName("EmailSuffixComboBox")
        self.EmailSuffixComboBox.addItem("")
        self.EmailSuffixComboBox.addItem("")
        self.EmailSuffixComboBox.addItem("")
        self.EmailSuffixComboBox.addItem("")
        self.EmailSuffixComboBox.addItem("")
        self.EmailSuffixComboBox.addItem("")
        self.EmailSuffixComboBox.addItem("")
        self.label_10 = QtWidgets.QLabel(RegisterDialog)
        self.label_10.setGeometry(QtCore.QRect(290, 246, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border-image: \\*url();")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(RegisterDialog)
        self.label_11.setGeometry(QtCore.QRect(470, 245, 16, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border-image: \\*url();")
        self.label_11.setObjectName("label_11")
        self.EmailOthersInput = QtWidgets.QLineEdit(RegisterDialog)
        self.EmailOthersInput.setGeometry(QtCore.QRect(490, 246, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.EmailOthersInput.setFont(font)
        self.EmailOthersInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.EmailOthersInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.EmailOthersInput.setClearButtonEnabled(False)
        self.EmailOthersInput.setObjectName("EmailOthersInput")
        self.label_12 = QtWidgets.QLabel(RegisterDialog)
        self.label_12.setGeometry(QtCore.QRect(290, 272, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-image: \\*url();")
        self.label_12.setObjectName("label_12")
        self.TagsComboBox = QtWidgets.QComboBox(RegisterDialog)
        self.TagsComboBox.setGeometry(QtCore.QRect(350, 271, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.TagsComboBox.setFont(font)
        self.TagsComboBox.setStyleSheet("border-image: \\*url();")
        self.TagsComboBox.setEditable(False)
        self.TagsComboBox.setObjectName("TagsComboBox")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.TagsComboBox.addItem("")
        self.label_13 = QtWidgets.QLabel(RegisterDialog)
        self.label_13.setGeometry(QtCore.QRect(290, 299, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border-image: \\*url();")
        self.label_13.setObjectName("label_13")
        self.DescriptionInput = QtWidgets.QLineEdit(RegisterDialog)
        self.DescriptionInput.setGeometry(QtCore.QRect(380, 304, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DescriptionInput.setFont(font)
        self.DescriptionInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.DescriptionInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.DescriptionInput.setText("")
        self.DescriptionInput.setClearButtonEnabled(False)
        self.DescriptionInput.setObjectName("DescriptionInput")
        self.graphicsView = QtWidgets.QGraphicsView(RegisterDialog)
        self.graphicsView.setGeometry(QtCore.QRect(290, 44, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.graphicsView.setFont(font)
        self.graphicsView.setStyleSheet("\n"
"border-radius: 25px;")
        self.graphicsView.setObjectName("graphicsView")
        self.UploadImageButton = QtWidgets.QPushButton(RegisterDialog)
        self.UploadImageButton.setGeometry(QtCore.QRect(350, 54, 131, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.UploadImageButton.setFont(font)
        self.UploadImageButton.setStyleSheet("border-image: \\*url();")
        self.UploadImageButton.setObjectName("UploadImageButton")
        self.SaveProfileButton = QtWidgets.QPushButton(RegisterDialog)
        self.SaveProfileButton.setGeometry(QtCore.QRect(100, 210, 80, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SaveProfileButton.setFont(font)
        self.SaveProfileButton.setStyleSheet("border-image: \\*url();")
        self.SaveProfileButton.setObjectName("SaveProfileButton")
        self.FirstNameInput = QtWidgets.QLineEdit(RegisterDialog)
        self.FirstNameInput.setGeometry(QtCore.QRect(380, 104, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.FirstNameInput.setFont(font)
        self.FirstNameInput.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.FirstNameInput.setStyleSheet("border-image: \\*url();\n"
"border-radius: 5px;\n"
"")
        self.FirstNameInput.setText("")
        self.FirstNameInput.setClearButtonEnabled(False)
        self.FirstNameInput.setObjectName("FirstNameInput")

        self.retranslateUi(RegisterDialog)
        QtCore.QMetaObject.connectSlotsByName(RegisterDialog)

    def retranslateUi(self, RegisterDialog):
        _translate = QtCore.QCoreApplication.translate
        RegisterDialog.setWindowTitle(_translate("RegisterDialog", "Dialog"))
        self.label_4.setText(_translate("RegisterDialog", "Address"))
        self.label_2.setText(_translate("RegisterDialog", "JoinMe"))
        self.label_3.setText(_translate("RegisterDialog", "Gender"))
        self.label_5.setText(_translate("RegisterDialog", "First Name"))
        self.label_6.setText(_translate("RegisterDialog", "Nickname (Account ID)"))
        self.label_7.setText(_translate("RegisterDialog", "Last Name"))
        self.GenderComboBox.setItemText(0, _translate("RegisterDialog", "Please Select"))
        self.GenderComboBox.setItemText(1, _translate("RegisterDialog", "Male"))
        self.GenderComboBox.setItemText(2, _translate("RegisterDialog", "Female"))
        self.GenderComboBox.setItemText(3, _translate("RegisterDialog", "Others"))
        self.label_8.setText(_translate("RegisterDialog", "Email Address"))
        self.label_9.setText(_translate("RegisterDialog", "@"))
        self.EmailSuffixComboBox.setItemText(0, _translate("RegisterDialog", "Please Select"))
        self.EmailSuffixComboBox.setItemText(1, _translate("RegisterDialog", "gmail.com"))
        self.EmailSuffixComboBox.setItemText(2, _translate("RegisterDialog", "outlook.com"))
        self.EmailSuffixComboBox.setItemText(3, _translate("RegisterDialog", "yahoo.com"))
        self.EmailSuffixComboBox.setItemText(4, _translate("RegisterDialog", "163.com"))
        self.EmailSuffixComboBox.setItemText(5, _translate("RegisterDialog", "qq.com"))
        self.EmailSuffixComboBox.setItemText(6, _translate("RegisterDialog", "others"))
        self.label_10.setText(_translate("RegisterDialog", "If others please specify"))
        self.label_11.setText(_translate("RegisterDialog", "@"))
        self.label_12.setText(_translate("RegisterDialog", "Tags "))
        self.TagsComboBox.setItemText(0, _translate("RegisterDialog", "Please Select"))
        self.TagsComboBox.setItemText(1, _translate("RegisterDialog", "Sports"))
        self.TagsComboBox.setItemText(2, _translate("RegisterDialog", "Social"))
        self.TagsComboBox.setItemText(3, _translate("RegisterDialog", "Outdoors"))
        self.TagsComboBox.setItemText(4, _translate("RegisterDialog", "Indoors"))
        self.TagsComboBox.setItemText(5, _translate("RegisterDialog", "Sightseeing"))
        self.TagsComboBox.setItemText(6, _translate("RegisterDialog", "Exhibitions"))
        self.TagsComboBox.setItemText(7, _translate("RegisterDialog", "Entertaining"))
        self.TagsComboBox.setItemText(8, _translate("RegisterDialog", "Charity"))
        self.TagsComboBox.setItemText(9, _translate("RegisterDialog", "Business"))
        self.TagsComboBox.setItemText(10, _translate("RegisterDialog", "Anything"))
        self.label_13.setText(_translate("RegisterDialog", "Description"))
        self.UploadImageButton.setText(_translate("RegisterDialog", "Upload Image"))
        self.SaveProfileButton.setText(_translate("RegisterDialog", "Save"))

