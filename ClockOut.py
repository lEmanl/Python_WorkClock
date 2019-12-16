from datetime import datetime
import sqlite3

from DBUtils import db_connect, update_active_workclock

def db_user_clockout(user_name, description):

    now = datetime.now()
    time_end = now.strftime("%H:%M:%S")
    clockout_message = f"{user_name} clocked out at: {time_end}"

    #   Gets active work clocks to see if any sessions are active
    connection = db_connect()

    update_active_workclock(connection, user_name, description, time_end)

    connection.commit()
    connection.close()

    return clockout_message