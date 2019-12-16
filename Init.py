import sqlite3

from DBUtils import db_connect

def db_init():
    connection = db_connect()
    cursor = connection.cursor()
    
    employees_sql = """
    CREATE TABLE employees (
        user_name text PRIMARY KEY UNIQUE,
        company text NOT NULL,
        first_name text NOT NULL,
        last_name text NOT NULL,
        job_title text NOT NULL
    )"""

    cursor.execute(employees_sql)

    workclocks_sql = """
    CREATE TABLE workclocks (
        id integer PRIMARY KEY,
        description text NOT NULL,
        date text NOT NULL,
        time_start integer NOT NULL,
        time_end integer NOT NULL,
        session_active integer NOT NULL,
        user_name text,
        FOREIGN KEY (user_name) REFERENCES employees (user_name)
    )"""

    cursor.execute(workclocks_sql)

    connection.commit()
    connection.close()