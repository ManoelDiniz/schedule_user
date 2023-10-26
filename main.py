import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
import ctypes
from components.Login import *


janela = ctk.CTk()

class Application:
    def __init__(self):
        tema()
        tela(janela)
        telaLogin(janela)        
        janela.mainloop()    
        
   

Application()