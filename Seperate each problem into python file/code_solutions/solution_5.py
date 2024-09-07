import sqlite3

conn = sqlite3.connect('mydb.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS mytable (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
)""")

c.execute("INSERT INTO mytable (name, age, gender) VALUES ('John', 30, 'Male')