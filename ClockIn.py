import sqlite3

from datetime import datetime
from DBUtils import db_connect, create_workclock, select_active_workclock

def db_user_clockin(user_name, description):

    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time_start = now.strftime("%H:%M:%S")
    time_end = now.strftime("%H:%M:%S")
    session_active = 1
    clockin_message = f"{user_name} clocked in at: {time_start}"

    #   Creates a new workclock
    connection = db_connect()

    active_workclock = select_active_workclock(connection, user_name)

    if(not active_workclock):
        create_workclock(connection, description, date, time_start, time_end, session_active, user_name)
    else:
        clockin_message = "Clock out of current active session before clocking in"

    connection.commit()
    connection.close()

    return clockin_message