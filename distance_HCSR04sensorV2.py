#!/usr/bin/env python
# -*- coding: utf-8 -*-    #Read ASCII character
import RPi.GPIO as GPIO    #Import GPIO lib
import time                #Import time (time.sleep)
GPIO.setmode(GPIO.BCM)     #Setup mode BCM
GPIO_TRIGGER = 25          #pin GPIO 25 as TRIGGER
GPIO_ECHO    = 7           #pin GPIO 7 as ECHO
GPIO_LED     = 15          #pin GPIO 15 as LED
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Setup Trigger as out
GPIO.setup(GPIO_ECHO,GPIO.IN)      #Setup Echo as in
GPIO.setup(GPIO_LED,GPIO.OUT)      #Setup Led as out
GPIO.output(GPIO_TRIGGER,False)    #Setup pin 25 as LOW
GPIO.output(GPIO_LED,0)            #init off

try:
    while True:     #init loop
        GPIO.output(GPIO_TRIGGER,True)   #Send a ultrasonic pulse
        time.sleep(0.00001)              #pause
        GPIO.output(GPIO_TRIGGER,False)  #switch off the pulse
        start = time.time()              #Save the time with time.time()
        while GPIO.input(GPIO_ECHO)==0:  #while the sensor doesn´t get signal
            start = time.time()          #keep the time with time.time()
        while GPIO.input(GPIO_ECHO)==1:  #If the sensor get signal
            stop = time.time()           #Save the time in stop value
        elapsed = stop-start             #Get the different within times
        distance = (elapsed * 34300)/2   #Distance,Time, Speed,  D = (T x V)/2
        print distance                   #Show the distance in cm
        var = 10                         #the value to switch the LED
        if distance < var:
                GPIO.output(GPIO_LED,1)  #seet on if distance < value
        else:
                GPIO.output(GPIO_LED,0)
        time.sleep(1)
except KeyboardInterrupt:                #CONTROL+C
    print "quit"                         #Show msg to user
    GPIO.cleanup()                       #Clean Pin and exit

