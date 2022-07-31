import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add

async def progression(lights):
    loop = PeriodicLoop(0.01)

    palettes = [snow_palette, red_palette]
    palette_index = 0

    background = [random.choice(snow_palette) for _ in range(24)]
    wave_color = red_palette[0]

    index = -1
    direction = 0.1
    while not loop.done():
        for i in range(24):
            if 0 <= (i - int(index)) <= 3:
                lights[i].set_state(wave_color)
            else:
                lights[i].set_state(background[i])

        index += direction
        if index < -1:
            index = -1
            direction = 0.1
        if index >= 21:
            index = 21
            direction = -0.1

        for click in clicks():
            wave_color = palettes[palette_index][0]
            palette_index = (palette_index + 1) % len(palettes)
            background = [random.choice(palettes[palette_index]) for _ in range(24)]

        await loop.next()


async def no_progression(lights):
    loop = PeriodicLoop(0.01)
    palettes = [snow_palette, red_palette]
    palette_index = 0

    background = [random.choice(snow_palette) for _ in range(24)]
    wave_color = red_palette[0]

    while not loop.done():
        for i in range(24):
            lights[i].set_state(background[i])

        for click in clicks():
            wave_color = palettes[palette_index][0]
            palette_index = (palette_index + 1) % len(palettes)
            background = [random.choice(palettes[palette_index]) for _ in range(24)]

        await loop.next()
