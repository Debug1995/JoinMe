import sys
import urllib.request
import random
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon, QImage
from PyQt5 import QtCore
from QT_FrontEnd.maindialog import Ui_MainDialog
from QT_FrontEnd.mainwindow import Ui_MainWindow
from QT_FrontEnd.googletokendisplay import Ui_GoogleTokenDisplay
from QT_FrontEnd.hosteventdisplaydialog import Ui_HostEventDisplayDialog
from QT_FrontEnd.hosteventedit import Ui_HostEventEdit
from QT_FrontEnd.eventdisplaydialog import Ui_EventDisplayDialog
from QT_FrontEnd.registerdialog import Ui_RegisterDialog
from QT_FrontEnd.userprofiledisplay import Ui_UserProfileDisplay
from Model.EventModel import EventModel
from Login.GmailController import *
from QT_FrontEnd.logic import SignInHandler
from QT_FrontEnd.logic import Connection
from Images.AWSConnector import AWSConnector
import webbrowser
from Login.GmapController import *
from Controller.UserController import *
import Controller.EventController as EventController


TODAY = datetime.today().strftime('%Y-%m-%d')

AWS_CONNECTOR = AWSConnector()

current_user: UserModel = UserModel('0', '', '', '', '', '', 'anything', '', [], [], 'DefaultUser.png', '')
current_event: EventModel = EventModel('0', '', '', '', '[None, None, None]', '', [], TODAY, '', '', '')
google_credentials = None


class SignInWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SignInWindow, self).__init__(parent)
        self.setupUi(self)

        self.SignInButton.clicked.connect(self.sign_in_button_clicked)
        self.QuitButton.clicked.connect(self.quit_button_clicked)

    def sign_in_button_clicked(self):
        SignInHandler.initiate_login()
        token_window.TokenInput.setText('')
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
            upload_result = upload_image(file_path, file_title)
            if upload_result:
                current_user.image = file_title
                pixmap = load_image(current_user.image)
                if pixmap != Errors.FAILURE.name:
                    self.profile_picture.setPixmap(pixmap.scaled(self.profile_picture.width(),
                                                                 self.profile_picture.height()))

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
            response = Connection.add_user(current_user)
            if response[0] == 'DUPLICATE':
                show_dialog('User with the same credential already exists. ')
            elif response[0] == 'FAILURE':
                show_dialog("Unable to connect to server, please check your connections. ")
            else:
                current_user.uid = response[1]['id']
                token_window.TokenInput.setText('')
                sign_in_window.show()
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
        google_credentials = SignInHandler.verify_login(token)

        if google_credentials == 'login error':
            show_dialog("Unable to connect to Google account, check your token. ")
            google_credentials = None
            self.show()
        else:
            global current_user
            result = SignInHandler.verify_registration(google_credentials)
            gmail = Gmail()
            google_id = gmail.get_user_email(google_credentials)
            current_user.google_id = google_id

            if result[0] == 'MISSING':
                sign_up_window.show()
                self.hide()
            elif result[0] == 'OK':
                current_user = response_to_user(result[1])
                update_lobby_user()
                lobby_window.event_list = get_default_list(current_user.uid)
                lobby_window.total_page = len(lobby_window.event_list)
                lobby_window.current_page = 1
                lobby_window.display_list()
                lobby_window.refresh_host()
                lobby_window.refresh_attend()
                lobby_window.show()
                self.hide()
            else:
                show_dialog("Unable to connect to server, check your connections. ")
                self.show()

    def back_button_clicked(self):
        sign_in_window.show()
        self.hide()


class LobbyWindow(QMainWindow, Ui_MainDialog):
    def __init__(self, parent=None):
        super(LobbyWindow, self).__init__(parent)
        self.setupUi(self)
        self.AttendEvent1.clicked.connect(lambda: self.attend_event_clicked(1))
        self.AttendEvent2.clicked.connect(lambda: self.attend_event_clicked(2))
        self.AttendEvent3.clicked.connect(lambda: self.attend_event_clicked(3))
        self.HostEvent1.clicked.connect(lambda: self.host_event_clicked(1))
        self.HostEvent2.clicked.connect(lambda: self.host_event_clicked(2))
        self.HostEvent3.clicked.connect(lambda: self.host_event_clicked(3))
        self.UpdateProfileButton.clicked.connect(self.update_profile_clicked)
        self.PostEventButton.clicked.connect(self.post_event_clicked)
        self.HostAttendSeeMoreButton.clicked.connect(self.see_more_attend_clicked)
        self.HostEventSeeMoreButton.clicked.connect(self.see_more_host_clicked)
        self.SearchButton.clicked.connect(self.search_button_clicked)
        self.LogOutButton.clicked.connect(self.log_out_button_clicked)
        self.LastPage.clicked.connect(self.last_clicked)
        self.NextPage.clicked.connect(self.next_clicked)
        self.event_list = []
        self.current_page = 1
        self.total_page = 1
        self.ScrollAreaEvent1.clicked.connect(lambda: self.scroll_clicked(0))
        self.ScrollAreaEvent2.clicked.connect(lambda: self.scroll_clicked(1))
        self.ScrollAreaEvent3.clicked.connect(lambda: self.scroll_clicked(2))
        self.ScrollAreaEvent4.clicked.connect(lambda: self.scroll_clicked(3))
        self.ScrollAreaEvent5.clicked.connect(lambda: self.scroll_clicked(4))

    def next_clicked(self):
        if self.current_page < self.total_page:
            self.current_page += 1
            self.display_list()

    def last_clicked(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.display_list()

    def clear_list(self):
        for item in self.ScrollAreaList:
            item['title'].setText('')
            item['date'].setText('')
            item['address'].setText('')
            item['image'].setVisible(False)
            item['id'] = 0

    def display_list(self):
        self.clear_list()
        current_list = self.event_list[self.current_page - 1]
        if len(current_list) == 0:
            self.ScrollAreaList[0]['title'].setText('No events match the filter. ')
        else:
            for i, event in enumerate(self.event_list[self.current_page - 1]):
                self.ScrollAreaList[i]['id'] = event[0]
                self.ScrollAreaList[i]['title'].setText(event[1])
                self.ScrollAreaList[i]['address'].setText(event[2])
                self.ScrollAreaList[i]['date'].setText(event[3].strftime('%Y%m%d'))
                event_image = eval(event[4])
                display_image = None
                for image in event_image:
                    if image:
                        display_image = image
                        break
                if not display_image:
                    image_profile = QImage('./DefaultImage.png')
                    self.ScrollAreaList[i]['image'].setPixmap(QPixmap.fromImage(image_profile).scaled(
                        self.ScrollAreaList[i]['image'].width(),
                        self.ScrollAreaList[i]['image'].height()))
                    self.ScrollAreaList[i]['image'].setVisible(True)
                else:
                    pixmap = load_image(display_image)
                    self.ScrollAreaList[i]['image'].setPixmap(pixmap.scaled(
                        self.ScrollAreaList[i]['image'].width(),
                        self.ScrollAreaList[i]['image'].height()))
                    self.ScrollAreaList[i]['image'].setVisible(True)

    def log_out_button_clicked(self):
        global current_user
        global current_event
        global google_credentials
        current_user = UserModel('0', '', '', '', '', '', 'anything', '', [], [], 'DefaultUser.png', '')
        current_event = EventModel('0', '', '', '', '[None, None, None]', '', [], TODAY, '', '', '')
        google_credentials = None
        self.event_list = []
        self.hide()
        sign_in_window.show()

    def scroll_clicked(self, i):
        if self.ScrollAreaList[i]['id'] != 0:
            populate_attend_window(self.ScrollAreaList[i]['id'])
            attend_event_display_window.show()
            self.hide()

    def search_button_clicked(self):
        tag = self.CatagoryComboBox.currentText()
        if tag == 'Category':
            tag = None
        state = self.PlaceComboBox.currentText()
        if state == 'Your Place':
            state = None
        time_margin = self.TimeComboBox.currentText()
        if time_margin == 'In One Day':
            time_margin = 1
        elif time_margin == 'In Three Days':
            time_margin = 3
        elif time_margin == 'In One Week':
            time_margin = 7
        elif time_margin == 'In One Month':
            time_margin = 30
        else:
            time_margin = None
        keyword = self.KeywordInput.text()
        if keyword == '':
            keyword = None

        event_filter = {
            'tag': tag,
            'state': state,
            'time': time_margin,
            'keyword': keyword
        }
        self.event_list = get_list(event_filter)
        self.total_page = len(self.event_list)
        self.current_page = 1
        self.display_list()

    def post_event_clicked(self):
        post_event_window.show()
        self.hide()

    def attend_event_clicked(self, i):
        if self.AttendEventList[i - 1].text() != '':
            populate_attend_window(self.AttendEventList[i - 1].text())
            attend_event_display_window.show()
            self.hide()

    def host_event_clicked(self, i):
        if self.HostEventList[i - 1].text() != '':
            update_event_display(self.HostEventList[i - 1].text())
            host_event_display_window.restore_attendees()
            host_event_display_window.update_attendees_image()
            host_event_display_window.update_host_image()
            host_event_display_window.show()
            self.hide()

    def update_profile_clicked(self):
        global current_user
        if current_user.uid != '0':
            _translate = QtCore.QCoreApplication.translate
            self.name = current_user.name.split(' ')
            profile_edit_window.FirstNameInput.setText(_translate("RegisterDialog", self.name[0]))
            profile_edit_window.LastNameInput.setText(_translate("RegisterDialog", self.name[1]))
            profile_edit_window.NickNameInput.setText(_translate("RegisterDialog", current_user.nickname))
            profile_edit_window.AddressInput.setText(_translate("RegisterDialog", current_user.location))
            profile_edit_window.GenderComboBox.setCurrentText(_translate("RegisterDialog", current_user.gender))
            self.email = current_user.email.split('@')
            profile_edit_window.EmailAddInput.setText(_translate("RegisterDialog", self.email[0]))
            if self.email[1] not in ['gmail.com', 'outlook.com', 'yahoo.com', '163.com', 'qq.com']:
                profile_edit_window.EmailOthersInput.setText(_translate("RegisterDialog", self.email[1]))
                profile_edit_window.EmailSuffixComboBox.setCurrentText(_translate("RegisterDialog", "others"))
            else:
                profile_edit_window.EmailSuffixComboBox.setCurrentText(_translate("RegisterDialog", self.email[1]))
            profile_edit_window.TagsComboBox.setCurrentText(_translate("RegisterDialog", current_user.tags))
            profile_edit_window.DescriptionInput.setText(_translate("RegisterDialog", current_user.description))
            pixmap = load_image(current_user.image)
            if pixmap != Errors.FAILURE.name:
                profile_edit_window.profile_picture.setPixmap(pixmap.
                                                              scaled(profile_edit_window.profile_picture.width(),
                                                                     profile_edit_window.profile_picture.height()))
        profile_edit_window.show()
        self.hide()

    def see_more_attend_clicked(self):
        self.refresh_attend()
        self.event_list = get_attend_event_list()
        self.total_page = len(self.event_list)
        self.current_page = 1
        self.display_list()

    def see_more_host_clicked(self):
        self.refresh_host()
        self.event_list = get_host_event_list()
        self.total_page = len(self.event_list)
        self.current_page = 1
        self.display_list()

    def refresh_attend(self):
        global current_user
        current_user = get_user(current_user.uid)
        for i, event in enumerate(current_user.join_events):
            if i > 2:
                break
            self.AttendEventList[i].setText(event)

    def refresh_host(self):
        global current_user
        current_user = get_user(current_user.uid)
        if len(current_user.host_events) > 0:
            self.HostEvent1.setText(current_user.host_events[0])
        if len(current_user.host_events) > 1:
            self.HostEvent2.setText(current_user.host_events[1])
        if len(current_user.host_events) > 2:
            self.HostEvent3.setText(current_user.host_events[2])


class AttendEventDisplayWindow(QMainWindow, Ui_EventDisplayDialog):
    def __init__(self, parent=None):
        super(AttendEventDisplayWindow, self).__init__(parent)
        self.setupUi(self)
        self.AttendEventButton.clicked.connect(self.attend_button_clicked)
        self.BackButton.clicked.connect(self.back_button_clicked)
        self.eye1.clicked.connect(self.view_profile_clicked)
        self.eye2.clicked.connect(self.view_profile_clicked)
        self.eye3.clicked.connect(self.view_profile_clicked)
        self.eye4.clicked.connect(self.view_profile_clicked)
        self.eye5.clicked.connect(self.view_profile_clicked)
        self.eye6.clicked.connect(self.view_profile_clicked)
        self.eye7.clicked.connect(self.view_profile_clicked)
        self.eye8.clicked.connect(self.view_profile_clicked)
        self.eye9.clicked.connect(self.view_profile_clicked)
        self.eye10.clicked.connect(self.view_profile_clicked)
        self.eyeHost.clicked.connect(self.view_profile_clicked)
        self.mapView.clicked.connect(self.map_view_clicked)
        self.SendEmailButton.clicked.connect(self.sendemail_button_clicked)

    def sendemail_button_clicked(self):
        sender = current_user.google_id
        subject = "A New Message from the attendee of " + current_event.title

        receiver = []

        hostID = EventController.get_host(current_event.eid)
        user = retrieve_user('userid', hostID)
        receiver.append(user.google_id)
        message = self.ToEmailInput.toPlainText()
        send_email(sender, receiver, subject, message)

    def map_view_clicked(self):
        self.mapView.setStyleSheet("border-image: url(./pin-2.png)")
        coordinate = eval(get_coordinate(current_event.address))
        lat = coordinate[0]
        lng = coordinate[1]
        get_map_link(lat, lng)

    def view_profile_clicked(self):
        profile_view_attend_window.show()
        self.hide()

    @staticmethod
    def attend_button_clicked():
        if str(current_event.hosts) == str(current_user.uid):
            show_dialog('You cannot join the event you host. ')
            return
        else:
            result = attend(current_user.uid, current_event.eid)
            if result == 'DUPLICATE':
                show_dialog('You already attended this event. ')
            if result == 'OK':
                show_dialog('Congrats, you are in! ')
            if result == 'FAILURE':
                show_dialog('Failed to add you to the event, try again later. ')
            return

    def back_button_clicked(self):
        lobby_window.show()
        lobby_window.refresh_attend()
        self.hide()


class HostEventDisplayWindow(QMainWindow, Ui_HostEventDisplayDialog):
    def __init__(self, parent=None):
        super(HostEventDisplayWindow, self).__init__(parent)
        self.setupUi(self)
        self.image_list = []
        self.last_image = 0
        self.host_image = None
        self.EventEditButton.clicked.connect(self.edit_button_clicked)
        self.BackButton.clicked.connect(self.back_button_clicked)
        self.eye1.clicked.connect(lambda: self.view_profile_clicked(0))
        self.eye2.clicked.connect(lambda: self.view_profile_clicked(1))
        self.eye3.clicked.connect(lambda: self.view_profile_clicked(2))
        self.eye4.clicked.connect(lambda: self.view_profile_clicked(3))
        self.eye5.clicked.connect(lambda: self.view_profile_clicked(4))
        self.eye6.clicked.connect(lambda: self.view_profile_clicked(5))
        self.eye7.clicked.connect(lambda: self.view_profile_clicked(6))
        self.eye8.clicked.connect(lambda: self.view_profile_clicked(7))
        self.eye9.clicked.connect(lambda: self.view_profile_clicked(8))
        self.eye10.clicked.connect(lambda: self.view_profile_clicked(9))
        self.eyeHost.clicked.connect(lambda: self.view_profile_clicked(-1))
        self.mapView.clicked.connect(self.map_view_clicked)
        self.BackButton.clicked.connect(self.back_button_clicked)
        self.SendEmailButton.clicked.connect(self.send_email_button_clicked)

    def update_host_image(self):
        #pixmap = load_image(get_user(current_event.hosts).image)
        #self.HostImage.setIcon(QIcon(pixmap))
        #size = QtCore.QSize()
        #size.setHeight(self.HostImage.height())
        #size.setWidth(self.HostImage.width())
        #self.HostImage.setIconSize(size)

        pixmap = load_image(get_user(current_event.hosts).image)
        self.HostImage.setVisible(True)
        self.HostImage.setPixmap(pixmap.scaled(self.HostImage.width(), self.HostImage.height()))

    def restore_attendees(self):
        self.image_list = []
        self.last_image = 0
        for i in range(0, 10):
            self.AttendeeList[i].setVisible(False)
            self.eyeList[i].setVisible(False)

    def update_attendees_image(self):
        global current_event
        current_event = get_event(current_event.eid)
        self.restore_attendees()
        self.image_list = get_image_list(current_event.attendees)
        last_image = 0
        for i, image in enumerate(self.image_list):
            if i > 9:
                last_image = 9
                break
            else:
                pixmap = load_image(self.image_list[i])
                self.AttendeeList[i].setVisible(True)
                self.eyeList[i].setVisible(True)
                self.AttendeeList[i].setPixmap(pixmap.scaled(self.AttendeeList[i].width(), self.AttendeeList[i].height()))
                last_image = i
        self.last_image = last_image

    def send_email_button_clicked(self):
        sender = current_user.google_id
        subject = "A New Message from the event: " + current_event.title
        temp_target = self.ToEmailInput.text()
        receiver = []
        if temp_target:
            target_user = retrieve_user('nickname', temp_target)
            receiver.append(target_user.email)
        else:
            tempList = EventController.get_join(current_event.eid)
            for item in tempList:
                user = get_user(item)
                receiver.append(user.email)
        message = self.GroupEmailContent.toPlainText()
        send_email(sender, receiver, subject, message)
        self.ToEmailInput.setText('')
        self.GroupEmailContent.setText('')

    def back_button_clicked(self):
        lobby_window.show()
        self.hide()
        
    def map_view_clicked(self):
        self.mapView.setStyleSheet("border-image: url(./pin-2.png)")
        coordinate = eval(get_coordinate(current_event.address))
        lat = coordinate[0]
        lng = coordinate[1]
        get_map_link(lat, lng)

    def view_profile_clicked(self, i):
        if i == -1:
            profile_view_host_window.show_user(current_event.hosts)
        else:
            profile_view_host_window.show_user(current_event.attendees[i])
        profile_view_host_window.show()
        self.hide()

    def edit_button_clicked(self):
        global current_event

        if current_event.eid != 0:
            _translate = QtCore.QCoreApplication.translate
            host_event_edit_window.TitleInput.setText(_translate("HostEventEdit", current_event.title))
            host_event_edit_window.DescriptionInput.setText(_translate("HostEventEdit", current_event.description))
            host_event_edit_window.AddressInput.setText(_translate("HostEventEdit", current_event.location))
            host_event_edit_window.CityInput.setText(_translate("HostEventEdit", current_event.location))
            host_event_edit_window.CatagoryComboBox.setCurrentText(_translate("HostEventEdit", current_user.tags))
            self.eventDate = current_event.event_date
            self.eventDateList = self.eventDate.split('-')
            host_event_edit_window.YearComboBox.setCurrentText(_translate("HostEventEdit", self.eventDateList[0]))
            host_event_edit_window.MonthComboBox.setCurrentText(_translate("HostEventEdit", self.eventDateList[1]))
            host_event_edit_window.DayComboBox.setCurrentText(_translate("HostEventEdit", self.eventDateList[2]))
            self.expireDate = current_event.expire_date
            self.eventDate = datetime.strptime(self.eventDate, '%Y-%m-%d')
            self.expireDate = datetime.strptime(self.expireDate, '%Y-%m-%d')
            current_event = get_event(current_event.eid)
            host_event_edit_window.update_attendees_image()
            host_event_edit_window.PeriodTimeInput.setText(_translate("HostEventEdit",
                                                                      str((self.expireDate - self.eventDate).days)))
            image_list = eval(current_event.image)
            display_list = []
            for image in image_list:
                if image is not None:
                    display_list.append(image)
            for i, image in enumerate(display_list):
                pixmap = load_image(image)
                host_event_edit_window.EventImageList[i].setPixmap(pixmap.scaled(
                    host_event_edit_window.EventImageList[i].width(),
                    host_event_edit_window.EventImageList[i].height()))

        host_event_edit_window.show()
        self.hide()


class HostEventEditWindow(QMainWindow, Ui_HostEventEdit):
    def __init__(self, parent=None):
        super(HostEventEditWindow, self).__init__(parent)
        self.image_list = []
        self.last_image = 0
        self.setupUi(self)
        self.SaveEventButton.clicked.connect(self.save_button_clicked)
        self.UploadImage1.clicked.connect(lambda: self.upload_image_button_clicked(1))
        self.UploadImage2.clicked.connect(lambda: self.upload_image_button_clicked(2))
        self.UploadImage3.clicked.connect(lambda: self.upload_image_button_clicked(3))
        self.DeleteSign1.clicked.connect(lambda: self.delete_clicked(0))
        self.DeleteSign2.clicked.connect(lambda: self.delete_clicked(1))
        self.DeleteSign3.clicked.connect(lambda: self.delete_clicked(2))
        self.DeleteSign4.clicked.connect(lambda: self.delete_clicked(3))
        self.DeleteSign5.clicked.connect(lambda: self.delete_clicked(4))
        self.DeleteSign6.clicked.connect(lambda: self.delete_clicked(5))
        self.DeleteSign7.clicked.connect(lambda: self.delete_clicked(6))
        self.DeleteSign8.clicked.connect(lambda: self.delete_clicked(7))
        self.DeleteSign9.clicked.connect(lambda: self.delete_clicked(8))
        self.DeleteSign10.clicked.connect(lambda: self.delete_clicked(9))

        self.BackButton.clicked.connect(self.back_button_clicked)

        for i in range(0, 10):
            self.AttendeeList[i].setStyleSheet("border-image: url(./Transparency.jpg);\n""")
            self.DeleteSignList[i].setVisible(False)

    def back_button_clicked(self):
        host_event_display_window.show()
        self.hide()

    def delete_clicked(self, i):
        if i > self.last_image:
            return
        else:
            removed = False
            try:
                remove_user(current_event.attendees[i], current_event.eid)
                removed = True
                self.image_list.pop(i)
                self.update_attendees_image()
            finally:
                if not removed:
                    show_dialog('Unable to remove user from event. ')

    def restore_attendees(self):
        self.image_list = []
        self.last_image = 0
        for i in range(0, 10):
            self.AttendeeList[i].setVisible(False)
            self.DeleteSignList[i].setVisible(False)

    def update_attendees_image(self):
        global current_event
        current_event = get_event(current_event.eid)
        self.restore_attendees()
        self.image_list = get_image_list(current_event.attendees)
        last_image = 0
        for i, image in enumerate(self.image_list):
            if i > 9:
                last_image = 9
                break
            else:
                pixmap = load_image(self.image_list[i])
                self.AttendeeList[i].setPixmap(pixmap.scaled(self.AttendeeList[i].width(),
                                                             self.AttendeeList[i].height()))
                self.AttendeeList[i].setVisible(True)
                self.DeleteSignList[i].setVisible(True)
                last_image = i
        self.last_image = last_image

    def upload_image_button_clicked(self, number):
        global current_event
        image_list = eval(current_event.image)
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
            now_time = datetime.now().strftime("%Y%m%d%H%M%S")
            random_num = random.randint(0, 1000000)
            file_title = str(now_time) + str(random_num) + '_event_' + str(number) + '.jpg'
            upload_result = upload_image(file_path, file_title)
            if upload_result:
                image_list[number - 1] = file_title
                current_event.image = str(image_list)
                display_list = eval(current_event.image)
                pixmap = load_image(display_list[number - 1])
                if pixmap != Errors.FAILURE.name:
                    if number == 1:
                        self.EventImage1.setPixmap(pixmap.scaled(self.EventImage1.width(),
                                                                 self.EventImage1.height()))
                    if number == 2:
                        self.EventImage2.setPixmap(pixmap.scaled(self.EventImage2.width(),
                                                                 self.EventImage2.height()))
                    if number == 3:
                        self.EventImage3.setPixmap(pixmap.scaled(self.EventImage3.width(),
                                                                 self.EventImage3.height()))

    def save_button_clicked(self):
        address = self.AddressInput.text()
        state = get_state(address)
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
            if datetime.strptime(end_date, "%Y-%m-%d") <= datetime.strptime(TODAY, "%Y-%m-%d"):
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
                response = Connection.edit_event(data)
                if response[0] == 'SUCCESS' or current_event == previous_event:
                    update_event_display(current_event.eid)
                    host_event_display_window.restore_attendees()
                    host_event_display_window.update_attendees_image()
                    host_event_display_window.update_host_image()
                    host_event_display_window.show()
                    self.hide()
                else:
                    current_event = previous_event
                    show_dialog('Unable to update, try again later. ')


class PostEventWindow(QMainWindow, Ui_HostEventEdit):
    def __init__(self, parent=None):
        super(PostEventWindow, self).__init__(parent)
        self.setupUi(self)
        self.image_list = []
        self.last_image = 0
        self.SaveEventButton.clicked.connect(self.save_button_clicked)
        self.UploadImage1.clicked.connect(lambda: self.upload_image_button_clicked(1))
        self.UploadImage2.clicked.connect(lambda: self.upload_image_button_clicked(2))
        self.UploadImage3.clicked.connect(lambda: self.upload_image_button_clicked(3))
        self.BackButton.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        lobby_window.show()
        lobby_window.refresh_host()
        self.hide()

    def upload_image_button_clicked(self, number):
        global current_event
        image_list = eval(current_event.image)
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
            now_time = datetime.now().strftime("%Y%m%d%H%M%S")
            random_num = random.randint(0, 1000000)
            file_title = str(now_time) + str(random_num) + '_event_' + str(number) + '.jpg'
            upload_result = upload_image(file_path, file_title)
            if upload_result:
                image_list[number - 1] = file_title
                current_event.image = str(image_list)
                display_list = eval(current_event.image)
                pixmap = load_image(display_list[number - 1])
                if pixmap != Errors.FAILURE.name:
                    if number == 1:
                        self.EventImage1.setPixmap(pixmap.scaled(self.EventImage1.width(),
                                                                 self.EventImage1.height()))
                    if number == 2:
                        self.EventImage2.setPixmap(pixmap.scaled(self.EventImage2.width(),
                                                                 self.EventImage2.height()))
                    if number == 3:
                        self.EventImage3.setPixmap(pixmap.scaled(self.EventImage3.width(),
                                                                 self.EventImage3.height()))

    def restore_attendees(self):
        self.image_list = []
        self.last_image = 0
        for i in range(0, 10):
            self.AttendeeList[i].setVisible(False)
            self.DeleteSignList[i].setVisible(False)

    def update_attendees_image(self):
        global current_event
        current_event = get_event(current_event.eid)
        self.restore_attendees()
        self.image_list = get_image_list(current_event.attendees)
        last_image = 0
        for i, image in enumerate(self.image_list):
            if i > 9:
                last_image = 9
                break
            else:
                pixmap = load_image(self.image_list[i])
                self.AttendeeList[i].setPixmap(pixmap.scaled(self.AttendeeList[i].width(),
                                                             self.AttendeeList[i].height()))
                self.AttendeeList[i].setVisible(True)
                self.DeleteSignList[i].setVisible(True)
                last_image = i
        self.last_image = last_image

    def save_button_clicked(self):
        global current_event
        address = self.AddressInput.text()
        state = get_state(address)
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
            if datetime.strptime(end_date, "%Y-%m-%d") <= datetime.strptime(TODAY, "%Y-%m-%d"):
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
                response = Connection.post_event(data)
                current_event.eid = response[1]['eid']
                current_event = get_event(current_event.eid)
                update_event_display(current_event.eid)
                host_event_display_window.restore_attendees()
                host_event_display_window.update_attendees_image()
                host_event_display_window.update_host_image()
                host_event_display_window.show()
                self.hide()


class ProfileEditWindow(QMainWindow, Ui_RegisterDialog):
    def __init__(self, parent=None):
        super(ProfileEditWindow, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.back_button_clicked)
        self.UploadImageButton.clicked.connect(self.upload_image_button_clicked)
        self.SaveProfileButton.clicked.connect(self.save_button_clicked)

    def back_button_clicked(self):
        lobby_window.show()
        update_lobby_user()
        lobby_window.refresh_host()
        self.hide()

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
            upload_result = upload_image(file_path, file_title)
            if upload_result:
                current_user.image = file_title
                pixmap = load_image(current_user.image)
                if pixmap != Errors.FAILURE.name:
                    self.profile_picture.setPixmap(pixmap.scaled(self.profile_picture.width(),
                                                                 self.profile_picture.height()))

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
            response = Connection.edit_user(current_user)
            if response[0] == 'MISSING':
                if current_user == previous_user:
                    update_lobby_user()
                    lobby_window.show()
                    self.hide()
                else:
                    show_dialog('User with this credential does not exist. ')
                    current_user = previous_user
            elif response[0] == 'FAILURE':
                show_dialog("Unable to connect to server, please check your connections. ")
                current_user = previous_user
            else:
                current_user.uid = response[1]['id']
                update_lobby_user()
                lobby_window.show()
                self.hide()


class ProfileViewWindow(QMainWindow, Ui_UserProfileDisplay):
    def __init__(self, parent=None):
        super(ProfileViewWindow, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        attend_event_display_window.show()
        self.hide()

    def show_user(self, user_id):
        user = get_user(user_id)
        first_name, last_name = user.name.split(' ')
        self.FirstNameOutput.setText(first_name)
        self.LastNameOutput.setText(last_name)
        self.GenderOutput.setText(user.gender)
        self.EmailAddressOutput.setText(user.email)
        self.DescritionOutput.setText(user.description)
        pixmap = load_image(user.image)
        self.UserImageOutput.setPixmap(pixmap.scaled(self.UserImageOutput.width(),
                                                     self.UserImageOutput.height()))


class HostProfileViewWindow(QMainWindow, Ui_UserProfileDisplay):
    def __init__(self, parent=None):
        super(HostProfileViewWindow, self).__init__(parent)
        self.setupUi(self)
        self.BackButton.clicked.connect(self.back_button_clicked)

    def back_button_clicked(self):
        global current_event
        current_event = get_event(current_event.eid)

        host_event_display_window.show()
        self.hide()

    def show_user(self, user_id):
        user = get_user(user_id)
        first_name, last_name = user.name.split(' ')
        self.FirstNameOutput.setText(first_name)
        self.LastNameOutput.setText(last_name)
        self.GenderOutput.setText(user.gender)
        self.EmailAddressOutput.setText(user.email)
        self.DescriptionOutput.setText(user.description)
        pixmap = load_image(user.image)
        self.UserImageOutput.setPixmap(pixmap.scaled(self.UserImageOutput.width(),
                                                     self.UserImageOutput.height()))
        self.CityOutput.setText(user.location)
        self.TagOutput.setText(user.tags)
        self.update_attendees(user)
        self.update_hosts(user)

    def update_attendees(self, user: UserModel):
        for event_title in self.AttendEventList:
            event_title.setText('')
        for i, event_id in enumerate(user.join_events):
            event = get_event(event_id)
            if i > 2:
                break
            else:
                self.AttendEventList[i].setText(event.title)

    def update_hosts(self, user: UserModel):
        for event_title in self.HostEventList:
            event_title.setText('')
        for i, event_id in enumerate(user.host_events):
            event = get_event(event_id)
            if i > 2:
                break
            else:
                self.HostEventList[i].setText(event.title)


def show_dialog(message):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText(message)
    msg.setWindowTitle("Warning")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()


def string_to_enum(tags_input):
    check_set = {'sports', 'social', 'outdoors', 'indoors', 'sightseeing',
                 'exhibitions', 'entertaining', 'charity', 'business'}
    if tags_input not in check_set:
        tags_input = 'anything'
    return tags_input


def upload_image(file_path, file_key):
    result = AWS_CONNECTOR.upload_image(file_path, file_key)
    if result:
        return True
    else:
        show_dialog('Error uploading image, please try again. ')
        return False


def load_image(file_title):
    if file_title == '':
        return
    else:
        loaded = False
        try:
            link = AWS_CONNECTOR.download_image(file_title)
            request = urllib.request.Request(link)
            data = urllib.request.urlopen(request).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            loaded = True
            return pixmap
        finally:
            if not loaded:
                return Errors.FAILURE.name


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


def parse_list(event_list):
    length = 5
    parsed_list = []
    count = 0
    temp_list = []
    for event in event_list:
        if count < length:
            temp_list.append(event)
            count = count + 1
        else:
            parsed_list.append(temp_list)
            count = 0
            temp_list = list()
            temp_list.append(event)
            count = count + 1
    parsed_list.append(temp_list)
    return parsed_list


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
        datetime.strptime(date, "%Y-%m-%d")
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
    d1 = datetime(cur_date[0], cur_date[1], cur_date[2])
    d = d1 + timedelta(days=int(register_period))
    year = str(d.year)
    month = str(d.month).zfill(2)
    date = str(d.day-1).zfill(2)
    return year + '-' + month + '-' + date


def update_event_display(eid):
    event = get_event(eid)
    global current_event
    current_event = event
    user = get_user(event.hosts)
    host_event_display_window.AddressOutput.setText(event.address)
    host_event_display_window.CityOutput.setText(event.location)
    host_event_display_window.DateOutput.setText(event.expire_date)
    host_event_display_window.DescriptionOutput.setText(event.description)
    host_event_display_window.UserName.setText(event.title)
    host_event_display_window.HostIDOutput.setText(user.nickname)
    image_list = eval(current_event.image)
    display_list = []
    for event_image in host_event_display_window.EventImageList:
        event_image.setStyleSheet("border-image: url(./Transparency.png);\n""")
    for image in image_list:
        if image is not None:
            display_list.append(image)
    for i, image in enumerate(display_list):
        pixmap = load_image(image)
        host_event_display_window.EventImageList[i].setPixmap(pixmap.scaled(
            host_event_display_window.EventImageList[i].width(),
            host_event_display_window.EventImageList[i].height()))


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
    res = Connection.request_user(int(uid))
    user = response_to_user(res[1])
    return user


def get_event(eid):
    res = Connection.request_event(int(eid))
    event = response_to_event(res[1])
    return event


def get_default_list(uid):
    user = get_user(uid)
    state = user.location
    tag = user.tags
    event_filter = {
        'state': state,
        'tag': tag,
        'time': None,
        'keyword': None
    }
    default_list = get_list(event_filter)

    return default_list


def get_list(event_filter):
    result = Connection.get_events(event_filter)
    status = result[0]
    if status == Errors.FAILURE.name:
        show_dialog('Error retrieving event, please try again. ')
        result = []
    else:
        result = result[1]

    result = parse_list(result)
    return result


def attend(uid, eid):
    result = Connection.attend_event(uid, eid)
    return result


def remove_user(uid, eid):
    result = Connection.remove_user(uid, eid)
    return result


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def get_map_link(lat, lng):
    link = 'https://www.google.com/maps/search/?api=1&query=' + str(lat) + ',' + str(lng)
    webbrowser.open(link, new=2)
    
    '''
    coordinate = eval(current_event.address)
    lat = coordinate[0]
    lng = coordinate[1]
    '''


def send_email(sender, receiver, subject, message_text):
    gmail_agent = Gmail()
    service = gmail_agent.build_service(google_credentials)

    receiver_num = len(receiver)
    for i in range(receiver_num):
        curr_receiver = receiver[i]
        message = gmail_agent.create_message(sender, curr_receiver, subject, message_text)
        gmail_agent.send_message(service, sender, message)


def get_image_list(user_list):
    image_list = []
    for user_id in user_list:
        user = get_user(user_id)
        image_list.append(user.image)

    return image_list


def get_attend_event_list():
    global current_user
    current_user = get_user(current_user.uid)
    result = []
    for event_id in current_user.join_events:
        event = get_event(event_id)
        tuple = [event.eid, event.title, event.location,
                 datetime.strptime(event.expire_date, '%Y-%m-%d').date(), event.image]
        result.append(tuple)

    result = parse_list(result)
    return result


def get_host_event_list():
    global current_user
    current_user = get_user(current_user.uid)
    result = []
    for event_id in current_user.host_events:
        event = get_event(event_id)
        tuple = [event.eid, event.title, event.location,
                 datetime.strptime(event.expire_date, '%Y-%m-%d').date(), event.image]
        result.append(tuple)

    result = parse_list(result)
    return result


if __name__ == '__main__':
    sys.excepthook = except_hook
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
    profile_view_host_window = HostProfileViewWindow()
    sign_in_window.show()
    sys.exit(app.exec_())
