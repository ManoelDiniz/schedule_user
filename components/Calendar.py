from datetime import datetime
import customtkinter as ctk
from tkcalendar import Calendar
from tkinter import ttk
import tkinter as tk
from database.queryDb import *
from services.EditTaskService import *

def calendar(home_frame,user):
    ctk.CTkLabel(master=home_frame, text=f'Bem Vindo ao Seu Calendário', font=('Roboto', 25)).place(x=75, y=5)
    qtd = qnt_task()
    start_cal = Calendar(home_frame, selectmode='day', locale='en_US')
    start_cal.place(x=115, y=50)


    style = ttk.Style()
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Arial', 11, 'bold'), foreground='black')
    style.configure("Treeview.Heading", font=('Calibri', 13, 'bold'), foreground='blue', background='black')
    style.configure("Treeview.Treeitem", foreground='white', background='black')
    columns = ["Prioridade", "Nome Tarefa", "Descrição Tarefa"]
    tree = ttk.Treeview(home_frame, show='headings', columns=columns)
    tree.place(x=45, y=280)
    tree.heading("#1", text="Prioridade")
    tree.heading("#2", text="Nome Tarefa")
    tree.heading("#3", text="Descrição Tarefa")
    tree.column("#0", stretch=tk.NO, width=0)
    tree.column("#1", width=100, anchor='center')
    tree.column("#2", width=150, anchor='center')
    tree.column("#3", width=150, anchor='center')
    selected_values = None
    selected_task_id = None

    def on_treeview_select(event):
        item = tree.selection()
        if item:
            nonlocal selected_values, selected_task_id
            values = tree.item(item, 'values')
            selected_task_id = values[0]  # Obtém o ID da tarefa
            selected_values = values[1]
            # Obtém os outros valores (Prioridade, Nome Tarefa, Descrição Tarefa)
    
    tree.bind("<<TreeviewSelect>>", on_treeview_select)
    
    def finish_task():
        if selected_values and selected_task_id:
            prioridade, nome_tarefa, descricao_tarefa, *_ = selected_values
            name_task = selected_values
            
            id = getTask(name_task, user)
            
            if id is not None: 
                EditTaskService.resolvTask(id)
            update_treeview()
    
    def update_treeview():
        select_date = selected_date_label.cget("text")
        getTask = getCalendarTask(select_date,user)
        tree.tag_configure("high_priority", background="red", foreground="white")
        tree.tag_configure("finish", background="black", foreground="white")
        tree.tag_configure("normal_priority", background="white", foreground="black")
        
        tree.delete(*tree.get_children())

        for nivel in getTask:
            Prioridade = nivel[0]
            NomeTarefa = nivel[1]
            Descrição_Tarefa = nivel[2]
            inativ = nivel[3]
            
            if inativ == 1:
                tree.insert("", "end", values=(Prioridade, NomeTarefa, Descrição_Tarefa), tags=("finish",))
            else:
                if Prioridade >= 5:
                    tree.insert("", "end", values=(Prioridade, NomeTarefa, Descrição_Tarefa), tags=("high_priority",))
                else:
                    tree.insert("", "end", values=(Prioridade, NomeTarefa, Descrição_Tarefa), tags=("normal_priority",))

    tree.config(height=8)

    
   
    selected_date_label = ctk.CTkButton(master=home_frame, text="", font=("Helvetica", 20),command=update_treeview,state="disable")
    selected_date_label.place(x=225, y=245)
    today = datetime.now().strftime("%d/%m/%Y")
    selected_date_label.configure(text=today)
    update_treeview()
    def set_selected_date(event):
        selected_date = start_cal.get_date()
        
        parts = selected_date.split('/')

        if len(parts) == 3:
    
            month,day, year = parts[0], parts[1], parts[2]

           
            if len(year) == 2:
                current_year = datetime.now().year
                century = current_year // 100
                full_year = century * 100 + int(year)
                selected_date = f'{day}/{month}/{full_year}'

            selected_date_label.configure(text=selected_date)
            update_treeview()
        else:
           
            selected_date_label.configure(text="Nenhuma data selecionada")
            tree.delete(*tree.get_children())
    
    start_cal.bind("<<CalendarSelected>>", set_selected_date)
    ctk.CTkButton(master=home_frame, text='Resolvido', width=100,command=finish_task,).place(x=120,y=245)
    
    
    


   
