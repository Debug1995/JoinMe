from Model.UserModel import *
import ControllerWrapper


def get_user(email):
    data = {'email': email}
    result = ControllerWrapper.login(data)
    return result


def add_user(user: UserModel):
    data = {
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

    result = ControllerWrapper.sign_up(data)
    return result


def edit_user(user: UserModel):
    data = {
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

    result = ControllerWrapper.edit_user(data)
    return result


def request_user(uid):
    result = ControllerWrapper.request_user(uid)
    return result


def post_event(data):
    result = ControllerWrapper.post_event(data)
    return result


def request_event(eid):
    result = ControllerWrapper.request_event(eid)
    return result


def edit_event(data):
    result = ControllerWrapper.edit_event(data)
    return result


def get_events(event_filter):
    result = ControllerWrapper.get_events(event_filter)
    return result


def attend_event(uid, eid):
    data = {
        'uid': uid,
        'eid': eid
    }

    result = ControllerWrapper.attend_event(data)
    return result


def remove_user(uid, eid):
    data = {
        'uid': uid,
        'eid': eid
    }

    result = ControllerWrapper.remove_user(data)
    return result