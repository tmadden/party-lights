import asyncio
import math
import time

from pywizlight.rgbcw import rgb2rgbcw

mouse_position = [0, 0]


def mouse():
    return mouse_position


mouse_clicks = []


def clicks():
    new_clicks = mouse_clicks.copy()
    mouse_clicks.clear()
    return new_clicks


def index(p):
    return p[0] * 4 + p[1]


def in_bounds(p):
    return p[0] >= 0 and p[0] < 4 and p[1] >= 0 and p[1] < 4


def flipped(v):
    return [-v[0], -v[1]]


def equal(a, b):
    return round(a[0]) == round(b[0]) and round(a[1]) == round(b[1])


def reset_all(lights):
    for light in lights:
        light.set_state(off)


interrupt_pattern_loop = False


class PeriodicLoop:
    def __init__(self, period, length=None):
        self.period = period
        self.next_frame_time = time.perf_counter()
        if length:
            self.finish_time = self.next_frame_time + length
        else:
            self.finish_time = None

    async def next(self):
        self.next_frame_time += self.period
        now = time.perf_counter()
        while now < self.next_frame_time and not interrupt_pattern_loop:
            await asyncio.sleep(0.005)
            now = time.perf_counter()

    def done(self):
        if interrupt_pattern_loop:
            return True
        if self.finish_time:
            return self.next_frame_time >= self.finish_time
        return False


def raw_rgb(r, g, b):
    return {'r': r, 'g': g, 'b': b}


def rgb(r, g, b):
    rgb, cw = rgb2rgbcw((r, g, b))
    red, green, blue = rgb
    state = {'r': r, 'g': g, 'b': b}
    if cw:
        state['c'] = cw
        state['w'] = cw
    return state


def color(c):
    return rgb(round(c.red * 255), round(c.green * 255), round(c.blue * 255))


def dim(c, intensity):
    # return {**{key: value * intensity for (key, value) in c.items()}, 'brightness': intensity}
    return {**c, 'brightness': intensity}


on = {'c': 255, 'w': 255}
off = None

cold_white = {'c': 255}
warm_white = {'w': 255}

light_gorgeous = raw_rgb(128, 0, 255)
gorgeous = raw_rgb(160, 0, 255)
snowy = raw_rgb(32, 32, 255)
blue_snowy = raw_rgb(8, 8, 255)
pretty = raw_rgb(255, 0, 64)
good_purple = raw_rgb(123, 0, 255)

palette = [light_gorgeous, gorgeous, snowy, good_purple]
