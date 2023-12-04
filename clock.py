from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import date

# Creating tkinter window
root = Tk()
root.title('Clock')
root.configure(bg='black')

# Function to display time on the label
def time():
    current_time = strftime('%H:%M:%S')
    lbl_time.config(text=current_time)
    lbl_time.after(1000, time)

# Function to display date on the label
def show_date():
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    lbl_date.config(text=current_date)

# Styling the time label widget
lbl_time = Label(root, font=('calibri', 80, 'bold'), background='black', foreground='white')
lbl_time.pack(anchor='center')
time()

# Styling the date label widget
lbl_date = Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl_date.pack(anchor='center')
show_date()

mainloop()
