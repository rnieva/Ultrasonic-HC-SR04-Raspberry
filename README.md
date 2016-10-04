# Ultrasonic-HC-SR04-Raspberry
(for Beginners and young children)
An easy Python script to get the distance using the HC-SR04 sensor between the sensor and an object.

HC-SR04
Basically this sensor emit high frequency ultrasonic sound, and receive the ultrasonic noise reflected. Later the sensor control calculate he time difference between the signal being transmitted and received, with a math formule the user can get the distance between the sensor and the object.   

1- Connect the sensor to Raspberry Pi in GPIO pins
- GND to GPIO ground (pin 6)
- Echo to GPIO 7 (pin 26). Here we using a 1k resistor within Echo pin and GPIO 7.
- Trig to GPIO 25 (pin 22)
- Vcc to GPIO 5v (pin 4)

*Important: don´t mistake the GPIO pin numbers with physical numbers in the Raspberry

Raspberry Pi Models A and B:
[GPIO pins](https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-gpio-numbers.png) - [Physical pin numbers](https://www.raspberrypi.org/documentation/usage/gpio/images/a-and-b-physical-pin-numbers.png) -  [More info in Raspberry Pi Foundation] (https://www.raspberrypi.org/documentation/usage/gpio/)

![alt tag](https://raw.github.com/rnieva/Ultrasonic-HC-SR04-Raspberry/master/imgRaspberryAndSensor.JPG)

2- Steps in the Raspberry Pi
- sudo apt-get install python or python3
- sudo nano name_of_your_Python_script.py
- Copy the code and save the changes
- python name_of_your_Python_script.py

### Added a LED
The script distance_HCSR04sensorV2.py has a "IF Statement". If the distance is less than a specific value, in this case 10, the LED will switch on.
- LED to GPIO 15 (pin 10), and a 1k resistor between GND and the shorter leg (negative or 0v) of LED.

*LED (Light Emitting Diodes), LEDs only pass electricity one way, so we need to make sure we put them in the right way round. They have a long leg and a slightly shorter leg. The long leg goes to the plus side and the shorter leg to the negative side

![alt tag](https://raw.github.com/rnieva/Ultrasonic-HC-SR04-Raspberry/master/scheme.png)
