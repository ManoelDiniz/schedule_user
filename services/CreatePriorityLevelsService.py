from database.queryDb import *
from tkinter import messagebox

def CreatePriorityLevelsService(namep, nivel, emoji):
    result = getNivel(namep)
    if result is not None:
        messagebox.showerror(title="Erro", message=f'Nivel {namep} ja cadastrado')
    else:
        createNivels(namep, nivel, emoji)
        messagebox.showinfo(title='Sucesso', message=f'Nivel {namep} foi criado com sucesso')