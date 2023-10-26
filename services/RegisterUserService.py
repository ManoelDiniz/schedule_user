import bcrypt
from tkinter import messagebox
from database.queryDb import *

def RegisterService(login, name, passw):
    user = userExist(login)
    if user is None:
        if login == '':
            messagebox.showerror(title='Erro', message='Por favor insira o seu login')
        elif name == '':
            messagebox.showerror(title='Erro', message='Por favor insira o seu nome')
        elif passw == '':
            messagebox.showerror(title='Erro', message='Por favor insira o sua senha')
        else:
            registeruser( name,login, passw)
            messagebox.showinfo(title='Sucesso', message='Registro Feito Sucesso')
    else:
        messagebox.showerror(title='Erro', message='Login Ja cadastrado')