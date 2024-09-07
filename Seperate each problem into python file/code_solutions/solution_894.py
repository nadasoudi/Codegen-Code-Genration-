import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER, name TEXT, dob DATE, address TEXT, phone INTEGER, email TEXT, website TEXT, password TEXT)')

c.execute('INSERT INTO data VALUES (1, "Raj", "2021-05-05", "Rajesh", "09