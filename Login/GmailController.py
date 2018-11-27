import httplib2
import base64
import json
from oauth2client.client import flow_from_clientsecrets
from apiclient.discovery import build
from email.mime.text import MIMEText

# needed libs:
#     pip install --upgrade google-api-python-client oauth2client
#     pip install email
#     pip install pybase64
# how to use gamil:
# 1. get login url
#     gmail = Gmail()
#     print(gmail.get_autho_uri())
# 2. copy autho_code back
#     credentials = gmail.get_credentials('the autho_code')
#     service = gmail.build_service(credentials)
# 3. creat a mail message object
#     sender = 'sender email'
#     to = 'receiver email'
#     subject = 'gmail api test'
#     message_text = 'This is a message sent from gmail api!!'
#     message = gmail.create_message(sender, to, subject, message_text)
# 4. send the email
#     gmail.send_message(service, '199511zc@gmail.com', message)

class Gmail:
    SECRET_LOCATION = 'secret.json'
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

    def get_use_email(self, credentials):
        email = credentials.id_token['email']
        return email
    
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
        return {'raw' : b64_string}
    
    def send_message(self, service, user_id, message):
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message