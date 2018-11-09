
#! /usr/bin/env python3
# code by Vinzenz Felder
# Here are all elementary funktion for execution

import sys
import Adafruit_BBIO.GPIO as GPIO
import time 

import tkinter as tk

import tkinter.ttk

#global a
#a=0
LED1 = "P9_12"
GPIO.setup(LED1, GPIO.OUT)


def led_on(a):    
    #a=0
    sys.stdout.flush()
    #GPIO.output(LED1,1)
    if a == 0 :
    #if GPIO.output("LED1",0) == true :
     #   time.sleep(0.1)
      #  old_switch_state = 1
        GPIO.output(LED1, 0)
        a=1
        print('Lights on')
        
    elif a == 1:
        GPIO.output(LED1,1)
        print('Lights off')
        a=0

def led_off():    
    sys.stdout.flush()
    GPIO.output(LED1,0)
    print('Lights off')

def quit():
    print('gui_support.quit')
    sys.stdout.flush()
    sys.exit()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui.py
    gui.py.vp_start_gui()




