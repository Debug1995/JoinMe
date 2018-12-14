from boto3.session import Session
import boto3
import os
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

    def download_image(self, image_name):
        url = self.s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': 'joinmeprofileimage',
                                                            'Key': image_name},
                                                    ExpiresIn=3600)
        return url

# aws_connector = AWSConnector()
#
# s3 = boto3.resource('s3',
#                     aws_access_key_id=ConnectConstants.AWS_KEY,
#                     aws_secret_access_key=ConnectConstants.AWS_SECRET)
# s3.Bucket('joinmeprofileimage').download_file('jl4924@columbia.edu_profile.jpg',
#                                               'Profile/jl4924@columbia.edu_profile.jpg')
