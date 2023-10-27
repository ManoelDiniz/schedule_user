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
                priority_levels INTEGER,
                FOREIGN KEY (userId) REFERENCES login(id)
                FOREIGN KEY (priority_levels) REFERENCES levels(id)
                );
                """)
cursor.execute("""
                 CREATE TABLE IF NOT EXISTS levels (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name_levels TEXT,
                     nivel_levels INTEGER,
                     emojis TEXT
                     
                 )
               """)
cursor.execute("""
                 CREATE TABLE IF NOT EXISTS taskfinish (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     taskId TEXT,
                     dat_finish text, 
                     Flg_finish integer,  
                     FOREIGN KEY (taskId) REFERENCES task(id)                 
                 )
               """)

cursor.execute("""
    CREATE TRIGGER IF NOT EXISTS task_insert_trigger
    AFTER INSERT ON task
    FOR EACH ROW
    BEGIN
        INSERT INTO taskfinish (taskId, Flg_finish)
        VALUES (NEW.id, '0');
    END;
""")

cursor.execute("""
CREATE VIEW IF NOT EXISTS task_view AS
SELECT t.id, l.nome, t.userId ,t.name_task, t.description, t.priority_levels, a.dat_finish, a.Flg_finish
FROM task AS t
INNER JOIN login AS l ON l.id = t.userId
INNER JOIN taskfinish AS a ON t.id = a.taskId
""")


conn.commit()
