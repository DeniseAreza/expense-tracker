import sqlite3

def expenses():
    # create connection

    connection = sqlite3.connect('money.db')

    # create cursor

    cursor = connection.cursor()

    # create table

    expenses = """CREATE TABLE IF NOT EXISTS
    expenses(amount FLOAT, category TEXT, message TEXT, date TEXT)"""

    cursor.execute(expenses)
    

def log(amount, category, message = ''):
    # the inserting command must be here in this function
    # amount : text
    # category : text
    # message : text
    # date : text

    # import datetime module
    from datetime import datetime
    date = str(datetime.now())

    # connect to database

    connection = sqlite3.connect("money.db")

    # create a cursor

    cursor = connection.cursor()

    # insert values to the table

    sql = """
    INSERT INTO expenses (amount, category, message, date) VALUES (
        ?,
        ?,
        ?,
        ?
    )"""
    cursor.execute(sql)

    # get results

    cursor.execute('SELECT * FROM expenses')

    results = cursor.fetchall()

    print(results)

