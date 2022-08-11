import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from datetime import date, timedelta

plt.style.use('ggplot')

conn = sqlite3.connect('cpu_temp_monitor.db')

df = pd.read_sql_query(con=conn, sql='SELECT * FROM cpu_temp')

conn.close()

df['datetime'] = pd.to_datetime(df['datetime'])

df = df[df['datetime'].dt.date == date.today()]

g = sns.relplot(
        data=df,
        x='datetime',
        y='temp',
        aspect=4,
        kind='scatter')

ax = plt.gca()
ax.set_xticklabels([str(timedelta(days=(tm % 1))).rsplit(':', 1)[0] for tm in ax.get_xticks()])
plt.title(f'CPU temp -- {date.today()}')
plt.savefig('eloelo.png', bbox_inches='tight')
plt.show()

