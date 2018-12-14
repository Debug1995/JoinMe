from enum import Enum


# mysql -h joinme.czodqmkcwniq.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
class ConnectConstants:
    USER = "admin"
    PASSWORD = "joinme4156"
    HOST = "joinme.czodqmkcwniq.us-east-1.rds.amazonaws.com"
    DATABASE = "joinme_db"
    AWS_KEY = 'AKIAJK5XABQ3I6BOHTYA'
    AWS_SECRET = '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'
    AWS_URL = 'joinmeprofileimage.s3-us-east-1.amazonaws.com'


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
