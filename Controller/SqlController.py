import threading
import mysql.connector

def synchronized(func):
    func.__lock__ = threading.Lock()
 
    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
 
    return lock_func

class SqlController(object):
    instance = None
 
    @synchronized
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
 
    def __init__(self, user, password, database):
        self.sql_connector = mysql.connector.connect(
            user = user,
            password = password,
            database = database,
        )