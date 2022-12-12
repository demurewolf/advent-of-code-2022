#!/usr/bin/env python3.8

from math import pow, gcd

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

# Monkey keys available
KEY_ID = "id"
KEY_ITEMS = "items"
KEY_OPERATION = "operation"
KEY_OPERATION_ARGUMENT = "op-arg"
KEY_TEST = "test"
KEY_TRUE_TEST = "true-test"
KEY_FALSE_TEST = "false-test"
KEY_DIVISOR = "divisor"
KEY_INSPECTION_COUNT = "inspection"


def init_monkeys():
    monkeys = []

    with open(in_file_name) as monkey_file:
        curr_monkey = {}

        for line in monkey_file:
            line = line.strip()
            # print(line)

            if line.startswith("Monkey"):
                curr_monkey[KEY_ID] = int(line.split()[1].rstrip(":"))
                curr_monkey[KEY_INSPECTION_COUNT] = 0

            elif line.startswith("Starting"):
                curr_monkey[KEY_ITEMS] = []
                parts = line.split()

                for p in parts[2:]:
                    curr_monkey[KEY_ITEMS].append(int(p.rstrip(",")))

            elif line.startswith("Operation"):
                parts = line.split()
                arg2 = parts[5]

                if parts[4] == "+":
                    def monkey_sum(old_worry, arg):
                        # print(f"Worry is increased by {arg} to {old_worry + arg}")
                        return old_worry + arg
                    curr_monkey[KEY_OPERATION] = monkey_sum
                    curr_monkey[KEY_OPERATION_ARGUMENT] = int(arg2)

                elif parts[4] == "*" and arg2 == "old":
                    def monkey_square(old_worry, extra=0):
                        # print(f"Worry is squared to {old_worry * old_worry}")
                        return pow(old_worry, 2)
                    curr_monkey[KEY_OPERATION] = monkey_square
                    curr_monkey[KEY_OPERATION_ARGUMENT] = 0

                elif parts[4] == "*":
                    def monkey_multiply(old_worry, arg):
                        # print(f"Worry is multiplied by {arg} to {old_worry * arg}")
                        return int(old_worry * arg)
                    curr_monkey[KEY_OPERATION] = monkey_multiply
                    curr_monkey[KEY_OPERATION_ARGUMENT] = int(arg2)

            elif line.startswith("Test"):
                divisor = int(line.split()[3])

                def monkey_test(worry, div):
                    return worry % div == 0

                curr_monkey[KEY_TEST] = monkey_test
                curr_monkey[KEY_DIVISOR] = divisor

            elif line.startswith("If"):
                next_monkey_id = int(line.split()[5])
                if line.startswith("If true:"):
                    curr_monkey[KEY_TRUE_TEST] = next_monkey_id
                elif line.startswith("If false:"):
                    curr_monkey[KEY_FALSE_TEST] = next_monkey_id

            else:
                # Finished reading info about current monkey
                monkeys.append(curr_monkey)
                curr_monkey = {}

    # Add final monkey to monkey list
    monkeys.append(curr_monkey)

    return len(monkeys), monkeys


def print_monkey_items(monkeys):
    for m in monkeys:
        print(f"Monkey {m[KEY_ID]}: {m['items']}")


def print_monkey_inspections(monkeys):
    for m in monkeys:
        print(f"Monkey {m[KEY_ID]}: inspected items {m[KEY_INSPECTION_COUNT]} times")


def compute_lcm(divisors):
    print(divisors)
    maybe_lcm = max(divisors)
    while True:
        divisible_check = True
        for d in divisors:
            if maybe_lcm % d:
                divisible_check = False
                break
        if divisible_check:
            lcm = maybe_lcm
            break
        maybe_lcm += 1
    return lcm


MAX_MONKEYS, all_monkeys = init_monkeys()

print(f"Read {MAX_MONKEYS} total monkeys")

MAX_ROUNDS = 10000
# MAX_ROUNDS = 20
# MAX_ROUNDS = 1

LCM = compute_lcm([m[KEY_DIVISOR] for m in all_monkeys])
print(f"LCM of these monkeys is {LCM}")

for r in range(MAX_ROUNDS):
    for monkey in all_monkeys:
        # print(f"On monkey {monkey[KEY_ID]}")
        # Monkey inspects and throws all items it's holding one at a time
        monkey[KEY_ITEMS].reverse()
        while len(monkey[KEY_ITEMS]):
            item = monkey[KEY_ITEMS].pop()
            # Monkey inspects item and performs its operation
            # print(f"Monkey inspects item with worry {item}")
            new_worry = monkey[KEY_OPERATION](item, monkey[KEY_OPERATION_ARGUMENT]) % LCM
            monkey[KEY_INSPECTION_COUNT] += 1

            # Monkey test's the worry level
            if monkey[KEY_TEST](new_worry, monkey[KEY_DIVISOR]):
                # print("Current level is divisible")
                next_monkey = monkey[KEY_TRUE_TEST]
            else:
                # print("Current level is not divisible")
                next_monkey = monkey[KEY_FALSE_TEST]

            # Monkey throws item to the next monkey
            all_monkeys[next_monkey][KEY_ITEMS].append(new_worry)
            # print(f"Item with worry level {new_worry} is thrown to monkey {next_monkey}")

    if r + 1 in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, MAX_ROUNDS]:
        print(f"==== After round {r+1} ====")
        # print_monkey_items(all_monkeys)
        print_monkey_inspections(all_monkeys)

    # print(f"---- Items after round {r+1} ----")
    # print_monkey_items(all_monkeys)

max1, max2 = 0, 0
for m in all_monkeys:
    inspection_count = m[KEY_INSPECTION_COUNT]
    if inspection_count > max1:
        max2 = max1
        max1 = inspection_count
    elif inspection_count > max2:
        max2 = inspection_count

if max2 == 0:
    max2 = all_monkeys[MAX_MONKEYS - 1][KEY_INSPECTION_COUNT]

print(f"The most inspections were {max1} and {max2}")
print(f"The level of monkey business was {max1 * max2}")
