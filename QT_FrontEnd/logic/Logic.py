import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from QT_FrontEnd.maindialog import *
from QT_FrontEnd.mainwindow import *
from QT_FrontEnd.registerdialog import *
from QT_FrontEnd.logic.SignInHandler import *
from QT_FrontEnd.googletokendisplay import *
from QT_FrontEnd.logic.Connection import *


class SignInWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SignInWindow, self).__init__(parent)
        self.setupUi(self)

        self.SignInButton.clicked.connect(self.sign_in_button_clicked)
        self.QuitButton.clicked.connect(self.quit_button_clicked)

    def sign_in_button_clicked(self):
        initiate_login()
        token_window.show()
        self.hide()

    def quit_button_clicked(self):
        self.close()


class SignUpWindow(QMainWindow, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(SignUpWindow, self).__init__(parent)
        self.setupUi(self)

        self.SaveProfileButton.clicked.connect(self.save_profile_button_clicked)

    def save_profile_button_clicked(self):
        nickname = self.NickNameInput.text()
        send_request(nickname)
        sign_in_window.show()
        self.hide()


class LobbyWindow(QMainWindow, Ui_MainDialog):
    def __init__(self, parent=None):
        super(LobbyWindow, self).__init__(parent)
        self.setupUi(self)


class TokenWindow(QMainWindow, Ui_GoogleTokenDisplay):
    def __init__(self, parent=None):
        super(TokenWindow, self).__init__(parent)
        self.setupUi(self)

        self.LoginButton.clicked.connect(self.login_button_clicked)

    def login_button_clicked(self):
        token = self.TokenInput.text()
        credential = verify_login(token)

        if credential == 'login error':
            show_dialog("Unable to connect to Google account, check your token. ")
            self.show()
        else:
            result = verify_registration(credential)
            if result[0] == 'MISSING':
                sign_up_window.show()
                self.hide()
            elif result[0] == 'OK':
                lobby_window.show()
                self.hide()
            else:
                show_dialog("Unable to connect to server, check your connections. ")
                self.show()



def show_dialog(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok)

    msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_in_window = SignInWindow()
    sign_up_window = SignUpWindow()
    lobby_window = LobbyWindow()
    token_window = TokenWindow()
    sign_in_window.show()
    sys.exit(app.exec_())
