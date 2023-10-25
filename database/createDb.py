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


def registeruser(login, name, passw):
     salt = bcrypt.gensalt()

     
     password = passw.encode('utf-8')

     # Crie o hash da senha com o salt
     hashed_password = bcrypt.hashpw(password, salt)
     cursor.execute("""
                   INSERT INTO Login( nome, login, Password ) VALUES (?,?,?)
                   """,(name, login, hashed_password))
     conn.commit()
def userExist(login):
    cursor.execute("""
                   SELECT login FROM Login WHERE login=?
                   """,(login))
    return cursor.fetchone()
    
def getPassword(login):
     cursor.execute("""
                   SELECT Password FROM Login WHERE login=?
                   """,(login))
     return cursor.fetchone()