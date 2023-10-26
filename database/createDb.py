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
     salt = bcrypt.gensalt(8)

     
     password = passw.encode('utf-8')

     # Crie o hash da senha com o salt
     hashed_password = bcrypt.hashpw(password, salt)
     cursor.execute("""
                   INSERT INTO Login( nome, login, Password ) VALUES (?,?,?)
                   """,(name, login, hashed_password))
     conn.commit()
def userExist(login):
    
    cursor.execute("""
    SELECT id FROM Login WHERE login=?
    """, (login,))
    result = cursor.fetchone()
    
    if result is not None:
        return result[0]  # Retorna o ID do usuário
    else:
        return None 
    
def getPassword(user):
     
    cursor.execute("""
                SELECT Password FROM Login WHERE id=?
                """,(user,))
    getpass =cursor.fetchone()
    password_byte = getpass[0]
    result = password_byte.decode('utf-8')
    return result