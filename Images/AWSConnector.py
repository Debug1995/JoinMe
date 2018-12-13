from boto3.session import Session
import boto3
from Constants.Constants import ConnectConstants


class AWSConnector:
    def __init__(self):
        self.access_key = ConnectConstants.AWS_KEY
        self.secret_key = ConnectConstants.AWS_SECRET
        self.url = ConnectConstants.AWS_URL
        self.session = Session(aws_access_key_id=self.access_key,
                               aws_secret_access_key=self.secret_key)
        self.s3_client = self.session.client('s3',
                                             aws_access_key_id=self.access_key,
                                             aws_secret_access_key=self.secret_key)

    def upload_image(self, image_path, image_key):
        uploaded = False
        try:
            resp = self.s3_client.put_object(Bucket="joinmeprofileimage",
                                             Key=image_key,
                                             Body=open(image_path, 'rb').read())
            if resp['ResponseMetadata']['HTTPStatusCode'] == 200:
                uploaded = True
                return True
        finally:
            if not uploaded:
                return False

    def download_image(self, image_name, file_type):
        if file_type == 0:  # profile
            file_path = '../../Images/Profile/'
        elif file_type == 1:  # event
            file_path = '../../Images/Activity/'
        else:
            return 'type error', None
        s3 = boto3.resource('s3',
                            aws_access_key_id=self.access_key,
                            aws_secret_access_key=self.secret_key)
        s3.Bucket('joinmeprofileimage').download_file(image_name, file_path + image_name)

        return file_path + image_name

# aws_connector = AWSConnector()
#
# s3 = boto3.resource('s3',
#                     aws_access_key_id=ConnectConstants.AWS_KEY,
#                     aws_secret_access_key=ConnectConstants.AWS_SECRET)
# s3.Bucket('joinmeprofileimage').download_file('jl4924@columbia.edu_profile.jpg',
#                                               'Profile/jl4924@columbia.edu_profile.jpg')
