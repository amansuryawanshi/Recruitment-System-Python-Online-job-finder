import sqlite3 as lite

conn = lite.connect('db/Form.db')
cur = conn.cursor()

def get_posts():
    with conn:
        cur.execute("SELECT * FROM Posts")
        print(cur.fetchall())

get_Form()
