import mysql.connector
import ast
from Model.UserModel import UserModel
from Controller.SqlController import SqlController
from Constants.Constants import Errors


def add_user(user: UserModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    handled = False

    sql = "INSERT INTO user " \
          "(realname, nickname, gender, location, email, tags, selfdescription, googleid, image) " \
          "VALUES " \
          "(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user.name, user.nickname, user.gender,
           user.location, user.email, user.tags, user.description, user.google_id, user.image)
    try:
        cursor.execute(sql, val)
        connector.commit()
        handled = True
        return Errors.SUCCESS.name
    except mysql.connector.errors.IntegrityError as err:
        if not handled:
            handled = True
            return Errors.DUPLICATE.name
    finally:
        connector.rollback()


def edit_user(user: UserModel):
    handled = False
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "UPDATE user " \
          "SET realname = %s, nickname = %s, gender = %s, location = %s, " \
          "email = %s, tags = %s, selfdescription = %s, image = %s" \
          "WHERE googleid = %s"

    val = (user.name, user.nickname, user.gender, user.location, user.email,
           user.tags, user.description, user.image, user.google_id)
    try:
        cursor.execute(sql, val)
        connector.commit()
        if cursor.rowcount == 0:
            handled = True
            return Errors.MISSING.name
        else:
            handled = True
            return user.uid
    except mysql.connector.errors.IntegrityError as err:
        print(err.msg)
        if not handled:
            handled = True
            return Errors.DUPLICATE.name
    finally:
        connector.rollback()
        if not handled:
            return Errors.FAILURE.name


def retrieve_user(field: str, value: str):
    handled = False
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "SELECT * " \
          "FROM user " \
          "WHERE {field} = %s".format(field=field)
    val = [value]

    try:
        cursor.execute(sql, val)
        user_info = cursor.fetchone()
        if not user_info:
            handled = True
            return Errors.MISSING.name
        else:
            handled = True
            return_user = decode_string(str(user_info))
            return_user.join_events = get_join(return_user.uid)
            return_user.host_events = get_host(return_user.uid)
            return return_user
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name


def decode_string(user_info: str):
    user_info = user_info[1: -1]
    user_info = '[' + user_info + ']'
    user_info = ast.literal_eval(user_info)
    name = user_info[0]
    nickname = user_info[1]
    gender = user_info[2]
    location = user_info[3]
    email = user_info[4]
    tags = user_info[5]
    description = user_info[6]
    uid = user_info[7]
    image = user_info[8]
    google_id = user_info[9]
    decoded_user = UserModel(uid, name, nickname, gender, email, location, tags, description, [], [], image, google_id)
    return decoded_user


def delete_user(user_nick_name: str, user_email: str):
    handled = False
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "DELETE " \
          "FROM user " \
          "WHERE nickname = %s AND email = %s"
    val = (user_nick_name, user_email)
    try:
        cursor.execute(sql, val)
        connector.commit()
        handled = True
        return "SUCCESS"
    except mysql.connector.errors as err:
        print(err.msg)
    finally:
        if not handled:
            connector.rollback()
            return Errors.FAILURE.name


def print_user(user: UserModel):
    if not user:
        print('This user is empty. ')
        print()
        return
    print('user id: ' + str(user.uid))
    print('real name: ' + user.name)
    print('nickname: ' + user.nickname)
    print('gender: ' + user.gender)
    print('location: ' + user.location)
    print('email: ' + user.email)
    print('tags: ' + user.tags)
    print('description: ' + user.description)
    print('hosted: ' + str(user.host_events))
    print('joined: ' + str(user.join_events))
    print('image: ' + str(user.image))
    print('google id: ' + str(user.google_id))
    print()
    return


def get_host(user_id: str):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    result = []

    sql = 'SELECT EventID '\
          'FROM Host ' \
          'WHERE HostID = %s'
    val = [user_id]

    try:
        cursor.execute(sql, val)
        hosts = cursor.fetchall()
        for host in hosts:
            result.append(str(host[0]))
        got = True
        return result
    finally:
        if not got:
            return []


def get_join(user_id: str):
    connector = SqlController().sql_connector
    cursor = connector.cursor()
    got = False
    result = []

    sql = 'SELECT EventID '\
          'FROM JoinTable ' \
          'WHERE JoinID = %s'
    val = [user_id]

    try:
        cursor.execute(sql, val)
        joins = cursor.fetchall()
        for attendee in joins:
            result.append(str(attendee[0]))
        got = True
        return result
    finally:
        if not got:
            return []
