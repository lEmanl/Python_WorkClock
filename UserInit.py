import sqlite3

from DBUtils import db_connect, create_employee

def db_user_init(user_name):

    #   Prompts and collects employee data
    print("Hello, %s" %(user_name))
    company = input("Company: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    job_title = input("Job Title: ")


    #   Creates new employee
    connection = db_connect()
    new_employee = create_employee(connection, user_name, company, first_name, last_name, job_title)
    connection.commit()
    connection.close()

    return new_employee