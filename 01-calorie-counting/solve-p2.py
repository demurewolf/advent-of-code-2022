#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as elf_calorie_file:
    elf_calories = [0]
    curr_elf = 0
    
    cal = elf_calorie_file.readline()
    
    while (cal != ""):
        #print(cal)

        if cal == "\n":
            elf_calories.append(0)
            curr_elf += 1
            cal = elf_calorie_file.readline()
            continue

        elf_calories[curr_elf] += int(cal)
        cal = elf_calorie_file.readline()

elf_calories.sort(reverse=True)
top_three = sum(elf_calories[0:3])

        
print(f"Elf calorie list is {elf_calories}")
print(f"Top three total calories are {top_three}")