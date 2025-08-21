import MySQLdb
import os

host = os.environ['DB_HOST']
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']

conn = MySQLdb.connect(
    host=host,
    user=user,
    passwd=password,
    db=db_name
)
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        password VARCHAR(100)
    );
''')

conn.commit()
cur.close()
conn.close()
