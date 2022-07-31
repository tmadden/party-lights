import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add

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

async def shots(lights):
    shots = []

    background = [random.choice(snow_palette) for _ in range(24)]
    for index, light in enumerate(lights):
        light.set_state(background[index])

    loop = PeriodicLoop(0.1)
    while not loop.done():
        for click in clicks():
            shots.append([0, 1, pretty])
        if random.random() < 0.05:
            shots.append([23, -1, raw_rgb(150, 100, 0)])
        for shot in shots:
            lights[(shot[0] - shot[1]) % 24].set_state(background[shot[0]])
            shot[0] += shot[1]
        shots = list(filter(lambda shot: 0 <= shot[0] <= 23, shots))
        for shot in shots:
            lights[(shot[0] + shot[1]) % 24].set_state(shot[2])
        await loop.next()
