import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from components.modules.emojis import *
from services.CreatePriorityLevelsService import * 

    
def PriorityLevels(home_frame):
    ctk.CTkLabel(master=home_frame, text='Tela Criação De Nivel', font=("Arial",35)).place(x=50,y=5)
    name_prioryt = ctk.CTkEntry(master=home_frame, placeholder_text='Insira o Nome da Prioridade', width=250)
    name_prioryt.place(x=120, y=120)
    
    options = ['1','2','3','4','5','6','7','8','9','10']
    
    box = ctk.CTkOptionMenu(master=home_frame, values=options, width=250)
    box.place(x=120,y=160)
    
    emoji = emojis()  
    
    boxemoji = ctk.CTkOptionMenu(master=home_frame, values=emoji, width=250)
    boxemoji.place(x=120, y=200)
    
    colums = ["Prioridade","Nivel Prioridade"]
    style = ttk.Style()
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 11, 'bold'),foreground='black')
    style.configure("Treeview.Heading" ,font=('Calibri', 13, 'bold'), foreground='blue', )
    style.configure("Treeview.Treeitem", foreground='white', background='black')
    tree = ttk.Treeview(home_frame, columns=colums, show= 'headings')
    tree.tag_configure('odd', background='#E8E8E8')
    tree.tag_configure('even', background='#DFDFDF')    
    tree.heading("#1", text="Prioridade")
    tree.heading("#2", text="Nivel Prioridade")
    tree.column("#0", stretch=tk.NO, width=0)
    tree.column("#1", width=100,anchor='center')
    tree.column("#2", width=150,anchor='center')
    tree.config(height=8)
    tree.place(y=280,x=120)
    niveis = get()     
    
    def update_treeview():
        tree.delete(*tree.get_children())
        is_odd = True
        for nivel in niveis:
            name_levels = nivel[0] 
            nivel_levels = nivel[1]
            tag = 'odd' if is_odd else 'even'
            is_odd = not is_odd
            tree.insert("", "end", values=(name_levels, nivel_levels),tags=(tag))
    
    update_treeview() 
    
    def createPriority():
        namep =name_prioryt.get()
        nivel = box.get()
        emoji = boxemoji.get()
        CreatePriorityLevelsService(namep, nivel, emoji)
        update_treeview()
    ctk.CTkButton(master=home_frame, text='Cadastrar Nivel', width=250, cursor="hand2", command=createPriority).place(x=120, y=240)