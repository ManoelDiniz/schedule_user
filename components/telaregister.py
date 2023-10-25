import customtkinter as ctk
from services.Register import *

def register():
    janela_registro = ctk.CTk()
    
    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(janela_registro):
        janela_registro.geometry("250x300")
        janela_registro.title("Registro - Infarma Utility")
    
    tela(janela_registro)
    
    registro_frame = ctk.CTkFrame(master=janela_registro, width=500, height=400)
    registro_frame.pack()
    
    label = ctk.CTkLabel(master=registro_frame, text='Tela de registro', font=('Roboto',25)).place(x=25,y=25)
    
    entryname = ctk.CTkEntry(master=registro_frame, placeholder_text='Insira seu nome', width=200)
    entryname.place(x=25, y=105)
    entrylogin = ctk.CTkEntry(master=registro_frame, placeholder_text='Insira seu login', width=200)
    entrylogin.place(x=25, y=145)
    entrypass = ctk.CTkEntry(master=registro_frame, placeholder_text='Insira seu password', width=200, show='*')
    entrypass.place(x=25, y=185)
    
    def registrar():
        login = entryname.get()
        name = entrylogin.get()
        passw = entrypass.get()
        RegisterService(login, name, passw)
    
    ctk.CTkButton(master=registro_frame, text='Registrar', width=200, command=registrar).place(x=25, y=225)

    janela_registro.mainloop()
