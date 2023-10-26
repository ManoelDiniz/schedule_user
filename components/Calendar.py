import customtkinter as ctk
from tkcalendar import Calendar

def calendar(home_frame):
    ctk.CTkLabel(master=home_frame, text='Bem Vindo ao Seu Calendário', font=('Roboto', 25)).place(x=75, y=5)

    start_cal = Calendar(home_frame, selectmode='day', locale='en_US')
    start_cal.place(x=100,y=80)

    selected_date_label = ctk.CTkLabel(master=home_frame, text="", font=("Helvetica", 12))
    selected_date_label.place(x=200, y=300)

    def set_selected_date(event):
        selected_date = start_cal.get_date()
        selected_date_label.configure(text=selected_date)

    start_cal.bind("<<CalendarSelected>>", set_selected_date)