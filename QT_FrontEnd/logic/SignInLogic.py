import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from QT_FrontEnd.maindialog import *
from QT_FrontEnd.mainwindow import *
from QT_FrontEnd.registerdialog import *
from QT_FrontEnd.logic.SignInHandler import *


class SignInWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SignInWindow, self).__init__(parent)
        self.setupUi(self)

        self.SignInButton.clicked.connect(self.sign_in_button_clicked)
        self.QuitButton.clicked.connect(self.quit_button_clicked)

    def sign_up_button_clicked(self):
        sign_up_window.show()
        self.hide()

    def sign_in_button_clicked(self):
        initiate_login()
        self.hide()

    def quit_button_clicked(self):
        self.close()


class SignUpWindow(QMainWindow, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(SignUpWindow, self).__init__(parent)
        self.setupUi(self)
        self.SaveProfileButton.clicked.connect(self.save_profile_button_clicked)

    def save_profile_button_clicked(self):
        sign_in_window.show()
        self.hide()


class LobbyWindow(QMainWindow, Ui_MainDialog):
    def __init__(self, parent=None):
        super(LobbyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_in_window = SignInWindow()
    sign_up_window = SignUpWindow()
    lobby_window = LobbyWindow()
    sign_in_window.show()
    sys.exit(app.exec_())
