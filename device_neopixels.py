#!/usr/bin/env python3

from neopixel import *

from lights import DeviceObj


# UnicornHat Object
class NeoPixels(DeviceObj):
    def __init__(self, name, count, bri=255, grb=False):
        DeviceObj.__init__(self, name, "neopixel", count)

        # LED strip configuration:
        pin = 18  # GPIO pin connected to the pixels (must support PWM!).
        freq_hz = 800000  # LED signal frequency in hertz (usually 800khz)
        dma = 5  # DMA channel to use for generating signal (try 5)
        invert = False  # True to invert the signal (when using NPN transistor level shift)

        # Create NeoPixel object with appropriate configuration.
        self.grb = grb
        self.strip = Adafruit_NeoPixel(count, pin, freq_hz, dma, invert, bri)

        self.strip.begin()

    def set(self, r, g, b, x=0, y=0):
        DeviceObj.set(self, r, g, b, x, y)

        # Set Pixel
        if not self.grb:
            self.strip.setPixelColor(x, Color(r, g, b))
        else:
            self.strip.setPixelColor(x, Color(g, r, b))

    def show(self):
        DeviceObj.show(self)

        # Update Display
        self.strip.show()
