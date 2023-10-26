from database.queryDb import *
from tkinter import messagebox

def CreateTaskService(name_task,dat_task,descri,user,namep):
    verifyNameTask = getTask(name_task, user)
    if verifyNameTask is not None:
        messagebox.showerror(title="Error",message="Nome da Tarefa em uso")
    elif name_task == '':
           messagebox.showerror(title="Error",message="Insira o nome da tarefa")
    else:
        id_level = getNivel(namep)
        createTask(name_task,dat_task,descri,user,id_level)
        messagebox.showinfo(title='Sucesso', message=f'Tarefa {name_task} criada com sucesso')
    
    