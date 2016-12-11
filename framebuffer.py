#!/usr/bin/env python3

from threading import Lock
from .util import make_color_grid

# Thread Safe Buffer for Frames
class FrameBuffer:
    def __init__(self, x, y):
        self._bufferLock = Lock()
        self._buffer = make_color_grid(x, y)

    def set(self, b):
        with self._bufferLock:
            self._buffer = b

    def get(self):
        with self._bufferLock:
            return self._buffer

    def set_pixel(self, x, y, r, g, b):
        with self._bufferLock:
            self._buffer[x][y] = [r, g, b]

    def get_size(self):
        with self._bufferLock:
            width = len(self._buffer)
            height = len(self._buffer[0])

            return [width, height]