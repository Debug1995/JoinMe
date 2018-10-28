from flask import Blueprint

user_model = Blueprint('user_model', __name__)


@user_model.route("/Model")
class UserModel:
    def __init__(self, uid, name, nickname, gender, email, location, tags, description):
        self.uid = uid
        self.name = name
        self.nickname = nickname
        self.gender = gender
        self.email = email
        self.location = location
        self.tags = tags
        self.description = description
        self.host_events = []
        self.join_events = []

    def join(self, eid):
        self.join_events.append(eid)

    def host(self, eid):
        self.host_events.append(eid)

    def update(self, uid, name, nickname, gender, email, location, tags, description):
        self.uid = uid
        self.name = name
        self.nickname = nickname
        self.gender = gender
        self.email = email
        self.location = location
        self.tags = tags
        self.description = description
