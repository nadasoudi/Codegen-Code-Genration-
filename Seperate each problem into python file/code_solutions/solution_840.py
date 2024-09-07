import sqlite3

conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS mytable (
    first_name text,
    last_name text,
    age integer,
    gender text
)""")

c.execute("INSERT INTO mytable VALUES ('John', 'Doe', 25, 'Male')")
c.execute("INSERT INTO mytable VALUES