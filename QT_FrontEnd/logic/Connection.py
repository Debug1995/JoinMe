import socket
from PyQt5 import QtCore, QtGui
import string
import random


class Connection(QtCore.QObject):
    remote_address = ("localhost", 1337)

    def __init__(self, parent=None):
        super(Connection, self).__init__(parent)
