import bcrypt
from tkinter import messagebox
from database.createDb import *

def RegisterService(login, name, passw):
    if login == '':
        messagebox.showerror(title='Erro', message='Por favor insira o seu login')
    elif name == '':
        messagebox.showerror(title='Erro', message='Por favor insira o seu nome')
    elif passw == '':
        messagebox.showerror(title='Erro', message='Por favor insira o sua senha')
    else:
        registeruser(login, name, passw)
        messagebox.showinfo(title='Sucesso', message='Registro Feito Sucesso')