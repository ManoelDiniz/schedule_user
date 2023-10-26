import bcrypt
from database.queryDb import *
from tkinter import messagebox
from components.HomePage import *

def AuthenticateService(login, password,janela):
    if login == '' or password == '':
        messagebox.showerror(title='Erro', message='Campo Usuario ou Senha Não pode \nFicar em branco ')
    else:
        user = userExist(login)
        
        if user is None:
            messagebox.showerror(title='Erro', message='Usuário não encontrado')
        else:
            get_pass = getPassword(user)
            if get_pass is not None:
                verify_pass = bcrypt.checkpw(password.encode('utf-8'), get_pass.encode('utf-8'))    
                if verify_pass:
                    janela.destroy()
                    name_user = getNameUser(user)                    
                    HomePage(name_user,user)
                else:
                    messagebox.showerror(title='Erro', message='Senha incorreta')
            else:
                messagebox.showerror(title='Erro', message='Senha não encontrada para o usuário')

