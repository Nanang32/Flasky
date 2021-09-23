import sqlite3

connection = sqlite3.connect("users.sqlite")

cursor = connection.cursor()
sql = """ CREATE TABLE akun(
        id integer PRIMARY KEY,
        username text NOT NULL,
        password text NOT NULL,
        email text NOT NULL
)"""

cursor.execute(sql)