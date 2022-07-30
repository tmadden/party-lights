import yaml
import asyncio
import time
import random
from utilities import reset_all
import utilities

from light import Light

# from patterns.connect_four import connect_four
# from patterns.ramp_up import ramp_up
from patterns.progression import progression
from patterns.random_lizard import random_lizard
from patterns.ambient_light import ambient_light
# from patterns.snake import snake
# from patterns.pulsate import pulsate
# from patterns.ferris import ferris
# from patterns.tictac import tictactoe

test_pattern = None

all_patterns = [progression, ambient_light]

current_pattern_index = 0


async def control_loop(lights):
    global current_pattern_index

    if test_pattern:
        await test_pattern(lights)
        reset_all(lights)
        await asyncio.sleep(1)
    else:
        while True:
            utilities.interrupt_pattern_loop = False
            await all_patterns[current_pattern_index](lights)


async def main():
    with open("ips.yml", "r") as file:
        ips = yaml.safe_load(file)

    lights = [Light(ip) for ip in ips]

    await asyncio.gather(*[light.connect() for light in lights])

    await asyncio.gather(control_loop(lights),
                         *[light.comm_loop() for light in lights])


from pynput import mouse


def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    print(button)


def on_scroll(x, y, dx, dy):
    global current_pattern_index
    current_pattern_index = (current_pattern_index + dy) % len(all_patterns)
    utilities.interrupt_pattern_loop = True


mouse_listener = mouse.Listener(on_move=on_move,
                                on_click=on_click,
                                on_scroll=on_scroll,
                                suppress=True)
mouse_listener.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
