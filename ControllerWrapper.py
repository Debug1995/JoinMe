from flask import Flask
import ControllerHandler
from Controller.UserController import *
from Controller.EventController import *

app = Flask(__name__)


def login(data):
    response = ControllerHandler.login(data['email'])
    if response == 'FAILURE':
        return 'FAILURE', None
    elif response == 'MISSING':
        return 'MISSING', None
    else:
        user = response
        data = {
            'id': user.uid,
            'name': user.name,
            'nickname': user.nickname,
            'email': user.email,
            'location': user.location,
            'description': user.description,
            'gender': user.gender,
            'image': user.image,
            'tags': user.tags,
            'google_id': user.google_id,
            'join': str(user.join_events),
            'host': str(user.host_events)
        }
        return 'OK', data


def sign_up(data):
    response = ControllerHandler.register(data)
    return response


def edit_user(data):
    response = ControllerHandler.update_profile(data)
    return response


def post_event(data):
    response = ControllerHandler.post_event(data)
    return response


def edit_event(data):
    print(data)
    response = ControllerHandler.update_event(data)
    return response


def get_default(data):
    response = ControllerHandler.get_default(data)
    return response


def request_user(data):
    print(data)
    user = retrieve_user('userid', data)
    if user == 'FAILURE':
        return user, None
    response = {
        'id': user.uid,
        'name': user.name,
        'nickname': user.nickname,
        'email': user.email,
        'location': user.location,
        'description': user.description,
        'gender': user.gender,
        'image': user.image,
        'tags': user.tags,
        'google_id': user.google_id,
        'join': user.join_events,
        'host': user.host_events
    }
    return 'OK', response


def request_event(data):
    print(data)
    event = retrieve_event(data)
    if event == 'FAILURE':
        return event, None
    response = {
        'id': event.eid,
        'title': event.title,
        'description': event.description,
        'address': event.address,
        'location': event.location,
        'image': event.image,
        'tags': event.tags,
        'event_date': event.event_date,
        'expire_date': event.expire_date,
        'host': event.hosts,
        'join': event.attendees
    }
    return 'OK', response


def attend_event(data):
    result = join_event(data)
    return result
