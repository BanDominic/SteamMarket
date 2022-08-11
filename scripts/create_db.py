import sqlite3

db = sqlite3.connect("raspberry_pi.db")
cursor = db.cursor()

cursor.exectute('''
CREATE TABLE cpu_temp
(
    datetime TEXT,
    temp REAL
);
''')

db.commit()
db.close()