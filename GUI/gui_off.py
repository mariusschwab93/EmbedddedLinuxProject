


#! /usr/bin/env python3

import sys
import Adafruit_BBIO.GPIO as GPIO
import time 

import tkinter as tk

import tkinter.ttk

LED1 = "P9_12"
GPIO.setup(LED1, GPIO.OUT)


def led_off():    
    print('Lights on')
    sys.stdout.flush()
    GPIO.output(LED1, 0)

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

