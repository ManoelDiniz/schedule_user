from datetime import datetime
import customtkinter as ctk
from tkcalendar import Calendar
from tkinter import ttk
import tkinter as tk
from database.queryDb import *
from components.Calendar import *
from services.EditTaskService import *

def EditTask(home_frame, user):
    ctk.CTkLabel(master=home_frame, text='Edição de Tarefa Salva', font=("Arial", 35,"bold")).place(x=55,y=25)
    style = ttk.Style()
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 11, 'bold'), foreground='black')
    style.configure("Treeview.Heading", font=('Calibri', 13, 'bold'), foreground='blue', background='black')
    style.configure("Treeview.Treeitem", foreground='white', background='black')
    columns = ["Id", "Prioridade", "Nome Tarefa", "Descrição Tarefa"]
    tree = ttk.Treeview(home_frame, show='headings', columns=columns)
    tree.place(x=45, y=280)
    tree.heading("#1", text="Id")
    tree.heading("#2", text="Prioridade")
    tree.heading("#3", text="Nome Tarefa")
    tree.heading("#4", text="Descrição Tarefa")
    tree.column("#0", stretch=tk.NO, width=0)
    tree.column("#1", width=10, anchor='center')
    tree.column("#2", width=100, anchor='center')
    tree.column("#3", width=150, anchor='center')
    tree.column("#4", width=150, anchor='center')

    def update_treeview():
        getTask = getEditTasks(user)
        tree.tag_configure("high_priority", background="red", foreground="white")
        tree.tag_configure("finish", background="black", foreground="white")
        tree.tag_configure("normal_priority", background="white", foreground="black")
        tree.delete(*tree.get_children())
        
        for nivel in getTask:
            id, Prioridade, NomeTarefa, Descrição_Tarefa, finish = nivel[0], nivel[1], nivel[2], nivel[3], nivel[4]
 
            if finish == 1:
                tree.insert("", "end", values=(id,Prioridade, NomeTarefa, Descrição_Tarefa), tags=("finish",))
            else:
                if Prioridade >= 5:
                    tree.insert("", "end", values=(id, Prioridade, NomeTarefa, Descrição_Tarefa), tags=("high_priority",))
                else:
                    tree.insert("", "end", values=(id, Prioridade, NomeTarefa, Descrição_Tarefa), tags=("normal_priority",))
    
    update_treeview()
    tree.config(height=8)

    name_task = ctk.CTkEntry(master=home_frame, placeholder_text='Insira o novo nome da tarefa', width=350)
    name_task.place(x=80, y=120)
    desc_task = ctk.CTkEntry(master=home_frame, placeholder_text='Insira a nova descrição da tarefa', width=350)
    desc_task.place(x=80, y=160)
    options = getNivelL()
    
    box = ctk.CTkOptionMenu(master=home_frame, values=options, width=350)
    box.set('')
    box.place(x=80, y=195)
    
    selected_values = None
    selected_task_id = None

    def on_treeview_select(event):
        item = tree.selection()
        if item:
            nonlocal selected_values, selected_task_id
            values = tree.item(item, 'values')
            selected_task_id = values[0]  # Obtém o ID da tarefa
            selected_values = values[1:]  # Obtém os outros valores (Prioridade, Nome Tarefa, Descrição Tarefa)
    
    tree.bind("<<TreeviewSelect>>", on_treeview_select)

    def alter_task():
        if selected_values and selected_task_id:
            prioridade, nome_tarefa, descricao_tarefa = selected_values            
            name = name_task.get()
            desc = desc_task.get()
            namep = box.get()
            id = selected_task_id
            EditTaskService.alter(name,desc,namep,id,user)
            update_treeview()
    
    button_alter = ctk.CTkButton(master=home_frame, text="Alterar", width=100, command=alter_task)
    button_alter.place(x=40, y=230)
    def delete_task():
        if selected_values and selected_task_id:
            prioridade, nome_tarefa, descricao_tarefa = selected_values            
            
            id = selected_task_id
            EditTaskService.delete(id)
            update_treeview()
    button_delete = ctk.CTkButton(master=home_frame, text="Apagar", width=100, command=delete_task)
    button_delete.place(x=145, y=230)
    def resolv_task():
        if selected_values and selected_task_id:
            prioridade, nome_tarefa, descricao_tarefa = selected_values            
            id = selected_task_id
            EditTaskService.resolvTask(id)
            update_treeview()
            
    button_resolv = ctk.CTkButton(master=home_frame, text="Resolvido", width=100,command=resolv_task).place(x=250, y=230)
    def unresolv_task():
        if selected_values and selected_task_id:
                       
            id = selected_task_id
            EditTaskService.rollbackTask(id)
            update_treeview()
    buttom_noresolv = ctk.CTkButton(master=home_frame, text="Não Resolvido", width=100,command=unresolv_task).place(x=355, y=230)
    