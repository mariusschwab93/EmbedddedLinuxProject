#! /usr/bin/env python3
# code by Vinzenz Felder/ Marius Schwab
# Here are all elementary funktion for execution the main gui.py is pointing to the gui_support
import os
import sys


import tkinter as tk

import tkinter.ttk
import time
import smbus
import alarm2
import Adafruit_BBIO.GPIO as GPIO

LED1 = "P9_12"              # Gpio setup
GPIO.setup(LED1, GPIO.OUT)
LED2 = "P9_16"
GPIO.setup(LED2,GPIO.OUT)

bus = smbus.SMBus(2) # i2c setup for temperature
address1 = 0x48
address2 = 0x49
b= 0
c= 0
def tempout():
   
   tempout = bus.read_byte_data(address1, 0)
   #temp2 = bus.read_byte_data(address2, 0)*(9/5)+32 to display in Fahrenheit
    
   return tempout

def tempin():
   
   #tempout = bus.read_byte_data(address1, 0)*(9/5)+32 
   tempin = bus.read_byte_data(address2, 0)
    
   return tempin

def edit():  # edit function for alarm of clock and edit
    print('gui_support.edit')
    #alarm2.MainApplication 
    os.system('python alarm2.py')
    #subprocess.Popen("alarm2.py")
    sys.stdout.flush()

def led_toggle(): # toggle function for relay 1 (Light)
    print('gui_support.led_toggle')
    sys.stdout.flush()
    global b    
    if b==1 :
        GPIO.output(LED1, 0)
        print('Lights off')
        b=0
    else:
        GPIO.output(LED1,1)
        print('Lights on')
        b=1
def relay_toggle(): # toggle function for relay 2 (Pump)
    print('gui_support.led_toggle')
    sys.stdout.flush()
    global c
        
    if c==1 :
        GPIO.output(LED2, 0)
        print('Pump off')
        c=0
    else:
        GPIO.output(LED2,1)
        print('pump on')
        c=1


def quit(): # gui quit function
    print('gui_support.quit')
    sys.stdout.flush()
    sys.exit()

def ticktick(): # clock function
    time_string = time.strftime( "%d/%m/%Y %A %H:%M:%S" )
    return time_string

def init(top, gui, *args, **kwargs): # argument value function
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




