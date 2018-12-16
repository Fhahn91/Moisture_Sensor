#!/usr/bin/python

# Importing libraries to be used.

import RPi.GPIO as GPIO # A Rasp. Pi GPIO pin library
import smtplib # To send emails from the Rasp. Pi
import time # Standard time library

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Defining Channels used
sensor_One = 17
sensor_Two = 5

# Setting GPIO Pins to Input
GPIO.setup(sensor_One, GPIO.IN)
GPIO.setup(sensor_Two, GPIO.IN)

#######PLACE HOLDER LOOP/COUNTER############
RUNNING = True
####################################

# SMTP sending info
smtp_UN = "email"
smtp_PW = "password"
smtp_Host = "smtp.gmail.com"
smtp_port = 465

smtp_sender = "email"
smtp_receiver = [ 'email' ]

# Messages

needs_WaterOne = """From: Your Friendly Neighborhood Pi <raspbpinotice@gmail.com>
To: Caretakers <.
Subject: Basil Needs Water

Please....water....dying.....

Regards,
Your Basil Plant
"""

wateredOne = """From: Your Friendly Neighborhood Pi <raspbpinotice@gmail.com>
To: Caretakers <>
Subject: Thanks

Thanks for the water.

Regards,
Your Basil Plant
"""

needs_WaterTwo = """From: Your Friendly Neighborhood Pi <raspbpinotice@gmail.com>
To: Caretaker <>
Subject: Thyme Needs Water

Please...water..dying....

Regards,
Your Thyme Plant
"""

wateredTwo = """From: Your Friendly Neighborhood Pi <raspbpinotice@gmail.com>
To: Caretaker <>
Subject: Thanks

Thanks for the water.

Regards,
Your Thyme Plant
"""

# email function

def sendEmail(smtp_message):
    try:
        smtpObj = smtplib.SMTP_SSL(smtp_Host, smtp_port)
        smtpObj.login(smtp_UN, smtp_PW)
        smtpObj.sendmail(smtp_sender, smtp_receiver, smtp_message)
        print("Message Sent")
    except smtplib.SMTPException:
        print("Message Failed to Send")

# GPIO input check function, will be called everytime GPIO is called

def GPIOcheck_One(channel):
    if GPIO.input(channel):
        print "Plant One Status: Dehydrated"
        sendEmail(needs_WaterOne)
	print(time.ctime())
    else:
        print "Plant One Status: Hydrated"
        sendEmail(wateredOne)
	print(time.ctime())

def GPIOcheck_Two(channel):
    if GPIO.input(channel):
        print "Plant Two Status: Dehydrated"
        sendEmail(needs_WaterTwo)
	print(time.ctime())
    else:
        print "Plant Two Status: Hydrated"
        sendEmail(wateredTwo)
	print(time.ctime())

# Detects when change in voltage occurs
GPIO.add_event_detect(sensor_One, GPIO.BOTH, bouncetime=200)
GPIO.add_event_detect(sensor_Two, GPIO.BOTH, bouncetime=400)

# Executes check functions when change in respective pin occurs
GPIO.add_event_callback(sensor_One, GPIOcheck_One)
GPIO.add_event_callback(sensor_Two, GPIOcheck_Two)

# Loop that keeps script running
while RUNNING == True:
	time.sleep(0.2)
