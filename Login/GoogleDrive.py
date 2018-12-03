from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from apiclient.http import MediaFileUpload


def set_up_drive(credentials):
    service = build('drive', 'v3', http=credentials.authorize(Http()))
    return service


def upload_image(service, file_path, file_title):
    file_metadata = {'name': file_title}
    media = MediaFileUpload(file_path,
                            mimetype='image/jpeg')
    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='thumbnailLink').execute()
    return file.get('thumbnailLink')
