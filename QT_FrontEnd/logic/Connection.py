from socketIO_client import SocketIO, LoggingNamespace


def get_user(email):
    with SocketIO('localhost', 8080, LoggingNamespace) as socketIO:
        result = None

        def on_login_response(*args):
            nonlocal result
            result = args
        socketIO.emit('login', {'email': email}, on_login_response)
        socketIO.wait_for_callbacks()
        return result
