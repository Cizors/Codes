import sqlite3
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()
sql = 'INSERT INTO users(username, password) VALUES (?, ?)'
cursor.execute(sql, ['Usuario_1', 'Minha Senha'])
conn.commit()
cursor.execute(sql, ['Usuario_2', 'Minha Senha2'])
conn.commit()