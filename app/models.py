from app import mysql
from werkzeug.security import generate_password_hash, check_password_hash

def insert_user(name, email, password):
    hashed_pw = generate_password_hash(password)  # hash password for security
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)",
        (name, email, hashed_pw)
    )
    mysql.connection.commit()
    cur.close()

def validate_user(email, password):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cur.fetchone()
    cur.close()
    if user and check_password_hash(user[3], password):  # user[3] = password column
        return user
    return None
