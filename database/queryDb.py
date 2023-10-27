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
    cursor.execute("SELECT nivel_levels FROM levels WHERE name_levels=?", (namep,))

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
def getCalendarTask(selected_date,user):
    
    cursor.execute("""
                   SELECT priority_levels, name_task, description,a.Flg_finish,t.id 
                   FROM task 
                   AS T INNER JOIN taskfinish as a on t.id=a.taskId
                   WHERE strftime('%d/%m/%Y', dat_task) = ? and userId=?""", 
                   (selected_date,user))
    
    results = cursor.fetchall()
    return results
def getEditTasks(user):
    
    cursor.execute("""
                   SELECT t.id, priority_levels, name_task, description,a.Flg_finish FROM task as t
                   INNER JOIN taskfinish as a on t.id=a.taskId 
                   where userId=?
                   """,(user,))
    
    results = cursor.fetchall()
    return results

def alterNameTask(name,id,user):
    cursor.execute("""
                   UPDATE TASK SET NAME_TASK=? WHERE ID= ? and userId=?
                   """,(name, id, user,))
    conn.commit()
def alterDescTask(desc,id,user):
    cursor.execute("""
                   UPDATE TASK SET description=? WHERE ID= ? and userId=?
                   """,(desc, id, user,))
    conn.commit()
def alterNivelTask(nivels,id,user):
    cursor.execute("""
                   UPDATE TASK SET priority_levels=? WHERE ID= ? and userId=?
                   """,(nivels, id, user,))
    conn.commit()
def getIdLevel(namep):
    cursor.execute("""
                   select id from levels where name_levels=?
                   """,(namep,))
def alterAllTask(name,desc,nivels,id, user):
    cursor.execute("""
                   UPDATE TASK SET priority_levels=?, description=?,
                   NAME_TASK=?,  WHERE ID= ? and userId=?
                   """,(nivels,desc,name, id, user,))
    conn.commit()
def deleteTask(id):
    cursor.execute("""
                   Delete from task where id=?
                   """,(id,))
    
    conn.commit()
def taskFinish(id):
    cursor.execute("""
                   UPDATE taskfinish set Flg_finish='1' ,  dat_finish = strftime('%s', 'now') where taskid=?
                   """,(id,))
    conn.commit()
    
def rollbackTask(id):
    cursor.execute("""
                   UPDATE taskfinish set Flg_finish=0 ,  dat_finish = '' where taskid=?
                   """,(id,))
    conn.commit()
def qnt_task():
    cursor.execute("""
                   SELECT COUNT(*) FROM task WHERE DAT_TASK = strftime('%Y-%m-%d', 'now')
                   """)
    result = cursor.fetchone()
        
    if result is not None:
        return result[0]  
    else:
        return None
    