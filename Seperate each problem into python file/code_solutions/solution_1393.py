import sqlite3

conn = sqlite3.connect('sqlite_python.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text,
    password text
)""")

c.execute("INSERT INTO users VALUES (1, 'bob','secret')")
c.execute("INSERT INTO users VALUES (2, '