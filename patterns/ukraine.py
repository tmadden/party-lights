import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add


async def ukraine(lights):

    loop = PeriodicLoop(0.01)
    u = 0
    while not loop.done():
        for i in range(24):
            if (i < 12) == (u % 2 == 0):
                rr = 0
                gr = 0
                br = 255
            else:
                rr = 255
                gr = 213
                br = 0

            lights[i].set_state(raw_rgb(rr, gr, br))

        for click in clicks():
            u += 1
        await loop.next()
