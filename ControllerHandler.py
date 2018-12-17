import Controller.EventController as EventController
import Controller.UserController as UserController
from Model.EventModel import EventModel as EventModel
from Model.UserModel import UserModel as UserModel
from Constants.Constants import Errors
from Constants.Constants import UserFields


def post_event(data):
    event = EventModel(0, data['title'], data['tags'], data['description'], data['image'], data['hosts'], [],
                       data['event_date'], data['state'], data['address'], data['register_period'])
    
    EventController.print_event(event)
    result = EventController.add_event(event)
    if result == Errors.DUPLICATE.name:
        event.eid = None
        return Errors.DUPLICATE.name, None
    elif result == Errors.FAILURE.name:
        event.eid = None
        return Errors.FAILURE.name, None
    print('Event #' + str(result) + ' has been posted. \n')
    event.eid = result

    result = EventController.host_event(event.hosts, event)
    if result == Errors.DUPLICATE.name:
        current_event.eid = None
        print("You have already hosted this event. \n")
        return Errors.DUPLICATE.name
    elif result == Errors.FAILURE.name:
        current_event.eid = None
        return Errors.FAILURE.name

    EventController.print_event(event)
    data = {
        'eid': event.eid,
        'title': event.title,
        'tags': event.tags,
        'description': event.description,
        'hosts': event.hosts,
        'event_date': event.event_date,
        'state': event.location,
        'address': event.address,
        'image': event.image,
        'register_period': event.register_period,
        'expire_date': event.expire_date
    }
    return 'OK', data


def update_event(data):
    event = EventModel(data['id'], data['title'], data['tags'], data['description'], data['image'], data['hosts'], [],
                       data['event_date'], data['state'], data['address'], data['register_period'])
    EventController.print_event(event)

    result = EventController.edit_event(event)

    if result == Errors.MISSING.name:
        return Errors.MISSING.name
    elif result == Errors.SUCCESS.name:
        return Errors.SUCCESS.name
    else:
        return Errors.FAILURE.name


def register(data):
    user = UserModel(0, data['name'], data['nickname'], data['gender'], data['email'], data['location'],
                     stringToEnum(data['tags']), data['description'], [], [], data['image'], data['google_id'])
    result = UserController.add_user(user)
    if result == Errors.DUPLICATE.name:
        return result, None
    elif result == Errors.FAILURE.name:
        return result, None
    else:
        user = UserController.retrieve_user(UserFields.googleid.name, data['google_id'])
        data = {
            'id': user.uid,
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
        return 'OK', data


def update_profile(data):
    user = UserModel(0, data['name'], data['nickname'], data['gender'], data['email'], data['location'],
                     stringToEnum(data['tags']), data['description'], [], [], data['image'], data['google_id'])
    result = UserController.edit_user(user)
    if result == Errors.MISSING.name:
        return result, None
    elif result == Errors.FAILURE.name:
        return result, None
    else:
        user = UserController.retrieve_user(UserFields.googleid.name, data['google_id'])
        data = {
            'id': user.uid,
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
        return 'OK', data


def login(email):
    result = UserController.retrieve_user(UserFields.googleid.name, email)
    return result


def group_email():
    global current_user
    global current_event
    if not current_user:
        add_output('You have to log in first. \n')
    event_id = event_id_input.get()
    current_event = EventController.retrieve_event(event_id)
    if current_event == Errors.MISSING.name:
        add_output('No such event. \n')
        current_event = None
        return
    elif current_event == Errors.FAILURE.name:
        return_failure()
        current_event = None
        return
    if current_user.uid != current_event.hosts:
        add_output('You have to be the host to send a group email. \n')
        current_event = None
        return

    message = email_message_input.get()
    user_list = current_event.attendees
    EventController.print_event(current_event)
    for user_id in user_list:
        sent = False
        try:
            temp_user = UserController.retrieve_user(UserFields.userid.name, user_id)
            send_email(message, temp_user.email)
            sent = True
        finally:
            if not sent:
                add_output('Unable to send email to ' + temp_user.email + '. \n')
    return


def contact_friend():
    global current_user
    if not current_user:
        add_output('You have to log in first. \n')
    message = email_message_input.get()
    nickname = email_nickname_input.get()
    sent = False

    try:
        temp_user = UserController.retrieve_user(UserFields.nickname.name, nickname)
        if temp_user == Errors.MISSING.name:
            add_output('No user with nickname ' + nickname + '. Please check again. \n')
        else:
            send_email(message, temp_user.email)
        sent = True
    finally:
        if not sent:
            add_output('Unable to send email to ' + temp_user.email + '. \n')

    return


# TODO: Replace with sending real email
def send_email(message: str, address: str):
    add_output('Message: ' + message + ' send to ' + address + '. \n')


def get_events(data):
    return EventController.get_events(data)


def stringToEnum(tags_input):
    check_set = {'sports', 'social', 'outdoors', 'indoors', 'sightseeing',
                 'exhibitions', 'entertaining', 'charity', 'business'}
    if tags_input not in check_set:
        tags_input = 'anything'
    return tags_input
