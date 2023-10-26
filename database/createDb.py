import sqlite3 as db
import bcrypt

conn = db.connect("estudo.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Login (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        login TEXT,
        Password TEXT
    )
""")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS task (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                userId INTEGER,
                name_task TEXT,
                dat_creat TEXT DEFAULT CURRENT_TIMESTAMP,
                description TEXT,
                dat_task TEXT,
                FOREIGN KEY (userId) REFERENCES login(id)
                );
                """)


