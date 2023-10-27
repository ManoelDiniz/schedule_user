from components.telaregister import *
from services.Authenticateservice import *
import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage



def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

def tela(janela):
        janela.geometry("700x400")
        janela.title("Mv Agenda")
def telaLogin (janela):
        labeltt = ctk.CTkLabel(
            master=janela,
            text="Bem Vindo ao \nMV Agenda",
            font=("Cambria", 55),
        )
        labeltt.place(x=5, y=100)
        # frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)
        # Interaction of Users
        label = ctk.CTkLabel(
            master=login_frame,
            text="Tela Login",
            text_color="white",
            font=("roboto", 35, "bold"),
        )
        label.place(x=55, y=15)
        User_entry = ctk.CTkEntry(
            master=login_frame,
            placeholder_text="Usuario",
            width=300,
            font=("Roboto", 14),
        )
        User_entry.place(x=25, y=105)

        username_label = ctk.CTkLabel(
            master=login_frame,
            text="Nome de usuario obrigatorio",
            text_color="white",
            font=("Roboto", 8),
        )
        username_label.place(x=25, y=135)
        senha_entry = ctk.CTkEntry(
            master=login_frame,
            placeholder_text="Senha",
            width=300,
            font=("Roboto", 14),
            show="*",
        )
        senha_entry.place(x=25, y=175)
        password_label = ctk.CTkLabel(
            master=login_frame,
            text="Senha de usuario obrigatorio",
            text_color="white",
            font=("Roboto", 8),
        )
        password_label.place(x=25, y=205)
        
        
        
        def login():
            login = User_entry.get()
            password = senha_entry.get()
            AuthenticateService(login,password,janela)
            
        button = ctk.CTkButton(master=login_frame, text='ENTRAR', command=login)
        button.place(x=80,y=265)
        buttonregister = ctk.CTkButton(master=login_frame, text='Registrar', command=register)
        buttonregister.place(x=80,y=305)