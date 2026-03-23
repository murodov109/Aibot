import sqlite3

class Database:
    def __init__(self, db_name='aibot.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_premium BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usage (
            user_id INTEGER,
            usage_count INTEGER DEFAULT 0,
            last_used TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )''')
        self.connection.commit()

    def add_user(self, username, password, is_premium=False):
        try:
            self.cursor.execute('''INSERT INTO users (username, password, is_premium) VALUES (?, ?, ?)''',
                              (username, password, is_premium))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print('User already exists.')

    def track_usage(self, username):
        self.cursor.execute('''SELECT id FROM users WHERE username = ?''', (username,))
        user = self.cursor.fetchone()
        if user:
            user_id = user[0]
            self.cursor.execute('''INSERT INTO usage (user_id) VALUES (?)
                                  ON CONFLICT(user_id) DO UPDATE SET usage_count = usage_count + 1, last_used = CURRENT_TIMESTAMP''', (user_id,))
            self.connection.commit()

    def close(self):
        self.connection.close()