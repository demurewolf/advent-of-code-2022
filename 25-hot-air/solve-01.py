#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

BASE_POWERS = [5 ** i for i in range(15)]


# At each digit d, we need to know how many 5^d to add/remove
# The first digit will always be at least 1 or 2
def snafu_to_int(snafu_num: str) -> int:
    curr_power = len(snafu_num) - 1
    ret_num = 0

    for d in snafu_num:
        switcher = {
            "2": 2,
            "1": 1,
            "0": 0,
            "-": -1,
            "=": -2
        }
        ret_num += switcher[d] * (5 ** curr_power)
        curr_power -= 1

    return ret_num

# I needed to look up some resources to figure this part out...
# dont we all
def int_to_snafu(num: int) -> str:
    snafu = ""
    carry = 0

    switcher = {
        2: "2",
        1: "1",
        0: "0",
        3: "=",
        4: "-",
        5: "0"
    }

    while num > 0:
        x = num % 5 + carry
        snafu += switcher[x]
        carry = 1 if x > 2 else 0
        num = num // 5

    return ''.join(reversed(snafu))


print(snafu_to_int("2=-01"))

print(int_to_snafu(2))
print(int_to_snafu(8))

total_fuel = 0
with open(in_file_name) as fuel_file:
    for line in fuel_file:
        if line.rstrip():
            total_fuel += snafu_to_int(line.rstrip())

print(total_fuel)
print(int_to_snafu(total_fuel))
