import sqlite3

class DBManager:
    def __init__(self, db_name='passwords.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, site TEXT, username TEXT, password TEXT)"
            )

    def add_password(self, site, username, password):
        with self.conn:
            self.conn.execute(
                "INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)",
                (site, username, password)
            )

    def get_passwords(self):
        with self.conn:
            cursor = self.conn.execute("SELECT id, site, username, password FROM passwords")
            return cursor.fetchall()

    def update_password(self, id, password):
        with self.conn:
            self.conn.execute(
                "UPDATE passwords SET password = ? WHERE id = ?",
                (password, id)
            )

    def delete_password(self, id):
        with self.conn:
            self.conn.execute("DELETE FROM passwords WHERE id = ?", (id,))
