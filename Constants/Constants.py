from enum import Enum


# mysql -h joinme.czodqmkcwniq.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
class ConnectConstants:
    USER = "DB USER"
    PASSWORD = "DB PASSWORD"
    HOST = "DB HOST"
    DATABASE = "DB NAME"
    AWS_KEY = 'AWS KEY'
    AWS_SECRET = 'AWS SECRET'
    AWS_URL = 'AWS URL'


class UserFields(Enum):
    userid = 1
    realname = 2
    nickname = 3
    gender = 4
    email = 5
    location = 6
    tags = 7
    description = 8
    googleid = 9


class Tags(Enum):
    sports = 1
    social = 2
    outdoors = 3
    indoors = 4
    sightseeing = 5
    exhibitions = 6
    entertaining = 7
    charity = 8
    business = 9
    anything = 10


class Errors(Enum):
    SUCCESS = 1
    FAILURE = 2
    DUPLICATE = 3
    MISSING = 4
