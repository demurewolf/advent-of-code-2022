#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
# in_file_name = "puzzle-input.txt"

# signals = []
#
#
# def check_and_sample_signal(cycle, register):
#     if (cycle + 20) % 40 == 0:
#         print(f"Sampling at cycle {cycle}")
#         print(f"Register is {register}")
#         signals.append(cycle * register)

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
    horizontal_loc = cycle % CRT_WIDTH

    if horizontal_loc in [x - 1, x, x + 1]:
        CRT_LIT_PIXELS_POS.append(crt_index)

    return cycle + 1


with open(in_file_name) as cpu_instructions:
    register_x = 1
    cycle_counter = 1

    for command in cpu_instructions:
        cmd_parts = command.split()

        if len(cmd_parts) > 1:
            v_value = int(cmd_parts[1])
            cycle_counter = draw_pixel_and_update(cycle_counter, register_x)
            register_x += v_value

        cycle_counter = draw_pixel_and_update(cycle_counter, register_x)


for lit_pixel_pos in CRT_LIT_PIXELS_POS:
    CRT_PIXELS = CRT_PIXELS[:lit_pixel_pos] + CRT_LIT_PIXEL_ENUM + CRT_PIXELS[lit_pixel_pos + 1:]

print(f"Finished with {cycle_counter} cycles completed")
# print(f"{CRT_PIXELS}")
for r in range(6):
    print(f"{CRT_PIXELS[r * CRT_WIDTH:(r + 1) * CRT_WIDTH]}")
