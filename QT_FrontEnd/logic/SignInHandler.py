import httplib2
import base64
from oauth2client.client import flow_from_clientsecrets
from apiclient.discovery import build
from email.mime.text import MIMEText
import webbrowser


SECRET_LOCATION = './secret.json'
SCOPES = [
    'https://www.googleapis.com/auth/gmail.send',
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]


class Gmail:
    SECRET_LOCATION = './secret.json'
    SCOPES = [
        'https://www.googleapis.com/auth/gmail.send',
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile'
    ]

    def __init__(self):
        self.flow = flow_from_clientsecrets(self.SECRET_LOCATION,
                                            scope=' '.join(self.SCOPES),
                                            redirect_uri='urn:ietf:wg:oauth:2.0:oob')

    def get_autho_uri(self):
        autho_uri = self.flow.step1_get_authorize_url()
        return autho_uri

    def get_credentials(self, autho_code):
        credentials = self.flow.step2_exchange(autho_code)
        self.refresh_code = credentials.refresh_token
        return credentials

    def build_service(self, credentials):
        http = httplib2.Http()
        http = credentials.authorize(http)
        service = build('gmail', 'v1', http=http)
        return service

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
        b64_string = b64_bytes.decode()
        return {'raw': b64_string}

    def send_message(self, service, user_id, message):
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
#         try:
#
#         except errors.HttpError as error:
#             print('An error occurred: %s' %s)


def initiate_login():
    gmail = Gmail()
    webbrowser.open(gmail.get_autho_uri(), new=2)

#credentials = gmail.get_credentials('4/iQDv65cotGFKZew9KgEJfAJVGkqSxIqf2xDfMqqvBVVf5TsXugD9PO0')
#service = gmail.build_service(credentials)
# print(credentials)

#sender = '199511zc@gmail.com'
#to = 'cy2468@columbia.edu'
#subject = 'gmail api test'
#message_text = 'This is a message sent from gmail api!!'
#message = gmail.create_message(sender, to, subject, message_text)

#gmail.send_message(service, '199511zc@gmail.com', message)