#! /usr/bin/env python3
# code by Vinzenz Felder
# Here are all elementary funktion for execution

import sys


import tkinter as tk

import tkinter.ttk
import time
import smbus

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x49

def tempout():
   
   tempout = bus.read_byte_data(address1, 0)
   #temp2 = bus.read_byte_data(address2, 0)*(9/5)+32
    
   return tempout

def tempin():
   
   #tempout = bus.read_byte_data(address1, 0)*(9/5)+32
   tempin = bus.read_byte_data(address2, 0)
    
   return tempin

def led_toggle():
    print('gui_support.led_toggle')
    sys.stdout.flush()

def quit():
    print('gui_support.quit')
    sys.stdout.flush()
    sys.exit()

def ticktick():
    time_string = time.strftime( "%d/%m/%Y %A %H:%M:%S" )
    return time_string

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
    




