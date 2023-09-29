# Initialize SQLite database connection
import sqlite3


def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


def register_user(username, password, role):
    conn = get_db()
    conn.execute('insert into users (username, password, role) values (?, ?, ?)', (username, password, role))
    conn.commit()
    conn.close()


def get_user_by_username(username):
    conn = get_db()
    user =  conn.execute("select * from users where username = ?", (username,)).fetchone()
    conn.close()
    return user