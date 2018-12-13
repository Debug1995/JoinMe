from boto3.session import Session
import boto3
import botocore


class AWSConnector:
    def __init__(self):
        self.access_key = 'AKIAJK5XABQ3I6BOHTYA'
        self.secret_key = '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'
        self.url = 'joinmeprofileimage.s3-us-east-1.amazonaws.com'
        self.session = Session(aws_access_key_id=self.access_key,
                               aws_secret_access_key=self.secret_key)
        self.s3_client = self.session.client('s3',
                                             aws_access_key_id=self.access_key,
                                             aws_secret_access_key=self.secret_key)

    def uploadImage(self, imageName, path = ''):
        resp = self.s3_client.put_object(Bucket="joinmeprofileimage",
                                         Key=imageName,
                                         Body=open(path+imageName, 'rb').read())
        if resp['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        return False

    def downloadImage(self, imageName, type):
        fileName = None
        if type == 0: #profile
            fileName = 'ProfileImage'
        elif type == 1: #event
            fileName = 'EventImage'
        else:
            return 'type error'
        s3 = boto3.resource('s3',
                            aws_access_key_id=self.access_key,
                            aws_secret_access_key=self.secret_key)
        s3.Bucket('joinmeprofileimage').download_file(imageName, fileName+'/download'+imageName)


connector = AWSConnector()
connector.uploadImage('9.png')
connector.downloadImage('9.png', 1)

