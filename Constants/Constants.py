from enum import Enum

class ConnectConstants:
    USER = "admin"
    PASSWORD = "joinme4156"
    HOST = "joinme.czodqmkcwniq.us-east-1.rds.amazonaws.com"
    DATABASE = "joinme_db"


class UserFields(Enum):
    uid = 1
    name = 2
    nickname = 3
    gender = 4
    email = 5
    location = 6
    tags = 7
    description = 8
