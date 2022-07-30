import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add


async def slider(lights):
    shots = []

    background = [random.choice(palette) for _ in range(24)]

    def render():
        for index, light in enumerate(lights):
            slider_index = int(mouse()[0] / 1000)
            if 0 <= (slider_index - index) % 24 <= 3:
                light.set_state(pretty)
            else:
                light.set_state(background[index])

    loop = PeriodicLoop(0.1)
    while not loop.done():
        render()
        await loop.next()
