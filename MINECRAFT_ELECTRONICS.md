# Electronics / GPIO (General Purpose IO)

## Introduction

A **Breadboard** is a reusbale device with a number of holes into which you push wires or components to create circuits. Breadboards  allow you to create circuits without needing to solder all the components. The two rows of holes at the top and bottom are for power.

**Voltage** is the difference in electrical energy between two points in a circuit. This difference allows current to flow in a circuit, like water pressure in pipes. Voltage is measured in volts (V).

An **LED** (Light-Emitting Diode) ligts up when electricty passes through it. A diode only allows current to pass in one direction and will only light up if you pass your current in the correct direction. LEDs have one short leg (cathode or negative) and one long leg (anode or positive).

A **resistor** resists or limits current in a circuit. An LED can be damaged by too much current and adding a resistor of the correct value will limit the amount of current and the LED will be protected. Resistance is measured in Ohms and the value of a resistor is shown by coloured bands that are read from left to right. You can read more about color code on [wikipedia](https://en.wikipedia.org/wiki/Electronic_color_code). 

A **current** is the rate at which electrical energy flows through a circuit and is measured in amperes (A) or amps. Smaller currents are measured in milliApms (mA). You can read more about circuits [here](http://www.allaboutcircuits.com/textbook/direct-current/#chpt-1).

## A simple circuit

- Connect an LED, a 330 Ohm resistor and two short wires to the positive + (red line) and negative - (blue line) rows as shown below.

**IMAGE**

## A programmable circuit

- Connect the positive + wire to GPIO pin 17.
- Run [led.py](scripts/intro.py)

```python
import RPi.GPIO as GPIO
import time

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)  # setup for output

GPIO.output(LED, True)
time.sleep(1.0)

GPIO.cleanup()  # reset GPIO and disble circuitry
```

- Explain setup, output and cleanup.
- :bulb: Make your LED flash forever: [led_flash.py](scripts/led_flash.py)
- :bulb: Make your LED flash only 3 times.
