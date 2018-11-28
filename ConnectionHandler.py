import socket
import Controller.EventController as EventController
import Controller.UserController as UserController
from Model.EventModel import EventModel as EventModel
from Model.UserModel import UserModel as UserModel
from Constants.Constants import Errors
from Constants.Constants import UserFields
from Constants.Constants import Tags


current_event: UserModel = None
current_user: UserModel = None


def read_event():
    eid = 0
    event_title = str(title_input.get())
    tags = stringToEnum(str(tags_input.get()))
    description = str(description_input.get())
    image = str(image_input.get())
    hosts = None
    attendees = []
    event_date = str(event_date_input.get())
    location = str(location_input.get())
    register_period = str(period_input.get())
    new_event = EventModel(eid, event_title, tags.name, description, image, hosts, attendees, event_date,
                           location, register_period)
    return new_event


def read_user():
    uid = 0
    real_name = str(realname_input.get())
    nickname = str(nickname_input.get())
    gender = str(gender_input.get())
    email = str(email_input.get())
    location = str(user_location_input.get())
    tags = stringToEnum(str(user_tags_input.get()))
    description = user_description_input.get()
    host_events = []
    join_events = []
    new_event = UserModel(uid, real_name, nickname, gender, email, location, tags, description,
                          host_events, join_events)
    return new_event


def post_event():
    global current_event
    global current_user
    current_event = read_event()
    if not current_user:
        add_output("You have to login first to post events. \n")
    else:
        result = EventController.add_event(current_user, current_event)
        if result == Errors.DUPLICATE.name:
            current_event.eid = None
            add_output("The same event already exists. \n")
        elif result == Errors.FAILURE.name:
            current_event.eid = None
            return_failure()
        add_output('Event #' + str(result) + ' has been posted. \n')
        current_event.eid = result

        result = EventController.host_event(current_user, current_event)
        if result == Errors.DUPLICATE.name:
            current_event.eid = None
            add_output("You have already hosted this event. \n")
        elif result == Errors.FAILURE.name:
            current_event.eid = None
            return_failure()
        add_output("You are the host of event " + str(current_event.eid) + " now. \n")
        current_event.hosts = current_user.uid
        current_user.host_events.append(current_event.eid)
        print('User #' + current_event.hosts + ' posted event #' + str(current_event.eid) + '. \n')
        EventController.print_event(current_event)
    return


def update_event():
    global current_event
    global current_user
    event_id = event_id_input.get()
    current_event = read_event()
    current_event.eid = event_id
    host_id = None
    temp_event = EventController.retrieve_event(event_id)
    if temp_event == Errors.MISSING.name:
        add_output('No such event. \n')
        current_event = None
        return
    if type(temp_event) == type(current_event):
        host_id = str(EventController.retrieve_event(event_id).hosts)
    if current_user.uid != host_id:
        add_output('You have to be the owner to update event #' + event_id + ' . \n')
        current_event = None
        return

    result = EventController.edit_event(current_event)

    if result == Errors.MISSING.name:
        add_output('No such event exists. \n')
        current_event = None
        EventController.print_event(current_event)
        return
    elif result == Errors.SUCCESS.name:
        add_output('Event #' + event_id + ' changed. \n')
        current_event = EventController.retrieve_event(event_id)
        EventController.print_event(current_event)
    else:
        add_output('Update failed, please try again. \n')
        current_event = None
        EventController.print_event(current_event)
        return


def remove_user():
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
        add_output('You have to be the host to remove attendees. \n')
        current_event = None
        return

    user_id = user_id_input.get()
    result = EventController.remove_user(user_id, current_event)
    if result == Errors.MISSING.name:
        add_output('User did not attend. \n')
        current_event = None
        return
    elif result == Errors.FAILURE.name:
        return_failure()
        current_event = None
        return
    add_output('User #' + result[0] + ' removed from event #' + result[1] + '. \n')
    return


def register(data):
    user = UserModel(0, data['name'], data['nickname'], data['gender'], data['email'], data['location'],
                     stringToEnum(data['tags']).name, data['description'], [], [], data['image'], data['google_id'])
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


def update_profile():
    global current_user
    if not current_user:
        add_output("You have to login first! \n")
        return
    temp = UserController.retrieve_user(UserFields.email.name, current_user.email)
    if temp == Errors.MISSING.name:
        add_output("No user with such credentials exists. \n")
        return
    elif temp == Errors.FAILURE.name:
        return_failure()
        return
    user_id = current_user.uid
    current_user = read_user()
    current_user.uid = user_id

    result = UserController.edit_user(current_user)
    if result == Errors.MISSING.name:
        add_output("No user with such credentials exists. \n")
        current_user = temp
    elif result == Errors.FAILURE.name:
        return_failure()
        current_user = temp
    elif result == Errors.DUPLICATE.name:
        add_output("A user with the same credentials already exists! \n")
        current_user = temp
    else:
        add_output("User updated. Email now at: " + current_user.email + ". \n")
        current_user = UserController.retrieve_user(UserFields.userid.name, result)
    UserController.print_user(current_user)
    return


def login(email):
    result = UserController.retrieve_user(UserFields.googleid.name, email)
    return result


def log_out():
    global current_user
    current_user = None
    text.set(value="This is the first iteration demo for JoinMe. \n")


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


def return_failure():
    add_output("Connection failed. Please try again. \n")


# TODO: Replace with sending real email
def send_email(message: str, address: str):
    add_output('Message: ' + message + ' send to ' + address + '. \n')


def join_event():
    global current_event
    global current_user
    event_id = event_id_input.get()
    current_event = EventController.retrieve_event(event_id)
    if current_event == Errors.MISSING.name:
        add_output('Event not found. \n')
        current_event = None
        return
    elif current_event == Errors.FAILURE.name:
        add_output('Failed to join event. \n')
        current_event = None
        return
    if not current_user:
        add_output('You have to login first to join events. \n')
        current_event = None
        return

    result = EventController.join_event(current_user, current_event)
    if result == Errors.DUPLICATE.name:
        add_output('You have already joined the event. \n')
    elif result == Errors.FAILURE.name:
        return_failure()
        current_event = None
        return
    else:
        add_output('You have joined event #' + current_event.eid + '. User ID: ' + current_user.uid + '. \n')

    EventController.print_event(current_event)
    return


def stringToEnum(tags_input):
    check_set = set(['sports', 'social', 'outdoors', 'indoors', 'sightseeing',
                     'exhibitions', 'entertaining', 'charity', 'business'])
    if tags_input not in check_set:
        tags_input = 'anything'
    return Tags[tags_input]
