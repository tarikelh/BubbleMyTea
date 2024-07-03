import sqlite3

def is_email_unique(email, user_id):
    query = "SELECT COUNT(*) FROM app_user WHERE email = ? AND id != ?"
    with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute(query, (email, user_id))
        count = cursor.fetchone()[0]
    return count == 0