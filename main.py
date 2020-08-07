import sqlite3 as db

def init():
    # Initialize a new database to store the expenditures

    # Connect the database 
    connectDB = db.connect("spend.db")

    # This will enable us to create queries in our database
    cursor = connectDB.cursor()
    
    # create table command
    sql = ''' CREATE TABLE IN NOT EXISTS expenses (
        amount number,
        category string,
        message string,
        date string 
    )'''

    # execute the command
    cursor.execute(sql)

    # To store that information permanently
    connectDB.commit()


def log(amount, category, message = '' ):
    # this function logs the expenditure in the database.
    # amount : number
    # category : string
    # messsage : (optional) string

    # Initializing the date
    # import the datetiem module
    from datetime import datetime
    date = str(datetime.now())
    # Connect the database 
    connectDB = db.connect("spend.db")

    # This will enable us to create queries in our database
    cursor = connectDB.cursor()
    
    # create table command
    sql = ''' INSERT INTO expenses VALUES (
         {},
        '{}',
        '{}',
        '{}'
    )'''.format(amount, category, message, date)

    # execute the command
    cursor.execute(sql)

    # To store that information permanently
    connectDB.commit()
    
log(120, "transport", "naglakad lang talaga ako")