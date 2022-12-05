#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as rucksack_file:
    total_priorities = 0

    for rucksack in rucksack_file:
        compartment1 = rucksack[0:len(rucksack)//2] 
        compartment2 = rucksack[len(rucksack)//2:len(rucksack)]

        #print(f"Compartments: {compartment1}, {compartment2}")
        for item1 in compartment1:
            if item1 in compartment2:
                # Found the item to prioritize
                misplaced = item1
                break

        if misplaced.isupper():
            # Different priority
            priority = ord(misplaced) - 38
        else:
            priority = ord(misplaced) - 96

        print(f"Items: {misplaced} -- {priority}")
        total_priorities += priority

print(f"Total priority of items: {total_priorities}")
