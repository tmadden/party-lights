import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add


async def ambient_light(lights):

    loop = PeriodicLoop(4, 150)
    u = 0
    while not loop.done():
        for i in range(24):
            if u % 2 == 0:
                if i < 12:
                    rr = 0
                    gr = 0
                    br = 255
                else:
                    rr = 255
                    gr = 255
                    br = 0
            else:
                rr = random.randint(0, 255)
                gr = random.randint(0, 255)
                br = random.randint(0, 255)

            lights[i].set_state(raw_rgb(rr, gr, br))
        u += 1
        await loop.next()
