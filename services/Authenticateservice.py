import bcrypt
from database.createDb import *
from tkinter import messagebox

def authenticateservice(login, password):
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
                    messagebox.showinfo(title='Sucesso', message='Autenticação bem-sucedida')
                else:
                    messagebox.showerror(title='Erro', message='Senha incorreta')
            else:
                messagebox.showerror(title='Erro', message='Senha não encontrada para o usuário')

