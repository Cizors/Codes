import sqlite3
from utils import connection_db

@connection_db
def login(cursor, username):
    # Not Good - Deveriamos receber o password e descriptografar aqui
    sql = 'SELECT * FROM users WHERE username=? '
    return cursor.execute(sql, [username]).fetchone()

@connection_db
def create_user(cursor, username, password):
    sql = 'INSERT INTO users(username, password) VALUES (?, ?)'
    return cursor.execute(sql, [username, password])
