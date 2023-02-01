# Pico-LED-Example-With-JQuery
This project uses the Raspberry Pi Projects Pico W tutorial and adds CSS and JQuery. The original tutorial did not use JQuery and CSS so I created this for anyone who is starting with the Pico W.

## Getting Started

First, make sure the Pico W is set up. Hold the Bootsel button then connect the Micro USB cable. Then go to the `INDEX.HTM` file and click on it. Then find the Pico W UF2 file and download it. Drag it to the Pico and then it'll vanish. Then make sure to have Thonny installed and opened and then switch to MicroPython. Then you can clone this repo, and save the files to the Pico. Then run it and go to the IP address you get and then if you get the image shown below then click the button and you should be able to turn on and off the internal LED.

![Pico](https://github.com/sentairanger/Pico-LED-Example-With-JQuery/blob/main/pico-w.png)

## Running code on boot and touch screen support

To run code on boot rename the code to `main.py`. For touch screen support rename mousedown and mouseup to touchstart and touchend.
