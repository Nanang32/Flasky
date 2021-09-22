import sqlite3

connection = sqlite3.connect("phonebook.sqlite")

cursor = connection.cursor()
sql = """ CREATE TABLE pbook(
        id integer PRIMARY KEY,
        namephone text NOT NULL,
        phonenumber number NOT NULL
)"""

cursor.execute(sql)