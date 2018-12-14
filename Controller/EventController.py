from Controller.SqlController import *
from Model.EventModel import EventModel
from Model.UserModel import UserModel
from Constants.Constants import Errors
import datetime


def add_event(event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    handled = False

    sql = "INSERT INTO event " \
          "(title, tags, eventdate, description, image, location, expiretime, city) " \
          "VALUES " \
          "(%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (event.title, event.tags, event.event_date,
           event.description, event.image, event.location, event.expire_date, event.address)
    try:
        cursor.execute(sql, val)
        connector.commit()
        handled = True
    except mysql.connector.errors.IntegrityError as err:
        print(err.msg)
        handled = True
        return Errors.DUPLICATE.name
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name

    cursor.execute("SELECT @@identity")
    for x in cursor:
        event_id = x[0]
    return event_id


def edit_event(event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    handled = False

    sql = "UPDATE event " \
          "SET title = %s, tags = %s, eventdate = %s, description = %s, " \
          "image = %s, location = %s, expiretime = %s, city = %s" \
          "WHERE eventid = %s"
    val = (event.title, event.tags, event.event_date, event.description, event.image,
           event.location, event.expire_date, event.address, event.eid)

    try:
        cursor.execute(sql, val)
        connector.commit()
        if cursor.rowcount == 0:
            handled = True
            return Errors.MISSING.name
        else:
            handled = True
            return Errors.SUCCESS.name
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name


def expire():
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    today = datetime.date.today()
    cur_year = str(today.year)
    cur_month = str(today.month).zfill(2)
    cur_day = str(today.day).zfill(2)
    expire_date = cur_year+'-'+cur_month+'-'+cur_day
    sql = "DELETE FROM event WHERE expiretime < %s"
    val = [expire_date]
    try:
        cursor.execute(sql, val)
        connector.commit()
        return cursor.rowcount
    finally:
        connector.rollback()
        return Errors.FAILURE.name


def remove_user(data):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    handled = False

    sql = "DELETE FROM JoinTable WHERE JoinID = %s and EventID = %s"
    val = (data['uid'], data['eid'])
    try:
        cursor.execute(sql, val)
        connector.commit()
        handled = True
        if cursor.rowcount == 0:
            return Errors.MISSING.name
        else:
            return data['uid'], data['eid']
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name


def join_event(data):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    handled = False

    sql = "INSERT INTO JoinTable (JoinID, EventID)" \
          "VALUES (%s, %s)"
    val = (data['uid'], data['eid'])

    try:
        cursor.execute(sql, val)
        connector.commit()
        handled = True
        return 'OK'
    except mysql.connector.errors.IntegrityError as err:
        print(err.msg)
        handled = True
        return Errors.DUPLICATE.name
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name


def host_event(uid, event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    handled = False

    sql = "INSERT INTO Host (hostid, eventid)" \
          "VALUES(%s, %s)"
    val = (uid, event.eid)

    try:
        cursor.execute(sql, val)
        connector.commit()
        handled = True
        return event.eid, uid
    except mysql.connector.errors.IntegrityError as err:
        if not handled:
            print(err.msg)
            handled = True
            return Errors.DUPLICATE.name
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name


def get_hosted_event(user: UserModel):
    events = []
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    sql = "SELECT eventid " \
          "FROM host "\
          "WHERE hostid = %s"
    val = [user.uid]

    try:
        cursor.execute(sql, val)
        event_list = cursor.fetchone()
        if not event_list:
            return events
        for result in event_list:
            events.append(result[0])
        return events
    except mysql.connector.errors as err:
        print(err.msg)
        return Errors.FAILURE.name
    finally:
        connector.rollback()
        return Errors.FAILURE.name


def retrieve_event(event_id: str):
    handled = False
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "SELECT * " \
          "FROM event " \
          "WHERE eventid = %s"
    val = [int(event_id)]

    try:
        cursor.execute(sql, val)
        event_info = cursor.fetchone()
        if not event_info:
            handled = True
            return Errors.MISSING.name
        else:
            handled = True
            return_event = decode_string_event(str(event_info))
            return_event.hosts = get_host(return_event.eid)
            return_event.attendees = get_join(return_event.eid)
            print(return_event.attendees)
            return return_event
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name


def decode_string_event(event_info: str):
    event_info = event_info[1: -1]
    event_info = '[' + event_info + ']'
    field_list = eval(event_info)
    print(field_list)
    eid = field_list[0]
    event_title = field_list[1]
    tags = field_list[2]
    event_date = str(field_list[3])
    description = field_list[4]
    image = field_list[5]
    location = field_list[6]
    expire_date = str(field_list[7])
    address = field_list[8]

    decoded_event = EventModel(eid, event_title, tags, description, image, None,
                               [], event_date, location, address, 0)
    decoded_event.expire_date = expire_date
    return decoded_event


def print_event(event: EventModel):
    if not event:
        print('This event is empty. \n')
    if type(event) == str:
        print(event)
        print()
    else:
        print('eid: ' + str(event.eid))
        print('title: ' + event.title)
        print('tags: ' + event.tags)
        print('description: ' + event.description)
        print('image: ' + event.image)
        print('hosts: ' + str(event.hosts))
        print('attendees: ' + str(event.attendees))
        print('event date: ' + event.event_date)
        print('location: ' + event.location)
        print('expire date: ' + event.expire_date)
        print()


def get_host(event_id: str):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    got = False

    sql = 'SELECT HostID '\
          'FROM Host ' \
          'WHERE EventID = %s'
    val = [event_id]

    try:
        cursor.execute(sql, val)
        host = cursor.fetchone()
        got = True
        return str(host[0])
    finally:
        if not got:
            return None


def get_join(event_id: str):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    got = False
    result = []

    sql = 'SELECT JoinID '\
          'FROM JoinTable ' \
          'WHERE EventID = %s'
    val = [event_id]

    try:
        cursor.execute(sql, val)
        join = cursor.fetchall()
        for attendee in join:
            result.append(str(attendee[0]))
        got = True
        return result
    finally:
        if not got:
            return []


def get_events(data):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    handled = False
    time = data['time']
    clauses = []
    time_clause = "expiretime > \'" + datetime.datetime.today().strftime('%Y-%m-%d') + "\'"
    if time:
        time_clause = "(" + time_clause + " AND DATEDIFF(expiretime, \'" + \
                      datetime.datetime.today().strftime('%Y-%m-%d') + "\') < " + str(time) + ")"
    clauses.append(time_clause)
    state = data['state']
    if state:
        state_clause = 'location = \'' + state + "\'"
        clauses.append(state_clause)
    tag = data['tag']
    if tag:
        tag_clause = "tags = \'" + tag + "\'"
        clauses.append(tag_clause)
    keyword = data['keyword']
    if keyword:
        keyword_clause = "(description LIKE \'%" + keyword + "%\'" + " OR " + "title LIKE \'%" + keyword + "%\')"
        clauses.append(keyword_clause)
    query = ''
    for clause in clauses:
        query = query + clause + ' AND '
    query = query[: -5]

    sql = 'SELECT eventid, title, location, expiretime, image ' \
          'FROM event ' \
          'WHERE ' + query
    try:
        cursor.execute(sql)
        result_list = cursor.fetchall()
        handled = True
        return Errors.SUCCESS.name, result_list
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name, None
