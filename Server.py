from flask import Flask
import socketio
import eventlet
import ConnectionHandler

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
            'google_id': user.google_id
        }
        return 'OK', data


@sio.on('sign_up')
def login(sid, data):
    print(data)
    response = ConnectionHandler.register(data)
    return response


if __name__ == '__main__':
    app = socketio.WSGIApp(sio, app)
    eventlet.wsgi.server(eventlet.listen(('localhost', 8080)), app)
