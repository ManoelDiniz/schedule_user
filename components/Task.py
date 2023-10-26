import customtkinter as ctk
from tkcalendar import DateEntry
from services.CreateTaskService import *


def CreateTask(home_frame, user):
    
    ctk.CTkLabel(master=home_frame, text="Bem Vindo à Tela de Criação de Tarefas", font=("Arial", 25)).place(x=5, y=5)

    input_name = ctk.CTkEntry(master=home_frame, placeholder_text='Insira o nome de sua tarefa', width=350)
    input_name.place(x=100, y=50)

    ctk.CTkLabel(master=home_frame, text="Data Da Tarefa", font=("Arial",15)).place(x=100, y=100)
    input_datask = DateEntry(
        home_frame,
        date_pattern="dd/MM/yyyy",
        font=("Arial", 12),  
        foreground="white",
        background="black",  
        bordercolor="blue",  
        selectbackground="lightblue", 
        selectforeground="black",  
        cursor="hand2",  
        showweeknumbers=False, 
        width=12,  
    )
    input_datask.set_date("01/01/2023")  
    input_datask.place(x=215, y=100)

    Input_descri = ctk.CTkEntry(master=home_frame, placeholder_text='Insira a descrição de sua tarefa', width=350)
    Input_descri.place(x=100, y=150)
    def CreateTask():
        name_task = input_name.get()
        dat_task = input_datask.get_date()
        descri = Input_descri.get()
        
        CreateTaskService(name_task,dat_task,descri,user)
        
    
    ctk.CTkButton(master=home_frame, text="Criar Tarefa", width=200, command=CreateTask).place(x=100,y=200)