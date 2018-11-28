from socketIO_client import SocketIO, LoggingNamespace
from Model.UserModel import *


def get_user(email):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_login_response(*args):
            nonlocal result
            result = args
        socketIO.emit('login', {'email': email}, on_login_response)
        socketIO.wait_for_callbacks()
        return result


def send_user(user: UserModel):
    data = {
        'name': user.name,
        'nickname': user.nickname,
        'email': user.email,
        'location': user.location,
        'description': user.description,
        'gender': user.gender,
        'image': user.image,
        'tags': user.tags.name,
        'google_id': user.google_id
    }

    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_sign_up_response(*args):
            nonlocal result
            result = args

        socketIO.emit('sign_up', data, on_sign_up_response)
        socketIO.wait_for_callbacks()
        return result
