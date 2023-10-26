from database.queryDb import *
from tkinter import messagebox

def CreateTaskService(name_task,dat_task,descri,user):
    verifyNameTask = getTask(name_task, user)
    if verifyNameTask is not None:
        messagebox.showerror(title="Error",message="Nome da Tarefa em uso")
    else:
        
        createTask(name_task,dat_task,descri,user)
        messagebox.showinfo(title='Sucesso', message=f'Tarefa {name_task} criada com sucesso')
    
    