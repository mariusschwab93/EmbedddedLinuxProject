from tkinter import Tk
from tkinter import Button
from tkinter import Frame
from tkinter import font
from tkinter import Widget
from tkinter import Label
from tkinter import Entry
import time
import datetime
import Adafruit_BBIO.GPIO as GPIO

LED2 = "P9_13"
GPIO.setup(LED2, GPIO.OUT)

#Define the Class to be used for this program. We will pass root into this as Frame.
class MainApplication(Frame):
#def MainApplication(Frame):
    wake = ""
    def __init__(self, master):
        master.geometry("800x400")
        master.title("Noah's Pi-Clock")
        master.config(bg="black")
        self.frame = Frame(master)
        self.frame.pack()

        self.master = master

        self.label = Label(master, font=("Times", 32), fg = "white", bg = "black")
        self.label.pack(expand = 1, fill = "both", side = "top")

        self.alarmButton = Button(master, text = "Alarm", command = self.alarm)
        self.alarmButton.pack(side="right")

        self.setButton = Button(master, text = "Set Alarm", command = self.setAlarm)
        self.setButton.pack_forget()

        self.alarm_entry = Entry(master, relief = "ridge")
        self.alarm_entry.bind("<Button-1>", self.numPad)
        self.alarm_entry.pack_forget()

        self.exitButton = Button(master, text = " Exit ", command = self.frame.quit)
        self.exitButton.pack(side = "left", ipadx = 3)

        self.clock()

    def clock(self):
        self.time1 = time.strftime("%I:%M:%S")
        self.label.config(text = self.time1)
        self.label.pack(expand = "yes", fill="both", side = "top")

        if self.time1 == self.wake:
            self.label.config(bg = "green")
            self.master.config(bg = "green")
            GPIO.output(LED2, 1)

        else:
            self.label.config(bg = "black")
            self.master.config(bg = "black")

        self.label.after(200, self.clock)

    def alarm(self):
        self.setButton.pack(side = "bottom", pady = 10)
        self.alarm_entry.pack()
        self.alarmButton.pack_forget()
        self.exitButton.pack_forget()

    def setAlarm(self, *args):
        self.wake = self.alarm_entry.get()
        self.alarm_entry.bind("<Button-1>", self.numPad)
        self.alarmButton.pack(side = "right")
        self.exitButton.pack(side = "left")
        self.setButton.pack_forget()
        self.alarm_entry.pack_forget()
        self.frame.pack_forget()

    def numPad(self, *args):
        self.alarm_entry.unbind("<Button-1>")
        self.frame = Frame()
        self.frame.pack()
        num_list = ["0","1","2","3","4","5","6","7","8","9",":"]
        r = 1
        c = 0
        for n in num_list:
            self.num_button = Button(self.frame,
            text = n, bg = "white", fg = "black", width = 7, relief = "ridge",
            command=lambda n = n: self.alarm_entry.insert("insert", n)).grid(row = r, column = c)
            c += 1
            if c > 4:
                c = 0
                r += 1
        self.delete_button = Button(self.frame, text = "Clear", bg = "white", fg = "black", width = 7, relief = "ridge",
        command =lambda: self.alarm_entry.delete(0, "end")).grid(row = 3, column = 1, columnspan = 2, sticky = "WE")



root = Tk()
app = MainApplication(root)
root.mainloop()
