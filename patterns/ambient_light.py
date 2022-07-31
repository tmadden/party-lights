import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add


async def ambient_light(lights):

    colors = []

    def set_colors():
        nonlocal colors
        colors = []
        for i in range(24):
            rr = random.randint(0, 255)
            gr = random.randint(0, 255)
            br = random.randint(0, 255)
            colors.append(raw_rgb(rr, gr, br))

    set_colors()

    loop = PeriodicLoop(1)
    while not loop.done():
        for i in range(24):
            lights[i].set_state(colors[i])

        for click in clicks():
            set_colors()

        await loop.next()
