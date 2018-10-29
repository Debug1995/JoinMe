import mysql.connector
from flask import Blueprint
from Model.UserModel import UserModel
from Controller.SqlController import SqlController


user_controller = Blueprint('user_controller', __name__)


@user_controller.route("/Controller")
def add_user(user: UserModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "INSERT INTO user " \
          "(realname, nickname, gender, location, email, tags, selfdescription) " \
          "VALUES " \
          "(%s, %s, %s, %s, %s, %s,%s)"
    val = (user.name, user.nickname, user.gender,
           user.location, user.email, user.tags, user.description)
    try:
        cursor.execute(sql, val)
        connector.commit()
        return 'Success'
    except mysql.connector.errors.IntegrityError as err:
        return err.msg
    finally:
        connector.rollback()
        return 'Connection Failure'


@user_controller.route("/Controller")
def edit_user(user: UserModel):
    connector = SqlController().sql_connector
    cursor = connector.cursor()

    sql = "UPDATE user " \
          "SET realname = %s, nickname = %s, gender = %s, location = %s, " \
          "email = %s, tags = %s, selfdescription = %s " \
          "WHERE email = %s"

    val = (user.name, user.nickname, user.gender, user.location, user.email,
           user.tags, user.description, user.email)
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


@user_controller.route("/Controller")
def retrieve_user(field: str, value: str):
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
            return 'Record Not Found'
        return str(user_info)
    except mysql.connector.errors as err:
        return err.msg
    finally:
        connector.rollback()
        return 'Connection Failure'

