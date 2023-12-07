import sqlite3
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
sql = '''CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   username varchar(255),
   password varchar(255)
)'''

cursor.execute(sql)

sql = '''CREATE TABLE IF NOT EXISTS tasks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title varchar(255),
  user_id INTEGER,
  FOREIGN KEY (user_id) REFERENCES user(id)
)'''

cursor.execute(sql)