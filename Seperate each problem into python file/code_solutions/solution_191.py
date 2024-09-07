import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS data')

c.execute('CREATE TABLE data (id INTEGER, name TEXT, address TEXT, phone_number TEXT, email TEXT)')

c.execute('INSERT INTO data VALUES (1, "Rajesh", "Delhi", "09123445566", "rajesh@gmail.com