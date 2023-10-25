import bcrypt
from database.createDb import *
from tkinter import messagebox

def authenticateservice(login, password):
    def getpassword():
        return userExist(login)

    def getuser():
        return getPassword(login)

    stored_password = getpassword().encode('utf-8')  # Codificar a senha armazenada
    provided_password = password.encode('utf-8')  # Codificar a senha fornecida

    if bcrypt.checkpw(provided_password, stored_password):
        messagebox.showinfo(title='Sucesso', message='Você Logou')
    else:
        messagebox.showerror(title='Erro', message='Usuário ou senha incorretos')

