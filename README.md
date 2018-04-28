So what?
===========
Sid-on-Air uses Arduino StereoSid to enable retro-SID WiFi music!


Getting Started
==================
Take a look at
https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
https://github.com/espressif/esptool/

Setup
================
You need an Arduino uno and an esp8266, connected via a I2C bus.

## Arduino setup as a Sid slave
Download https://github.com/daitangio/sid-arduino-lib
(at least version 2.0.5)
Flash the arduino with the SID_I2C_receiver.ino

## Esp8266
Connect ESP8266 pin GPIO 12 (D6) to Arduino A4 (will be I2C SDA)
Connect pin GPIO 13 (D7) to Arduino A5
Link GND of ESP8266 and Arduino together

## How to test your setup
My sugested setup is to provide 6V to Arduino, and provide power to
esp8266 via USB port while developing.

