
def connect():
    import psycopg2

    conn = psycopg2.connect(
        host="192.168.18.108",
        database="steam_market_db",
        user="pi",
        password="************")

    cur = conn.cursor()

    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.close()