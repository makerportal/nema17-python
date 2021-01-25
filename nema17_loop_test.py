#######################################
# Copyright (c) 2021 Maker Portal LLC
# Author: Joshua Hrisko
#######################################
#
# NEMA 17 (17HS4023) Raspberry Pi Tests
# --- rotating the NEMA 17 clockwise
# --- and counterclockwise in a loop
#
#
#######################################
#
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

################################
# RPi and Motor Pre-allocations
################################
#
#define GPIO pins
direction= 22 # Direction (DIR) GPIO Pin
step = 23 # Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)

# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output

###########################
# Actual motor control
###########################
#
dir_array = [False,True]
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
for ii in range(10):
    mymotortest.motor_go(dir_array[ii%2], # False=Clockwise, True=Counterclockwise
                         "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                         200, # number of steps
                         .0005, # step delay [sec]
                         False, # True = print verbose output 
                         .05) # initial delay [sec]
    time.sleep(1)

GPIO.cleanup() # clear GPIO allocations after run
