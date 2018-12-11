#!/usr/bin/python

# Importing libraries to be used.

import Rpi.GPIO as GPIO # A Rasp. Pi GPIO pin library
import smtplib # To send emails from the Rasp. Pi
import time # Standard time library

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Defining Channels used
sensor_One = 17
#sensor_Two = 5

# Setting GPIO Pins to Input
GPIO.setup(sensor_One, GPIO.IN)
#GPIO.setup(sensor_Two, GPIO.IN)

#######PLACE HOLDER LOOP/COUNTER############
RUNNING = True
COUNTER = 0
####################################

# SMTP sending info
smtp_UN = "raspbpinotice@gmail.com"
smtp_PW = "lelouch12"
smtp_Host = "smtp.gmail.com"
smtp_port = 465

smtp_sender = "raspbpinotice@gmail.com"
smtp_receiver = [ 'hahnfrankie@gmail.com', 'katieamenta@aol.com' ]

# Messages

needs_Water = """From: Your Friendly Neighborhood Pi <raspbpinotice@gmail.com>
To: Caretakers <hahnfrankie@gmail.com, katieamenta@aol.com>
Subject: WATER ME PLEASE

I am so thirsty, please give me something to drink.

Regards,
Your Plant
"""

watered = """From: Your Friendly Neighborhood Pi <raspbpinotice@gmail.com>
To: Caretakers <hahnfrankie@gmail.com, katieamenta@aol.com>
Subject: Thanks

Thank you so much for the delicious water.

Regards,
Your Plant
"""

# email function

def sendEmail(smtp_variable):
    try:
        smtpObj = smtplib.SMTP_SSL(smtp_Host, smtp_port)
        smtpObj.login(smtp_UN, smtp_PW)
        smtpObj.sendmail(smtp_sender, smtp_receiver, smtp_message)
        print("Message Sent")
    except smtplib.SMTPException:
        print("Message Failed to Send")

# GPIO input check function, will be called everytime GPIO is called

def GPIOcheck_One(channel, COUNTER):
    if GPIO.input(channel):
        print "Plant Status: Dehydrated"
        sendEmail(needs_Water)
        COUNTER += 1
    else:
        print "Plant Status: Hydrated"
        sendEmail(watered)
        COUNTER += 1

def GPIOcheck_Two(channel, COUNTER):
    if GPIO.input(channel):
        print "Plant Two Status: Dehydrated"
        sendEmail(needs_Water)
        COUNTER += 1
    else:
        print "Plant Two Status: Hydrated"
        sendEmail(Watered)
        COUNTER += 1

while RUNNING == True

    if COUNTER > 3:
        Print("Maximum Checks have occured, please try again tomorrow")

    else:
        # Detects when change in voltage occurs
        GPIO.add_event_detect(sensor_One, GPIO.BOTH, bouncetime=200)
        #GPIO.add_event_detect(sensor_Two, GPIO.BOTH, bouncetime=600)

        # Executes check functions when change in respective pin occurs
        GPIOP.add_event_callback(sensor_One, GPIOcheck_One)
        #GPIOP.add_event_callback(sensor_Two, GPIOcheck_Two)

    

