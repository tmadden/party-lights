import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add


async def color_slider(lights):
    shots = []

    offsets = [random.randint(0, 31) for _ in range(24)]
    off_component = [random.randint(0, 31) for _ in range(24)]

    rgb_index = 0

    def render():
        for index, light in enumerate(lights):
            slider_index = int(mouse()[0] / 10) % 224
            rgb = [0, 0, 0]
            rgb[0] = int((offsets[index] + slider_index) / 16) * 16
            rgb[1] = 255 - rgb[0]
            rgb[2] = off_component[index]
            light.set_state(raw_rgb(rgb[rgb_index % 3], rgb[(rgb_index + 1) % 3], rgb[(rgb_index + 2) % 3]))

    loop = PeriodicLoop(0.1)
    while not loop.done():
        render()

        for click in clicks():
            rgb_index += 1

        await loop.next()
