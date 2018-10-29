from Controller.SqlController import *
from Model.EventModel import EventModel
from Model.UserModel import UserModel
import datetime


def calculate_date(initial_date, register_period):
    cur_date = [int(x) for x in initial_date.strip().split('-')]
    d1 = datetime.date(cur_date[0], cur_date[1], cur_date[2])
    d = d1 + datetime.timedelta(days=int(register_period))
    year = str(d.year)
    month = str(d.month).zfill(2)
    date = str(d.day).zfill(2)
    return year + '-' + month + '-' + date


def post_event(user: UserModel, event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "INSERT INTO event " \
          "(Title, Tags, eventdate, description, image, location, expiretime) " \
          "VALUES " \
          "(%s, %s, %s, %s, %s, %s,%s)"
    val = (event.title, event.tags, event.event_date,
           event.description, event.image, event.location, event.expire_date)
    try:
        cursor.execute(sql, val)
        connector.commit()
    except mysql.connector.errors.IntegrityError as err:
        return err.msg

    cursor.execute("SELECT @@identity")
    for x in cursor:
        event_id = x[0]

    sql = "INSERT INTO host (hostid, eventid)" \
          "VALUES(%s, %s)"
    val = (user.uid, event_id)

    try:
        cursor.execute(sql, val)
        connector.commit()
        return event_id
    except mysql.connector.errors.IntegrityError as err:
        return err.msg
    finally:
        connector.rollback()
        return 'Connection Failure'


def edit_event(event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "UPDATE event " \
          "SET title = %s, tags = %s, eventdate = %s, description = %s, " \
          "image = %s, location = %s, expiretime = %s " \
          "WHERE eventid = %s"
    val = (event.title, event.tags, event.event_date, event.description, event.image,
           event.location, event.expire_date, event.eid)
    try:
        cursor.execute(sql, val)
        connector.commit()
        if cursor.rowcount == 0:
            return 'Record Not Found'
        else:
            return 'Success'
    finally:
        connector.rollback()
        return 'Connection Failure'


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
        return "Connection Failure"


def remove_user(user: UserModel, event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "DELETE FROM joins WHERE joinid = %s and eventid = %s"
    val = (user.uid, event.eid)
    try:
        cursor.execute(sql, val)
        connector.commit()
        return cursor.rowcount
    finally:
        connector.rollback()
        return "Connection Failure"


def join_event(user: UserModel, event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "INSERT INTO joins (joinid, eventid)" \
          "VALUES(%s, %s)"
    val = (user.uid, event.eid)

    try:
        cursor.execute(sql, val)
        connector.commit()
        event.attendees.append(user.uid)
        user.join_events.append(event.eid)
        return user.uid, event.eid
    except mysql.connector.errors.IntegrityError as err:
        return err.msg
    finally:
        connector.rollback()
        return 'Connection Failure'


def host_event(user: UserModel, event: EventModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "INSERT INTO host (hostid, eventid)" \
          "VALUES(%s, %s)"
    val = (user.uid, event.eid)

    try:
        cursor.execute(sql, val)
        connector.commit()
        event.hosts.append(user.uid)
        user.host_events.append(event.eid)
        return user.uid, event.eid
    except mysql.connector.errors.IntegrityError as err:
        return err.msg
    finally:
        connector.rollback()
        return 'Connection Failure'

def get_event(user: UserModel, event: EventModel):

