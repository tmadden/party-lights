import yaml
import asyncio
import time
import random
from utilities import reset_all
import utilities

from light import Light

# from patterns.connect_four import connect_four
from patterns.progression import progression, no_progression
from patterns.random_lizard import random_lizard
from patterns.ambient_light import ambient_light
from patterns.ukraine import ukraine
from patterns.slider import slider
from patterns.color_slider import color_slider
from patterns.sparkle import sparkle
from patterns.shots import shots

test_pattern = None

all_patterns = [progression, slider, shots, color_slider, sparkle, ukraine]

current_pattern_index = 0


async def control_loop(lights):
    global current_pattern_index

    while True:
        utilities.interrupt_pattern_loop = False
        utilities.mouse_clicks.clear()
        if test_pattern:
            await test_pattern(lights)
        else:
            await all_patterns[current_pattern_index](lights)


async def main():
    with open("ips.yml", "r") as file:
        ips = yaml.safe_load(file)

    lights = [Light(ip) for ip in ips]

    await asyncio.gather(*[light.connect() for light in lights])

    await asyncio.gather(control_loop(lights),
                         *[light.comm_loop() for light in lights])


from pynput import mouse

mouse_controller = mouse.Controller()


def on_move(x, y):
    utilities.mouse_position[0] += x
    utilities.mouse_position[1] += y
    if [x, y] != [0, 0]:
        mouse_controller.position = (0, 0)


def on_click(x, y, button, pressed):
    if pressed:
        if button == mouse.Button.left:
            utilities.mouse_clicks.append(button)
        elif button == mouse.Button.right:
            global current_pattern_index
            current_pattern_index = (current_pattern_index + 1) % len(all_patterns)
            utilities.interrupt_pattern_loop = True



mouse_listener = mouse.Listener(on_move=on_move,
                                on_click=on_click,
                                suppress=True)
mouse_listener.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
