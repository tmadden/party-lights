import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add

nl = 24

#whole_lizard = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'bp', 'bo', 'po' ]

wl = ['g'] * 21 + ['bp', 'bo', 'po']
sl = ['g'] * 2 + ['bp', 'bo', 'po']

#c = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'bp', 'bo', 'po' ]

#pass setstate rgb(255, 255, 255)

cdic = {
    'g': rgb(0, 255, 0),
    'po': rgb(230, 25, 100),
    'bp': rgb(20, 125, 10),
    'bo': rgb(5, 5, 22)
}

pausetime = 1


async def whole_lizard(lights):

    #display whole lizard

    for i in range(len(wl)):
        lights[i].set_state(dim(cdic[wl[i]], 0.2))

    await asyncio.sleep(4)

    #shut down the whole lizard
    for i in range(len(wl)):
        lights[i].set_state(off)

    #small lizard wiggle
    loop = PeriodicLoop(2, 5)
    lasts = 0
    while not loop.done():
        s = random.randint(0, 24 - len(sl))
        for i in range(len(sl)):
            lights[lasts + i].set_state(off)

        for i in range(len(sl)):
            lights[s + i].set_state(cdic[sl[i]])

        lasts = s
        await loop.next()

    #small lizard run
    loop = PeriodicLoop(1, 12)
    lasts = 0
    while not loop.done():
        s = (lasts + 1) % 24
        for i in range(len(sl)):
            lights[lasts + i].set_state(off)

        for i in range(len(sl)):
            lights[s + i].set_state(cdic[sl[i]])

        lasts = s
        await loop.next()
