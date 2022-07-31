import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add


async def slider(lights):
    shots = []

    loop = PeriodicLoop(0.01)

    palettes = [snow_palette, red_palette, yellow_palette]
    palette_index = 0

    background = [random.choice(snow_palette) for _ in range(24)]
    wave_color = red_palette[0]

    slider_index = 0

    def render():
        for index, light in enumerate(lights):
            slider_index = int(mouse()[0] / 1000)
            if 0 <= (index - slider_index) % 24 <= 3:
                light.set_state(wave_color)
            else:
                light.set_state(background[index])

    loop = PeriodicLoop(0.1)
    while not loop.done():
        render()

        for click in clicks():
            wave_color = palettes[palette_index][0]
            palette_index = (palette_index + 1) % len(palettes)
            background = [random.choice(palettes[palette_index]) for _ in range(24)]

        await loop.next()
