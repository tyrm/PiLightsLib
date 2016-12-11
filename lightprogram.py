#!/usr/bin/env python3

from .util import make_color_grid

class LightProgram:
    def __init__(self, w, h):
        self.current_frame = []
        self.last_w = w
        self.last_h = h

    def get_next_frame(self, w, h):
        next_frame = make_color_grid(w, h)

        self.current_frame = next_frame
        return self.current_frame
