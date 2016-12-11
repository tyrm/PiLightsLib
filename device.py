#!/usr/bin/env python3

from .util import make_color_grid

# Base Device Object
class DeviceObj:
    def __init__(self, name, t, x=1, y=1):
        # Save Parameters
        self.width = x
        self.height = y
        self.name = name
        self.type = t

        # Build Light array
        self._lights = make_color_grid(self.width, self.height)
        self._showBuffer = make_color_grid(self.width, self.height)

    def __str__(self):
        return "{0} ({1}, {2}x{3})".format(self.name, self.type, self.width, self.height)

    def get(self, x=0, y=0):
        r = self._lights[x][y][0]
        g = self._lights[x][y][1]
        b = self._lights[x][y][2]
        return [r, g, b]

    def get_size(self):
        return [self.width, self.height]

    def set(self, r, g, b, x=0, y=0):
        self._showBuffer[x][y][0] = r
        self._showBuffer[x][y][1] = g
        self._showBuffer[x][y][2] = b

    def show(self):
        self._lights = self._showBuffer
