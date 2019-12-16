import sqlite3
import os

#   Default file path for sqlite database file
DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

#   Connects to our data base file
def db_connect(db_path=DEFAULT_DB_PATH):
    connection = sqlite3.connect(db_path)
    return connection

#   Query to create an employee in our sqlite db
def create_employee(connection, user_name, company, first_name, last_name, job_title):
    sql = """
        INSERT INTO employees (user_name, company, first_name, last_name, job_title)
        VALUES (?, ?, ?, ?, ?)"""
    cursor = connection.cursor()
    cursor.execute(sql, (user_name, company, first_name, last_name, job_title))
    return cursor.lastrowid

#   Query to create an employee in our sqlite db
def create_workclock(connection, description, date, time_start, time_end, session_active, user_name):
    sql = """
        INSERT INTO workclocks (description, date, time_start, time_end, session_active, user_name)
        VALUES (?, ?, ?, ?, ?, ?)"""
    cursor = connection.cursor()
    cursor.execute(sql, (description, date, time_start, time_end, session_active, user_name))
    return cursor.lastrowid

#   Query to get an active workclock for user
def select_active_workclock(connection, user_name):
    select_sql = f"SELECT session_active FROM workclocks WHERE session_active = 1 AND user_name = '{user_name}'"
    cursor = connection.cursor()
    cursor.execute(select_sql)

    return cursor.fetchone()

#   Update active workclock of user
def update_active_workclock(connection, user_name, description, time_end):
    update_sql = f"UPDATE workclocks SET description = ?, time_end = ?, session_active = ? WHERE session_active = 1 AND user_name = '{user_name}'"
    cursor = connection.cursor()
    cursor.execute(update_sql, (description, time_end, 0))

    return cursor.fetchone()