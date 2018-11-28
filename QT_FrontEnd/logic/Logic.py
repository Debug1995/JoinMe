import sys
import urllib.request
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from QT_FrontEnd.maindialog import *
from QT_FrontEnd.mainwindow import *
from QT_FrontEnd.logic.SignInHandler import *
from QT_FrontEnd.googletokendisplay import *
from QT_FrontEnd.hosteventdisplaydialog import *
from QT_FrontEnd.hosteventedit import *
from QT_FrontEnd.eventdisplaydialog import *
from QT_FrontEnd.registerdialog import *
from QT_FrontEnd.userprofiledisplay import *
from Model.UserModel import *
from Controller.UserController import *
from Login.GmailController import *
from Login.GoogleDrive import *

user_priority = 1
current_user: UserModel = UserModel('0', '', '', '', '', '', Tags.anything, '',
                                    [], [], '', '')
google_credentials = None


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
        self.UploadImageButton.clicked.connect(self.upload_image_button_clicked)

    def upload_image_button_clicked(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        try:
            file_name = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileNames()", "",
                                                    "Images (*.png *jpg *.jpeg)", options=options)
        finally:
            self.show()
        if file_name[0] != '':
            global current_user
            file_path = file_name[0]
            file_title = current_user.google_id + '_profile.jpg'
            drive_service = set_up_drive(google_credentials)
            link = upload_image(drive_service, file_path, file_title)
            current_user.image = link
            pixmap = load_image(link)
            self.profile_picture.setPixmap(pixmap.scaled(self.profile_picture.width(), self.profile_picture.height()))

    def save_profile_button_clicked(self):
        global current_user
        email_suffix = str(self.EmailSuffixComboBox.currentText())
        if email_suffix == 'others':
            email_suffix = self.EmailOthersInput.text()

        if self.FirstNameInput.text() == '' or self.LastNameInput.text() == '':
            show_dialog('Please specify your name. ')
        elif self.NickNameInput.text() == '':
            show_dialog('Please enter a nickname. ')
        elif str(self.GenderComboBox.currentText()) == 'Please Select':
            show_dialog('Please specify your gender. ')
        elif self.AddressInput.text() == '':
            show_dialog('Please enter your address. ')
        elif self.EmailAddInput.text() == '':
            show_dialog('Please enter your email address. ')
        elif email_suffix == '' or email_suffix == 'Please Select':
            show_dialog('Please enter your email address. ')
        else:
            current_user.name = self.FirstNameInput.text() + ' ' + self.LastNameInput.text()
            current_user.nickname = self.NickNameInput.text()
            current_user.gender = str(self.GenderComboBox.currentText())
            current_user.email = self.EmailAddInput.text() + '@' + email_suffix
            current_user.location = self.AddressInput.text()
            current_user.tags = string_to_enum(str(self.TagsComboBox.currentText()))
            current_user.description = self.DescriptionInput.toPlainText()
            response = send_user(current_user)
            if response[0] == 'DUPLICATE':
                show_dialog('User with the same credential already exists. ')
            elif response[0] == 'FAILURE':
                show_dialog("Unable to connect to server, please check your connections. ")
            else:
                current_user.uid = response[1]['id']
                print_user(current_user)
                sign_in_window.show()
                self.hide()


class LobbyWindow(QMainWindow, Ui_MainDialog):
    def __init__(self, parent=None):
        super(LobbyWindow, self).__init__(parent)
        self.setupUi(self)
        self.AttendEvent1.clicked.connect(self.attend_event_clicked)
        self.AttendEvent2.clicked.connect(self.attend_event_clicked)
        self.AttendEvent3.clicked.connect(self.attend_event_clicked)
        self.HostEvent1.clicked.connect(self.host_event_clicked)
        self.HostEvent2.clicked.connect(self.host_event_clicked)
        self.HostEvent3.clicked.connect(self.host_event_clicked)
        self.UpdateProfileButton.clicked.connect(self.update_profile_clicked)
        self.PostEventButton.clicked.connect(self.post_event_clicked)

    def post_event_clicked(self):
        host_event_edit_window.show()
        self.hide()

    def attend_event_clicked(self):
        attend_event_display_window.show()
        self.hide()

    def host_event_clicked(self):
        host_event_display_window.show()
        self.hide()

    def update_profile_clicked(self):
        profile_edit_window.show()
        self.hide()


class TokenWindow(QMainWindow, Ui_GoogleTokenDisplay):
    def __init__(self, parent=None):
        super(TokenWindow, self).__init__(parent)
        self.setupUi(self)

        self.LoginButton.clicked.connect(self.login_button_clicked)
        self.BackButton.clicked.connect(self.back_button_clicked)

    def login_button_clicked(self):
        global google_credentials
        token = self.TokenInput.text()
        google_credentials = verify_login(token)

        if google_credentials == 'login error':
            show_dialog("Unable to connect to Google account, check your token. ")
            google_credentials = None
            self.show()
        else:
            global current_user

            result = verify_registration(google_credentials)
            gmail = Gmail()
            google_id = gmail.get_user_email(google_credentials)
            current_user.google_id = google_id

            if result[0] == 'MISSING':
                sign_up_window.show()
                self.hide()
            elif result[0] == 'OK':
                lobby_window.show()
                self.hide()
            else:
                show_dialog("Unable to connect to server, check your connections. ")
                self.show()

    def back_button_clicked(self):
        sign_in_window.show()
        self.hide()


class AttendEventDisplayWindow(QMainWindow, Ui_EventDisplayDialog):
    def __init__(self, parent=None):

        super(AttendEventDisplayWindow, self).__init__(parent)
        self.setupUi(self)
        self.AttendEventButton.clicked.connect(self.attend_button_clicked)
        self.BackButton.clicked.connect(self.back_button_clicked)
        self.Attendee1.clicked.connect(self.view_profile_clicked)
        self.Attendee2.clicked.connect(self.view_profile_clicked)
        self.Attendee3.clicked.connect(self.view_profile_clicked)
        self.Attendee4.clicked.connect(self.view_profile_clicked)
        self.Attendee5.clicked.connect(self.view_profile_clicked)
        self.Attendee6.clicked.connect(self.view_profile_clicked)
        self.Attendee7.clicked.connect(self.view_profile_clicked)
        self.Attendee8.clicked.connect(self.view_profile_clicked)
        self.Attendee9.clicked.connect(self.view_profile_clicked)
        self.Attendee10.clicked.connect(self.view_profile_clicked)
        self.Hostimage.clicked.connect(self.view_profile_clicked)

    def view_profile_clicked(self):
        global user_priority
        user_priority = 0
        profile_view_attend_window.show()
        self.hide()

    def attend_button_clicked(self):
        lobby_window.show()
        self.hide()

    def back_button_clicked(self):
        lobby_window.show()
        self.hide()


class HostEventDisplayWindow(QMainWindow, Ui_HostEventDisplayDialog):

    def __init__(self, parent=None):

        super(HostEventDisplayWindow, self).__init__(parent)
        self.setupUi(self)
        self.EventEditButton.clicked.connect(self.edit_button_clicked)
        self.BackButton.clicked.connect(self.back_button_clicked)
        self.Attendee1.clicked.connect(self.view_profile_clicked)
        self.Attendee2.clicked.connect(self.view_profile_clicked)
        self.Attendee3.clicked.connect(self.view_profile_clicked)
        self.Attendee4.clicked.connect(self.view_profile_clicked)
        self.Attendee5.clicked.connect(self.view_profile_clicked)
        self.Attendee6.clicked.connect(self.view_profile_clicked)
        self.Attendee7.clicked.connect(self.view_profile_clicked)
        self.Attendee8.clicked.connect(self.view_profile_clicked)
        self.Attendee9.clicked.connect(self.view_profile_clicked)
        self.Attendee10.clicked.connect(self.view_profile_clicked)
        self.HostImage.clicked.connect(self.view_profile_clicked)

    def view_profile_clicked(self):
        global user_priority
        user_priority = 1
        profile_view_host_window.show()
        self.hide()

    def edit_button_clicked(self):
        host_event_edit_window.show()
        self.hide()

    def back_button_clicked(self):
        lobby_window.show()
        self.hide()


class HostEventEditWindow(QMainWindow, Ui_HostEventEdit):
    def __init__(self, parent=None):
        super(HostEventEditWindow, self).__init__(parent)
        self.setupUi(self)
        self.SaveEventButton.clicked.connect(self.save_button_clicked)
        self.Attendee1.clicked.connect(self.delete_clicked)
        self.Attendee2.clicked.connect(self.delete_clicked)
        self.Attendee3.clicked.connect(self.delete_clicked)
        self.Attendee4.clicked.connect(self.delete_clicked)
        self.Attendee5.clicked.connect(self.delete_clicked)
        self.Attendee6.clicked.connect(self.delete_clicked)
        self.Attendee7.clicked.connect(self.delete_clicked)
        self.Attendee8.clicked.connect(self.delete_clicked)
        self.Attendee9.clicked.connect(self.delete_clicked)
        self.Attendee10.clicked.connect(self.delete_clicked)

    def delete_clicked(self):
        pass

    def save_button_clicked(self):
        host_event_display_window.show()
        self.hide()


class ProfileEditWindow(QMainWindow, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(ProfileEditWindow, self).__init__(parent)
        self.setupUi(self)
        self.SaveProfileButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        lobby_window.show()
        self.hide()


class ProfileViewWindow(QMainWindow, Ui_UserProfileDisplay):
    def __init__(self, parent=None):
        super(ProfileViewWindow, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        global user_priority
        if user_priority == 0:
            attend_event_display_window.show()
            self.hide()
        else:
            host_event_display_window.show()
            self.hide()


def show_dialog(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def string_to_enum(tags_input):
    check_set = set(['sports', 'social', 'outdoors', 'indoors', 'sightseeing',
                     'exhibitions', 'entertaining', 'charity', 'business'])
    if tags_input not in check_set:
        tags_input = 'anything'
    return Tags[tags_input]


def load_image(url):
    data = urllib.request.urlopen(url).read()
    pixmap = QPixmap()
    pixmap.loadFromData(data)
    return pixmap


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_in_window = SignInWindow()
    sign_up_window = SignUpWindow()
    lobby_window = LobbyWindow()
    token_window = TokenWindow()
    host_event_display_window = HostEventDisplayWindow()
    host_event_edit_window = HostEventEditWindow()
    attend_event_display_window = AttendEventDisplayWindow()
    profile_edit_window = ProfileEditWindow()
    profile_view_attend_window = ProfileViewWindow()
    profile_view_host_window = ProfileViewWindow()
    sign_in_window.show()
    sys.exit(app.exec_())
