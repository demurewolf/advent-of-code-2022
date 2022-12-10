#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"
signals = []


def check_and_sample_signal(cycle, register):
    if (cycle + 20) % 40 == 0:
        print(f"Sampling at cycle {cycle}")
        print(f"Register is {register}")
        signals.append(cycle * register)


with open(in_file_name) as cpu_instructions:
    register_x = 1
    cycle_counter = 0

    for command in cpu_instructions:
        cycle_counter += 1
        check_and_sample_signal(cycle_counter, register_x)
        cmd_parts = command.split()
        if cycle_counter > 215:
            print("checking now")

        if len(cmd_parts) > 1:
            v_value = int(cmd_parts[1])
            cycle_counter += 1
            check_and_sample_signal(cycle_counter, register_x)
            register_x += v_value



print(f"The total signals samples is {signals}")
print(f"The sum of signals is {sum(signals)}")