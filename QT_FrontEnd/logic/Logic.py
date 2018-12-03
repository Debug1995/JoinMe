import sys
import urllib.request
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
from QT_FrontEnd.maindialog import *
from QT_FrontEnd.mainwindow import *
from QT_FrontEnd.googletokendisplay import *
from QT_FrontEnd.hosteventdisplaydialog import *
from QT_FrontEnd.hosteventedit import *
from QT_FrontEnd.eventdisplaydialog import *
from QT_FrontEnd.registerdialog import *
from QT_FrontEnd.userprofiledisplay import *
from Model.EventModel import *
from Controller.UserController import *
from Login.GmapController import *
from Login.GoogleDrive import *

TODAY = datetime.datetime.today().strftime('%Y-%m-%d')

current_user: UserModel = UserModel('0', '', '', '', '', '', 'anything', '', [], [], '', '')
current_event: EventModel = EventModel('0', '', '', '', '', '', [], TODAY,
                                       '', '', '')
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
        address = self.AddressInput.text()
        state = get_state(address)

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
        elif state == 'FAILURE':
            show_dialog('Please enter a valid address. ')
        else:
            current_user.name = self.FirstNameInput.text() + ' ' + self.LastNameInput.text()
            current_user.nickname = self.NickNameInput.text()
            current_user.gender = str(self.GenderComboBox.currentText())
            current_user.email = self.EmailAddInput.text() + '@' + email_suffix
            current_user.location = state
            current_user.tags = string_to_enum(str(self.TagsComboBox.currentText()))
            current_user.description = self.DescriptionInput.toPlainText()
            response = add_user(current_user)
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
        self.HostAttendSeeMoreButton.clicked.connect(self.refresh_attend)
        self.HostEventSeeMoreButton.clicked.connect(self.refresh_host)
        self.SearchButton.clicked.connect(self.search_button_clicked)
        self.ScrollAreaDate1.clicked.connect(self.scroll_clicked)

    def scroll_clicked(self):
        if self.ScrollAreaDate1.text() != 'Date':
            populate_attend_window(self.ScrollAreaDate1.text())
            attend_event_display_window.show()
            self.hide()

    def search_button_clicked(self):
        get_default_list(current_user.uid)

    def post_event_clicked(self):
        post_event_window.show()
        self.hide()

    def attend_event_clicked(self):
        if self.AttendEvent1.text() != 'AttendEvent1':
            populate_attend_window(self.AttendEvent1.text())
            attend_event_display_window.show()
            self.hide()

    def host_event_clicked(self):
        if self.HostEvent1.text() != 'HostEvent1':
            update_event_display(self.HostEvent1.text())
            host_event_display_window.show()
            self.hide()

    def update_profile_clicked(self):
        profile_edit_window.show()
        self.hide()

    def refresh_attend(self):
        global current_user
        current_user = get_user(current_user.uid)
        print(current_user.join_events)
        if len(current_user.join_events) > 0:
            self.AttendEvent1.setText(current_user.join_events[0])
        if len(current_user.join_events) > 1:
            self.AttendEvent2.setText(current_user.join_events[1])
        if len(current_user.join_events) > 2:
            self.AttendEvent3.setText(current_user.join_events[2])

    def refresh_host(self):
        global current_user
        current_user = get_user(current_user.uid)
        print(current_user.host_events)
        if len(current_user.host_events) > 0:
            self.HostEvent1.setText(current_user.host_events[0])
        if len(current_user.host_events) > 1:
            self.HostEvent2.setText(current_user.host_events[1])
        if len(current_user.host_events) > 2:
            self.HostEvent3.setText(current_user.host_events[2])


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
                current_user = response_to_user(result[1])
                update_lobby_user()
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
        profile_view_attend_window.show()
        self.hide()

    def attend_button_clicked(self):
        result = attend(current_user.uid, current_event.eid)
        if result[0] == 'DUPLICATE':
            show_dialog('You already attended this event. ')
        if result[0] == 'OK':
            show_dialog('Congrats, you are in! ')
        if result[0] == 'FAILURE':
            show_dialog('Failed to add you to the event, try again later. ')

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
        self.UploadImage1.clicked.connect(self.upload_image_button_clicked)
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

    def upload_image_button_clicked(self):
        global current_event
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
            file_title = current_user.google_id + '_event.jpg'
            drive_service = set_up_drive(google_credentials)
            link = upload_image(drive_service, file_path, file_title)
            current_event.image = link
            pixmap = load_image(link)
            self.EventImage1.setPixmap(pixmap.scaled(self.EventImage1.width(), self.EventImage1.height()))

    def save_button_clicked(self):
        address = self.AddressInput.text()
        state = get_state(address)
        address = get_coordinate(address)
        year = self.YearComboBox.currentText()
        month = self.MonthComboBox.currentText()
        day = self.DayComboBox.currentText()
        start_date = year + '-' + month + '-' + day
        if year == 'Year' or month == 'Month' or day == 'Day':
            show_dialog('Please enter a specific start date. ')
        elif not valid_check_date(start_date):
            show_dialog('Please enter a valid start date. ')
        elif self.TitleInput.text() == '':
            show_dialog('Please enter a title. ')
        elif self.AddressInput.text() == '':
            show_dialog('Please enter a location of the event. ')
        elif not valid_period(self.PeriodTimeInput.text()):
            show_dialog('Please enter a valid event duration. ')
        elif state == 'FAILURE':
            show_dialog('Please enter a valid address. ')
        else:
            end_date = calculate_date(start_date, self.PeriodTimeInput.text())
            if datetime.datetime.strptime(end_date, "%Y-%m-%d") <= datetime.datetime.strptime(TODAY, "%Y-%m-%d"):
                show_dialog('Please make sure that the event ends after today. ')

            else:
                global current_event
                previous_event = current_event
                current_event.title = self.TitleInput.text()
                current_event.tags = string_to_enum(self.CatagoryComboBox.currentText())
                current_event.description = self.DescriptionInput.toPlainText()
                current_event.hosts = current_user.uid
                current_event.event_date = start_date
                current_event.location = state
                current_event.register_period = self.PeriodTimeInput.text()
                current_event.expire_date = end_date
                print_event(current_event)
                data = {
                    'id': current_event.eid,
                    'title': current_event.title,
                    'tags': current_event.tags,
                    'description': current_event.description,
                    'hosts': current_event.hosts,
                    'event_date': current_event.event_date,
                    'state': current_event.location,
                    'address': address,
                    'image': current_event.image,
                    'register_period': current_event.register_period,
                    'expire_date': current_event.expire_date
                }
                response = edit_event(data)
                if response[0] == 'SUCCESS':
                    update_event_display(current_event.eid)
                    host_event_display_window.show()
                    self.hide()
                else:
                    current_event = previous_event
                    show_dialog('Unable to update, please try again later. ')


class PostEventWindow(QMainWindow, Ui_HostEventEdit):
    def __init__(self, parent=None):
        super(PostEventWindow, self).__init__(parent)
        self.setupUi(self)
        self.SaveEventButton.clicked.connect(self.save_button_clicked)
        self.UploadImage1.clicked.connect(self.upload_image_button_clicked)

    def upload_image_button_clicked(self):
        global current_event
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
            file_title = current_user.google_id + '_event.jpg'
            drive_service = set_up_drive(google_credentials)
            link = upload_image(drive_service, file_path, file_title)
            current_event.image = link
            pixmap = load_image(link)
            self.EventImage1.setPixmap(pixmap.scaled(self.EventImage1.width(), self.EventImage1.height()))

    def save_button_clicked(self):
        global current_event
        address = self.AddressInput.text()
        state = get_state(address)
        address = get_coordinate(address)
        year = self.YearComboBox.currentText()
        month = self.MonthComboBox.currentText()
        day = self.DayComboBox.currentText()
        start_date = year + '-' + month + '-' + day
        if year == 'Year' or month == 'Month' or day == 'Day':
            show_dialog('Please enter a specific start date. ')
        elif not valid_check_date(start_date):
            show_dialog('Please enter a valid start date. ')
        elif self.TitleInput.text() == '':
            show_dialog('Please enter a title. ')
        elif self.AddressInput.text() == '':
            show_dialog('Please enter a location of the event. ')
        elif not valid_period(self.PeriodTimeInput.text()):
            show_dialog('Please enter a valid event duration. ')
        elif state == 'FAILURE':
            show_dialog('Please enter a valid address. ')
        else:
            end_date = calculate_date(start_date, self.PeriodTimeInput.text())
            if datetime.datetime.strptime(end_date, "%Y-%m-%d") <= datetime.datetime.strptime(TODAY, "%Y-%m-%d"):
                show_dialog('Please make sure that the event ends after today. ')

            else:
                current_event.title = self.TitleInput.text()
                current_event.tags = string_to_enum(self.CatagoryComboBox.currentText())
                current_event.description = self.DescriptionInput.toPlainText()
                current_event.hosts = current_user.uid
                current_event.event_date = start_date
                current_event.location = state
                current_event.register_period = self.PeriodTimeInput.text()
                current_event.expire_date = end_date
                print_event(current_event)
                data = {
                    'title': current_event.title,
                    'tags': current_event.tags,
                    'description': current_event.description,
                    'hosts': current_event.hosts,
                    'event_date': current_event.event_date,
                    'state': current_event.location,
                    'address': address,
                    'image': current_event.image,
                    'register_period': current_event.register_period,
                    'expire_date': current_event.expire_date
                }
                response = post_event(data)
                current_event.eid = response[1]['eid']
                current_event = get_event(current_event.eid)
                update_event_display(current_event.eid)
                host_event_display_window.show()
                self.hide()


class ProfileEditWindow(QMainWindow, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(ProfileEditWindow, self).__init__(parent)
        self.setupUi(self)

        self.UploadImageButton.clicked.connect(self.upload_image_button_clicked)
        self.SaveProfileButton.clicked.connect(self.save_button_clicked)

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

    def save_button_clicked(self):
        global current_user
        email_suffix = str(self.EmailSuffixComboBox.currentText())
        if email_suffix == 'others':
            email_suffix = self.EmailOthersInput.text()
        address = self.AddressInput.text()
        state = get_state(address)

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
        elif state == 'FAILURE':
            show_dialog('Please enter a valid address. ')
        else:
            previous_user = current_user
            current_user.name = self.FirstNameInput.text() + ' ' + self.LastNameInput.text()
            current_user.nickname = self.NickNameInput.text()
            current_user.gender = str(self.GenderComboBox.currentText())
            current_user.email = self.EmailAddInput.text() + '@' + email_suffix
            current_user.location = state
            current_user.tags = string_to_enum(str(self.TagsComboBox.currentText()))
            current_user.description = self.DescriptionInput.toPlainText()
            response = edit_user(current_user)
            if response[0] == 'MISSING':
                show_dialog('User with this credential does not exist. ')
                current_user = previous_user
            elif response[0] == 'FAILURE':
                show_dialog("Unable to connect to server, please check your connections. ")
                current_user = previous_user
            else:
                current_user.uid = response[1]['id']
                print_user(current_user)
                update_lobby_user()
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
    return tags_input


def load_image(url):
    if url == '':
        return
    else:
        loaded = False
        try:
            request = urllib.request.Request(url, headers={'User-Agent':
                                                               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                                                               'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                               'Chrome/50.0.2661.102 Safari/537.36'})
            data = urllib.request.urlopen(request).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            loaded = True
            return pixmap
        finally:
            if not loaded:
                return 'FAILURE'


def response_to_user(response):
    user = UserModel('0', '', '', '', '', '', 'anything', '', [], [], '', '')
    user.uid = response['id']
    user.name = response['name']
    user.nickname = response['nickname']
    user.email = response['email']
    user.location = response['location']
    user.description = response['description']
    user.gender = response['gender']
    user.image = response['image']
    user.tags = response['tags']
    user.google_id = response['google_id']
    user.join_events = ast.literal_eval(str(response['join']))
    user.host_events = ast.literal_eval(str(response['host']))
    return user


def response_to_event(response):
    event = EventModel('0', '', '', '', '', '', [], TODAY, '', '', '')
    event.title = response['title']
    event.eid = response['id']
    event.description = response['description']
    event.address = response['address']
    event.location = response['location']
    event.image = response['image']
    event.tags = response['tags']
    event.event_date = response['event_date']
    event.expire_date = response['expire_date']
    event.hosts = response['host']
    event.attendees = ast.literal_eval(str(response['join']))
    return event


def print_user(user: UserModel):
    if not user:
        print('This user is empty. ')
        print()
        return
    print('user id: ' + str(user.uid))
    print('real name: ' + user.name)
    print('nickname: ' + user.nickname)
    print('gender: ' + user.gender)
    print('location: ' + user.location)
    print('email: ' + user.email)
    print('tags: ' + str(user.tags))
    print('description: ' + user.description)
    print('hosted: ' + str(user.host_events))
    print('joined: ' + str(user.join_events))
    print('image: ' + str(user.image))
    print('google id: ' + str(user.google_id))
    print()
    return


def print_event(event: EventModel):
    if not event:
        print('This event is empty. \n')
    if type(event) == str:
        print(event)
        print()
    else:
        print('eid: ' + str(event.eid))
        print('title: ' + event.title)
        print('tags: ' + event.tags)
        print('description: ' + event.description)
        print('image: ' + event.image)
        print('hosts: ' + str(event.hosts))
        print('attendees: ' + str(event.attendees))
        print('event date: ' + event.event_date)
        print('state: ' + event.location)
        print('address: ' + event.address)
        print('expire date: ' + event.expire_date)
        print()


def update_lobby_user():
    if current_user.image == '':
        return
    pixmap = load_image(current_user.image)
    if pixmap != 'FAILURE':
        lobby_window.UserImage.setPixmap(pixmap.scaled(lobby_window.UserImage.width(),
                                                       lobby_window.UserImage.height()))

    lobby_window.NickName.setText(current_user.nickname)


def valid_check_date(date):
    date = date.strip()
    if len(date) != 10 or date[4] != '-' or date[7] != '-' or not date or len(date) == 0:
        return False
    check_string = date[:4] + date[5:7] + date[8:]
    for char in check_string:
        if not char.isdigit():
            return False
    try:
        time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False


def valid_period(period):
    period = str(period).strip()
    if not period or len(period) == 0:
        return False
    for char in period:
        if not char.isdigit():
            return False
    return True


def calculate_date(initial_date, register_period):
    cur_date = [int(x) for x in initial_date.strip().split('-')]
    d1 = datetime.date(cur_date[0], cur_date[1], cur_date[2])
    d = d1 + datetime.timedelta(days=int(register_period))
    year = str(d.year)
    month = str(d.month).zfill(2)
    date = str(d.day-1).zfill(2)
    return year + '-' + month + '-' + date


def update_event_display(eid):
    event = get_event(eid)
    user = get_user(event.hosts)
    host_event_display_window.AddressOutput.setText(event.address)
    host_event_display_window.CityOutput.setText(event.location)
    host_event_display_window.DateOutput.setText(event.expire_date)
    host_event_display_window.DescriptionOutput.setText(event.description)
    host_event_display_window.UserName.setText(event.title)
    host_event_display_window.HostIDOutput.setText(user.nickname)


def populate_attend_window(eid):
    event = get_event(eid)
    global current_event
    current_event = event
    user = get_user(event.hosts)
    attend_event_display_window.HostIDOutput.setText(user.nickname)
    attend_event_display_window.AddressOutput.setText(event.address)
    attend_event_display_window.CityOutput.setText(event.location)
    attend_event_display_window.DateOutput.setText(event.expire_date)
    attend_event_display_window.DescriptionOutput.setText(event.description)
    attend_event_display_window.UserNameOutput.setText(event.title)


def get_user(uid):
    res = request_user(int(uid))
    print(res[1])
    user = response_to_user(res[1])
    return user


def get_event(eid):
    res = request_event(int(eid))
    print(res[1])
    event = response_to_event(res[1])
    print_event(event)
    return event


def get_default_list(uid):
    user = get_user(uid)
    state = user.location
    default_list = get_default(state)
    default_list = default_list[1]
    default_list = ast.literal_eval(str(default_list))
    print(default_list)
    print(len(default_list))

    if len(default_list) > 0:
        result = default_list[0]
        print(result)
        lobby_window.ScrollAreaDate1.setText(str(result[0]))
        lobby_window.ScrollAreaEvent1.setText(result[1])
        lobby_window.ScrollAreaAddress1.setText(result[2])


def attend(uid, eid):
    result = attend_event(uid, eid)
    print(result)
    return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sign_in_window = SignInWindow()
    sign_up_window = SignUpWindow()
    lobby_window = LobbyWindow()
    token_window = TokenWindow()
    host_event_display_window = HostEventDisplayWindow()
    host_event_edit_window = HostEventEditWindow()
    post_event_window = PostEventWindow()
    attend_event_display_window = AttendEventDisplayWindow()
    profile_edit_window = ProfileEditWindow()
    profile_view_attend_window = ProfileViewWindow()
    profile_view_host_window = ProfileViewWindow()
    sign_in_window.show()
    sys.exit(app.exec_())
