Hi this is our ECE-497 Project at ROSE-Hulman Institute of Technology

We are three students who thought about making a Prototype for a Camper automation, which connects different function of the Camper under on centralized system.
the three students are: Marius Schwab, Daniel Patzer and Vinzenz Felder

# Introduction
This Project is called Camper Home Automation:

In the Project we are using a 7” LED Touch panel to display sensor data and control outputs. Sensor data that will be displayed on the screen include two independent temperature measurements. The data will be displayed in number. For monitoring the temperature behavior over time. The GUI include Buttons to control a one channel relays to switch on led Lights or a Pump. Additional we integrated a clock with an alarm function to trigger time dependent events. 

all information are sumed up in a wiki Page.
located here: https://elinux.org/ECE497_Project_-_Camper_Automation

# Installation:
for all necessary packages we included an install.sh file , please execute it before beginning

the used packages for python are : tkinter, tcl, tk, Adafruit_GPIO, time, sys, os and smbus


# Setting up Scripts
For setting up put the autostart.sh file on the Desktop and execute it with double touch. We had no success to set up the GUI file as boot. several problems accured.
Please let me know if some one fixed the problem! We tried systemctl, crontab, autostart.No success

# Hackster.io
The wikipedia for this project can be found here.
https://www.hackster.io/DanielPatzer/smart-rv-96ddbd


