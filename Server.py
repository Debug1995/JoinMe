from flask import Flask
import socketio
import eventlet
import ConnectionHandler
from Controller.UserController import *
from Controller.EventController import *

sio = socketio.Server()
app = Flask(__name__)


@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)


@sio.on('login')
def login(sid, data):
    response = ConnectionHandler.login(data['email'])
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


@sio.on('sign_up')
def sign_up(sid, data):
    response = ConnectionHandler.register(data)
    return response


@sio.on('edit_user')
def edit_user(sid, data):
    print(data)
    response = ConnectionHandler.update_profile(data)
    return response


@sio.on('post_event')
def post_event(sid, data):
    print(data)
    response = ConnectionHandler.post_event(data)
    return response


@sio.on('edit_event')
def edit_event(sid, data):
    print(data)
    response = ConnectionHandler.update_event(data)
    return response


@sio.on('get_default')
def get_default(sid, data):
    response = ConnectionHandler.get_default(data)
    return response


@sio.on('request_user')
def request_user(sid, data):
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


@sio.on('request_event')
def request_event(sid, data):
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


@sio.on('attend_event')
def attend_event(sid, data):
    result = join_event(data)
    return result


if __name__ == '__main__':
    app = socketio.WSGIApp(sio, app)
    eventlet.wsgi.server(eventlet.listen(('localhost', 8080)), app)
