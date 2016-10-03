# Ultrasonic-HC-SR04-Raspberry
(for Beginners and young children)
A easy Python script to get the distance using the HC-SR04 sensor between the sensor and an object.

HC-SR04
Basically this sensor emit high frequency ultrasonic sound, and receive the ultrasonic noise reflected. Later the sensor control calculate he time difference between the signal being transmitted and received, with a math formule the user can get the distance between the sensor and the object.   

1- Connect the sensor to Raspberry Pi in GPIO pins
- GND to GPIO ground pin
- Echo to GPIO 7 pin. Here we using a 1k resistor within Echo pin and GPIO 7.
- Trig to GPIO 25 pin
- Vcc to GPIO 5v

*Important: don´t mistake the GPIO pin numbers with physical numbers in the Raspberry

[GPIO pins](https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-gpio-numbers.png)

[Physical pin numbers](https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-physical-pin-numbers.png)

![alt tag](https://raw.github.com/rnieva/Ultrasonic-HC-SR04-Raspberry/master/imgRaspberryAndSensor.JPG)

2- Steps in the Raspberry Pi
- sudo apt-get install python or python3
- sudo nano name_of_your_Python_script.py
- Copy the code and save the changes
- python name_of_your_Python_script.py
