#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

"""
NOTES:
The CRT draws one pixel every cycle, each pixel has a specific row, col spot (duh)

The value of the X register determines where a 3-pixel wide sprite is on the CRT

If the sprite is positioned where the CRT is currently drawing one of its 3 pixels,
then the pixel on the CRT is # otherwise it's .

"""

CRT_WIDTH = 40
CRT_PIXELS = "." * (CRT_WIDTH * 6)
CRT_LIT_PIXEL_ENUM = "#"
CRT_LIT_PIXELS_POS = []


def draw_pixel_and_update(cycle, x):
    crt_index = cycle - 1
    horizontal_loc = crt_index % CRT_WIDTH

    if horizontal_loc in [x - 1, x, x + 1]:
        CRT_LIT_PIXELS_POS.append(crt_index)

    print_crt(lit_pixels=CRT_LIT_PIXELS_POS, cycle=cycle)

    return cycle + 1


def print_sprite(x):
    blank_screen = "." * CRT_WIDTH
    sprite_str = blank_screen[:x-1] + "###" + blank_screen[x+2:]
    print(f"Sprite pos: {sprite_str}")
    # print(f"Sprite pos: {blank_screen[:x-1]}###{blank_screen[x+1:]}")


def print_crt(lit_pixels, cycle=240):
    crt_slice = CRT_PIXELS[:cycle]

    for pixel in lit_pixels:
        if pixel < cycle:
            crt_slice = crt_slice[:pixel] + CRT_LIT_PIXEL_ENUM + crt_slice[pixel + 1:]

    if cycle > CRT_WIDTH:
        for crt_row in range(cycle // 40):
            print(f"{crt_slice[crt_row * CRT_WIDTH:(crt_row + 1) * CRT_WIDTH]}")
    else:
        print(f"{crt_slice}")


with open(in_file_name) as cpu_instructions:
    register_x = 1
    cycle_counter = 1

    for command in cpu_instructions:
        cmd_parts = command.split()

        print(f"Start of cycle {cycle_counter}, executing {command.rstrip()}")

        print(f"During cycle {cycle_counter}, drawing pixel {cycle_counter - 1}")
        cycle_counter = draw_pixel_and_update(cycle_counter, register_x)

        if len(cmd_parts) == 1:
            print(f"End of cycle {cycle_counter - 1}, finished with noop")
            continue

        print(f"During cycle {cycle_counter}, drawing pixel {cycle_counter - 1}")
        cycle_counter = draw_pixel_and_update(cycle_counter, register_x)

        v_value = int(cmd_parts[1])
        register_x += v_value
        print(f"End of cycle {cycle_counter - 1}, finished with add {v_value}, register is now {register_x}")
        print_sprite(register_x)

print_crt(lit_pixels=CRT_LIT_PIXELS_POS)
