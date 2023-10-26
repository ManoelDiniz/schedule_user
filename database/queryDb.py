from database.createDb import *     
def registeruser( name,login, passw):
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
        return result[0]  
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
def getNameUser(user):
    cursor.execute("""
    SELECT nome FROM Login WHERE id=?
    """, (user,))
    result = cursor.fetchone()
    
    if result is not None:
        return result[0]  
    else:
        return None
def getTask(name_task, user):
    cursor.execute("SELECT id FROM task where name_task=? and userId= ?", (name_task,user))
    result = cursor.fetchone()
    
    if result is not None:
        return result[0]  
    else:
        return None

def createTask(name_task, dat_task, descri, user,id_level):
    cursor.execute(
        "INSERT INTO task (userId, name_task, description, dat_task,priority_levels) VALUES (?, ?, ?, ?,?)",
        (user, name_task, descri, dat_task,id_level)
    )
    conn.commit()
def createNivels(namep, nivel, emoji):
    cursor.execute("""
                   INSERT INTO levels(name_levels,nivel_levels,emojis) VALUES  (?,?,?)
                   """,(namep, nivel, emoji))
    conn.commit()
def getNivel(namep):
    cursor.execute("SELECT id FROM levels WHERE name_levels=?", (namep,))

    result = cursor.fetchone()
    
    if result is not None:
        return result[0]  
    else:
        return None
    
def getNivelL():
    cursor.execute("""
        SELECT name_levels FROM levels
    """)
    results = cursor.fetchall()
    return [result[0] for result in results]

def get():
    cursor.execute("""
        SELECT name_levels,nivel_levels FROM levels order by nivel_levels asc
    """)
    results = cursor.fetchall()
    return results