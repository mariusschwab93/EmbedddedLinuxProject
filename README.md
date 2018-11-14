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

the used packages for python are : tkinter, tcl, tk, Adafruit_GPIO, time, sys and smbus


# Setting up Scripts
In order to have the sequence play on startup, you need to download crontab. Get internet on your pocketbeagle by using the ipMasquerade script as well as the pocketssh script. SSH into your beagle and run a ping google.com command to verify that you have internet on your pocketbeagle. 
- All information on how you can use crontab to execute the autostart.sh file from the Beaglebone are here: https://billwaa.wordpress.com/2014/10/03/beaglebone-black-launch-python-script-at-boot-like-arduino-sketch/

# Heckster.io
The wikipedia for this project can be found here.
https://www.hackster.io/DanielPatzer/smart-rv-96ddbd


