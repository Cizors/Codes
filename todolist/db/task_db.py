from utils import connection_db

@connection_db
def insert_task(cursor, title, user_id):
    sql = 'INSERT INTO tasks (title, user_id) VALUES (?, ?)'
    return cursor.execute(sql, [title, user_id])

@connection_db
def update_task(cursor, title, task_id, user_id):
    sql = 'UPDATE tasks SET title=? WHERE id=? AND user_id=?'
    return cursor.execute(sql, [title, task_id, user_id])

@connection_db
def delete_task(cursor, task_id, user_id):
    sql = 'DELETE FROM tasks WHERE id=? AND user_id=?'
    return cursor.execute(sql, [task_id, user_id])

@connection_db
def list_tasks(cursor, user_id):
    sql = 'SELECT * FROM tasks WHERE user_id=?'
    return cursor.execute(sql, [user_id]).fetchall()


@connection_db
def search_task(cursor, title):
    sql = 'SELECT * FROM tasks WHERE title LIKE ?'
    return cursor.execute(sql, [f'%{title}%']).fetchall()
