#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as rucksack_file:
    total_badge_priorities = 0
    current_elf_rucksacks = []

    while True:
        for _ in range(3):
            current_elf_rucksacks.append(rucksack_file.readline())
            
        if current_elf_rucksacks[0] == "":
            break

        for item in current_elf_rucksacks[0]:
            if item in current_elf_rucksacks[1] and item in current_elf_rucksacks[2]:
                # item is currently the elf badge

                if item.isupper():
                    # Different priority
                    priority = ord(item) - 38
                else:
                    priority = ord(item) - 96

                print(f"Items: {item} -- {priority}")
                total_badge_priorities += priority

                break

        current_elf_rucksacks = []

print(f"Total priority of items: {total_badge_priorities}")
