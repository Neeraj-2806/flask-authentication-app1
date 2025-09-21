from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='../templates')  # 👈 force template path
app.secret_key = os.getenv("SECRET_KEY")

# MySQL Config
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_PORT'] = int(os.getenv("MYSQL_PORT", 3306))
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")

mysql = MySQL(app)

# ✅ Function to auto-create users table
def create_users_table():
    with app.app_context():  # ensure app context for MySQL
        cur = mysql.connection.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            )
        """)
        mysql.connection.commit()
        cur.close()

# Call the function once at startup
create_users_table()

from app import routes
