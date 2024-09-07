import sqlite3

conn = sqlite3.connect('sqlite_python.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
)""")

c.execute("""CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PR