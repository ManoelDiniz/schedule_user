import customtkinter as ctk
from  components.Calendar import *
from components.Task import *
from components.PriorityLevels import *
from components.EditTask import *
from database.queryDb import *


def HomePage(name_user, user):
    Home = ctk.CTk()

    def tema():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(Home):
        Home.geometry("700x500")
        Home.title("Home Page")

    home_frame = ctk.CTkFrame(master=Home, width=550, height=550)
    home_frame.place(x=180)
    
    label = ctk.CTkLabel(master=Home, text="Opções", font=("Aria", 35))
    label.place(x=35,y=5)
    
    
    calendar(home_frame,user)
    
    def Calendar():
        for widget in home_frame.winfo_children():
            widget.destroy()
        calendar(home_frame,user)
    ctk.CTkButton(master=Home, text='Seu Calendario', width=150, command=Calendar).place(x=15,y=125)
    def task():
        for widget in home_frame.winfo_children():
            widget.destroy()
        CreateTask(home_frame, user)  
    ctk.CTkButton(master=Home, text='Criar Tarefas', width=150,command=task).place(x=15,y=165)
    
    def editTasks():
        for widget in home_frame.winfo_children():
            widget.destroy()
        EditTask(home_frame, user)
    ctk.CTkButton(master=Home, text='Editar Tarefas', width=150,command=editTasks).place(x=15,y=205)
    def levels():
        for widget in home_frame.winfo_children():
            widget.destroy()
        PriorityLevels(home_frame)
    ctk.CTkButton(master=Home, text='Niveis de pioridade', width=150,command=levels).place(x=15,y=245)
    
   
    
    

   
    tela(Home)
    Home.mainloop()

