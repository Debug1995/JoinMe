from Login.GmailController import *
from QT_FrontEnd.logic.Connection import *
import webbrowser


SECRET_LOCATION = './secret.json'
SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]


def initiate_login():
    gmail = Gmail()
    webbrowser.open(gmail.get_autho_uri(), new=2)


def verify_login(token):
    returned = False
    try:
        gmail = Gmail()
        credentials = gmail.get_credentials(token)
        returned = True
        return credentials
    finally:
        if not returned:
            return 'login error'


def verify_registration(credential):
    gmail = Gmail()
    email = gmail.get_user_email(credential)
    query_result = get_user(email)
    return query_result



# service = gmail.build_service(credentials)
#sender = '199511zc@gmail.com'
#to = 'cy2468@columbia.edu'
#subject = 'gmail api test'
#message_text = 'This is a message sent from gmail api!!'
#message = gmail.create_message(sender, to, subject, message_text)

#gmail.send_message(service, '199511zc@gmail.com', message)
