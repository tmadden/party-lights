import asyncio
import time
import random
from colour import Color

from utilities import *

from operator import add

# async def progression(lights):
#     loop = PeriodicLoop(0.1, 10)
#     index = 0
#     while not loop.done():
#         lights[(index - 4) % 24].set_state(off)
#         lights[index % 24].set_state(on)
#         index += 1
#         await loop.next()


async def progression(lights):
    loop = PeriodicLoop(0.1, 40)
    for light in lights:
        light.set_state(dim(random.choice(palette), 0.1))
    index = 0
    while not loop.done():
        old_index = (index - 4) % 24
        lights[old_index].set_state(dim(random.choice(palette), 0.1))
        lights[index % 24].set_state(dim(pretty, 0.1))
        index += 1
        await loop.next()


# async def progression(lights):
#     shots = []

#     background = [random.choice(palette) for _ in range(24)]
#     for index, light in enumerate(lights):
#         light.set_state(background[index])

#     loop = PeriodicLoop(0.1, 40)
#     while not loop.done():
#         if random.random() < 0.1:
#             shots.append(random.choice([[0, 1, pretty], [23, -1, raw_rgb(150, 100, 0)]]))
#         print('---')
#         print(shots)
#         for shot in shots:
#             lights[(shot[0] - shot[1]) % 24].set_state(background[shot[0]])
#             shot[0] += shot[1]
#         shots = list(filter(lambda shot: 0 <= shot[0] <= 23, shots))
#         print(shots)
#         for shot in shots:
#             lights[(shot[0] + shot[1]) % 24].set_state(shot[2])
#         await loop.next()
