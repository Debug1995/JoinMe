from flask import Flask
import socketio
import eventlet
import ConnectionHandler

sio = socketio.Server()
app = Flask(__name__)


@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid, environ)


@sio.on('login')
def login(sid, data):
    response = ConnectionHandler.login(data['email'])
    if response == 'FAILURE':
        return 'FAILURE', None
    if response == 'MISSING':
        return 'MISSING', None
    return 'OK', {'Nickname': response.nickname, 'Image': response.image, 'Email': response.email}


if __name__ == '__main__':
    app = socketio.WSGIApp(sio, app)
    eventlet.wsgi.server(eventlet.listen(('localhost', 8080)), app)
