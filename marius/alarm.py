from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import time
import datetime

root = Tk()
root.geometry("640x480")
root.frame = Frame(root)
root.frame.pack(fill = "both")
label = Label(root, text= "Welcome", bg = "black", fg = "white", font=("Times", 50))
label.pack(side= "top", fill = "both", expand = 1)
root.title_font = tkfont.Font(family = "Times", size = 100, weight = "bold", slant = "italic")
root.title("Clock")
wake = ''

def alarm():
    button_alarm.pack_forget()
    wake_entry.pack()
    wake_entry_button.pack(side = BOTTOM)
    wake_entry.focus()

def set_alarm():
   global wake
   wake_entry.pack_forget()
   wake_entry_button.pack_forget()
   button_alarm.pack()
   wake = wake_entry.get()

def tick():
    global wake
    current_time = time.strftime("%I:%M:%S")
    label.config(text=current_time)
    print(wake)
    if wake == current_time:
        label.config(bg="red")
    label.after(200, tick)
        
wake_entry = Entry(root)
wake_entry_button = Button(root, text="Set Alarm", command=set_alarm)
button_alarm = Button(text = "Alarm", command=alarm)
button_alarm.pack()
tick()
root.mainloop()
