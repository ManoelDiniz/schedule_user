from tkinter import messagebox
from database.queryDb  import *

class EditTaskService:
    def alter(name,desc,namep,id, user):
        if name == '' and desc == '' and namep =='':
            messagebox.showerror(title="Erro", message="Insira ao menos uma informação para \nalterar a tarefa")
        elif desc == '' and namep == '':
            alterNameTask(name,id,user)
            messagebox.showinfo(title='Sucesso', message="Nome alterado com sucesso")
        elif name == '' and namep == '':
            alterDescTask(desc, id , user)
            messagebox.showinfo(title='Sucesso', message="Descrição alterada com sucesso alterado com sucesso")
        elif name == '' and desc == '':
                nivels = getNivel(namep)
                alterNivelTask(nivels, id , user)
                messagebox.showinfo(title='Sucesso', message="Nivel da Tarefa alterada com sucesso alterado com sucesso")
        else:
            nivels = getNivel(namep)
            
            alterAllTask(name,desc,namep,id, user)
    def delete(id):
        try:    
            deleteTask(id)
            messagebox.showinfo(title='Sucesso', message="Nivel da Tarefa alterada com sucesso alterado com sucesso")
        except:
            messagebox.showerror(title="Erro", message="Erro ao deletar a tarefa")
    def resolvTask(id):
        try:
            taskFinish(id)
            messagebox.showinfo(title='Sucesso', message="Tarefa Finalizada com sucesso")
        except:
            messagebox.showerror(title="Erro", message="Erro ao finalizar a tarefa")
    def rollbackTask(id):
        try:
            rollbackTask(id)
            messagebox.showinfo(title='Sucesso', message="Tarefa Voltada com sucesso")
        except:
            messagebox.showerror(title="Erro", message="Erro ao voltar a tarefa")