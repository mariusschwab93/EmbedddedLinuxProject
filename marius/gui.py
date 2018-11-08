#! /usr/bin/env python
#  code Vinzenz Felder
# main class for creating GUI --> hardware execution is done through gui_2_support.py 

import smbus
import sys
import time
try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import tkinter.ttk

except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui_support

from tkinter import messagebox


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {DejaVu Sans} -size 17 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1024x600+1185+447")
        top.title("Camper Automation")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.693, rely=0.067, relheight=0.858, relwidth=0.269)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(width=275)

        self.LIGHT = tk.Button(self.Frame1)
        self.LIGHT.place(relx=0.036, rely=0.039, height=133, width=257)
        self.LIGHT.configure(activebackground="#d82750")
        self.LIGHT.configure(activeforeground="white")
        self.LIGHT.configure(command=gui_support.led_toggle)
        self.LIGHT.configure(font=font11)
        self.LIGHT.configure(highlightbackground="#999496")
        self.LIGHT.configure(text='''LIGHT''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.036, rely=0.369, height=133, width=257)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(font=font11)
        self.Button2.configure(text='''PUMP''')

        self.Button3 = tk.Button(self.Frame1)
        self.Button3.place(relx=0.036, rely=0.718, height=123, width=257)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(font=font11)
        self.Button3.configure(text='''Button''')

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.068, rely=0.65, relheight=0.268, relwidth=0.45)
        self.Message1.configure(text='''Camper Home Automation''')
        self.Message1.configure(width=461)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.566, rely=0.817, height=41, width=85)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#ff246d")
        self.Button1.configure(command=gui_support.quit)
        self.Button1.configure(text='''QUIT''')

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.479, rely=0.1, height=91, width=72)
        self.Button4.configure(activebackground="#d9d9d9") 
        self.Button4.configure(command=gui_support.edit)
        self.Button4.configure(text='''Edit''')
        self.Button4.configure(width=72)

        self.Labelframe1 = tk.LabelFrame(top)
        self.Labelframe1.place(relx=0.049, rely=0.267, relheight=0.325, relwidth=0.176)
        self.Labelframe1.configure(relief='groove')
        self.Labelframe1.configure(text='''Temp''')
        self.Labelframe1.configure(width=180)


        self.Label2 = tk.Label(self.Labelframe1)
        self.Label2.place(relx=0.056, rely=0.154, height=73, width=159, bordermode='ignore')
        self.Label2.configure(activebackground="#ededed")
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(font=font13)
       # self.Label2.configure(text='''indoor Temp''')
        self.Label2.configure(width=159)
        def temp_in():
                self.Label2.configure(text="Inside:  "+str(gui_support.tempin())+" °C")
                self.Label2.after(150,temp_in)

        temp_in()

        self.Label3 = tk.Label(self.Labelframe1)
        self.Label3.place(relx=0.056, rely=0.564, height=73, width=159, bordermode='ignore')
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(font=font13)
 #       self.Label3.configure(text='''Labelb''')
        self.Label3.configure(width=159)

        def temp_out():
                self.Label3.configure(text="Outside:  "+str(gui_support.tempout())+" °C")
                self.Label3.after(150,temp_out)

        temp_out()

        self.Labelframe2 = tk.LabelFrame(top)
        self.Labelframe2.place(relx=0.049, rely=0.067, relheight=0.192, relwidth=0.42)
        self.Labelframe2.configure(relief='groove')
        self.Labelframe2.configure(font=font15)
        self.Labelframe2.configure(text='''Clock''')
        self.Labelframe2.configure(width=430)


        self.Label1 = tk.Label(self.Labelframe2)
        self.Label1.place(relx=0.023, rely=0.261, height=73, width=415, bordermode='ignore')
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(background="#000000")
        self.Label1.configure(foreground="#1cff2b")
        self.Label1.configure(highlightbackground="#17ff2e")
        self.Label1.configure(highlightcolor="#08ff31")
        #self.Label1.configure(text='''Label''')
        self.Label1.configure(width=415)
        def tick():
                self.Label1.configure(text=gui_support.ticktick())
                self.Label1.after(150,tick)
        tick()



#        root.geometry("640x480")
 #       root.frame = Frame(root)
  #      root.frame.pack(fill = "both")
   #     label = Label(root, text= "Welcome", bg = "black", fg = "white", font=("Times", 50))
    #    label.pack(side= "top", fill = "both", expand = 1)
     #   root.title_font = tkfont.Font(family = "Times", size = 100, weight = "bold", slant = "italic")
      #  root.title("Clock")



       # def alarm():
        #        current_time = tick()
         #       wake_entry = Entry(root)
          #      wake_entry.pack()
           #     wake_entry_button = Button(root, text="Set Alarm")
            #    wake_entry_button.pack(side = BOTTOM)
             #   wake = wake_entry.get()
              #  wake = time.strftime("%I:%M")
               # if wake == gui_support.ticktick():
                #       label.config(root, bg = "red")


#	def tick(time1 = ""):

    	#	time2 = time.strftime("%I:%M:%S")
    	#	if time2 != time1:
        #		time1 = time2
        #		label.config(text = time1)
    	#	label.after(200, tick)
    	#	return time1

#        button_alarm = Button(text = "Alarm")
 #       button_alarm.config(command = alarm)
  #      button_alarm.pack()





if __name__ == '__main__':
    vp_start_gui()





