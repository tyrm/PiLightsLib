#!/usr/bin/env python3

def decode_rgba32(c):
    red = (c & 0xFF000000) >> 24
    green = (c & 0xFF0000) >> 16
    blue = (c & 0xFF00) >> 8
    alpha = c & 0xFF

    return [red, green, blue, alpha]


# Create a "color grid" array with optional fill
def make_color_grid(x, y, r=0, g=0, b=0):
    return [[[r, g, b] for _ in range(y)] for _ in range(x)]


def rgba32(r, g, b, a=0):
    color = a
    color += b << 8
    color += g << 16
    color += r << 24

    return color


def scale(value, input_low, input_high, output_low, output_high):
    return ((value - input_low) / (input_high - input_low)) * (output_high - output_low) + output_low
