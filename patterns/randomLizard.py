import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add

nl = 24

#wholelizard = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'bp', 'bo', 'po' ]

wholelizard = ['g'] * 21 + ['bp', 'bo', 'po']

c = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'bp', 'bo', 'po' ]

#pass setstate rgb(255, 255, 255)

cdic = {'g': raw_rgb(0, 255, 0), 'po': raw_rgb(230, 25, 100), 'bp': raw_rgb(20, 125, 10), 'bo': raw_rgb(5, 5, 220)}

pausetime = 1

async def randomLizard(lights):
    loop = PeriodicLoop(5, 100)
    lasts = 0
    while not loop.done():
        s = random.randint(0,24-len(c))
        print(s)
        for i in range(len(c)):
            #print(cdic[c[i]])
            #print(i)
            lights[lasts+i].set_state(off)

        for i in range(len(c)):
            #print(cdic[c[i]])
            #print(i)
            lights[s+i].set_state(cdic[c[i]])

        lasts = s
        await loop.next()
