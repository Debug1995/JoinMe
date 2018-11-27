from socketIO_client import SocketIO, LoggingNamespace


def get_user(email):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        socketIO.emit('login', {'email': email}, on_login_response)
        socketIO.wait_for_callbacks()


def on_login_response(*args):
    print('response:', args, len(args))


get_user('email_1')
