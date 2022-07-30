import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add

                                                                                        
pausetime = 1

async def ambientLight0(lights):

    loop = PeriodicLoop(3, 150)

    while not loop.done():
        for i in range(24):
            rr = random.randint(0,255)
            gr = random.randint(0,255)
            br = random.randint(0,255)
            #rr = 255
            #gr = 0
            #br = 0
            lights[i].set_state(raw_rgb(rr,gr,br))

        await loop.next()

#ukraine flag
async def ambientLight1(lights):

    loop = PeriodicLoop(3, 150)

    while not loop.done():
        for i in range(24):
            if i<12:
                rr = 0 
                gr = 0
                br = 255
            else:
                rr = 255 
                gr = 255
                br = 0
            lights[i].set_state(raw_rgb(rr,gr,br))

        await loop.next()

#mix em
async def ambientLight(lights):

    loop = PeriodicLoop(4, 150)
    u = 0
    while not loop.done():
        for i in range(24):
            if u % 2 ==  0:
                if i<12:
                    rr = 0 
                    gr = 0
                    br = 255
                else:
                    rr = 255 
                    gr = 255
                    br = 0
            else:
                rr = random.randint(0,255)
                gr = random.randint(0,255)
                br = random.randint(0,255)
                
            lights[i].set_state(raw_rgb(rr,gr,br))
        u += 1
        await loop.next()
