#! /usr/bin/env python3
# code by Vinzenz Felder
# Here are all elementary funktion for execution

import sys

try:
    import tkinter as tk

try:
    import tkinter.ttk


def led_toggle():
    print('gui_2_support.led_toggle')
    sys.stdout.flush()

def quit():
    print('gui_2_support.quit')
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




