from components.telaregister import *
from services.Authenticateservice import *
import customtkinter as ctk
from tkinter import *
import tkinter as tk



def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

def tela(janela):
        janela.geometry("700x400")
        janela.title("Login Infarma Utility")
def telaLogin (janela):
        
        label_img = ctk.CTkButton(
            master=janela,
            
            hover_color="none",
            bg_color="transparent",
            fg_color=None,
            text=None,
            hover=None,
        )
        label_img.place(x=35, y=65)
        labeltt = ctk.CTkLabel(
            master=janela,
            text="Bem vindo \n ao \n Infarma Integrações",
            font=("Arial", 18),
        )
        labeltt.place(x=175, y=150)
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
            authenticateservice(login,password)
            
        button = ctk.CTkButton(master=login_frame, text='ENTRAR', command=login)
        button.place(x=25,y=265)
        buttonregister = ctk.CTkButton(master=login_frame, text='Registrar', command=register)
        buttonregister.place(x=25,y=305)