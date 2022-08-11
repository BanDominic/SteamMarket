import subprocess
import sqlite3
from datetime import datetime


conn = sqlite3.connect('raspberry_pi.db')
cursor = conn.cursor()

command = ['vcgencmd', 'measure_temp']
cpu_temp_value = subprocess.run(command, stdout=subprocess.PIPE).stdout.decode('utf-8')[5:-3]

query = f"""
    INSERT INTO cpu_temp(datetime, temp)
    VALUES ('{datetime.now()}', '{cpu_temp_value}');
"""

cursor.execute(query)
conn.commit()
conn.close()

