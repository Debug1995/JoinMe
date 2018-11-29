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


def add_user(user: UserModel):
    data = {
        'name': user.name,
        'nickname': user.nickname,
        'email': user.email,
        'location': user.location,
        'description': user.description,
        'gender': user.gender,
        'image': user.image,
        'tags': user.tags,
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


def edit_user(user: UserModel):
    data = {
        'name': user.name,
        'nickname': user.nickname,
        'email': user.email,
        'location': user.location,
        'description': user.description,
        'gender': user.gender,
        'image': user.image,
        'tags': user.tags,
        'google_id': user.google_id
    }

    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_edit_user_response(*args):
            nonlocal result
            result = args

        socketIO.emit('edit_user', data, on_edit_user_response)
        socketIO.wait_for_callbacks()
        return result


def post_event(data):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_post_event_response(*args):
            nonlocal result
            result = args

        socketIO.emit('post_event', data, on_post_event_response)
        socketIO.wait_for_callbacks()
        return result


def request_user(uid):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_request_user_response(*args):
            nonlocal result
            result = args

        socketIO.emit('request_user', uid, on_request_user_response)
        socketIO.wait_for_callbacks()
        return result


def request_event(eid):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_request_event_response(*args):
            nonlocal result
            result = args

        socketIO.emit('request_event', eid, on_request_event_response)
        socketIO.wait_for_callbacks()
        print(result)
        return result


def edit_event(data):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_edit_event_response(*args):
            nonlocal result
            result = args

        socketIO.emit('edit_event', data, on_edit_event_response)
        socketIO.wait_for_callbacks()
        return result


def get_default(location):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_edit_event_response(*args):
            nonlocal result
            result = args

        socketIO.emit('get_default', location, on_edit_event_response)
        socketIO.wait_for_callbacks()
        return result


def attend_event(uid, eid):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_attend_event_response(*args):
            nonlocal result
            result = args

        data = {
            'uid': uid,
            'eid': eid
        }
        socketIO.emit('attend_event', data, on_attend_event_response)
        socketIO.wait_for_callbacks()
        return result
