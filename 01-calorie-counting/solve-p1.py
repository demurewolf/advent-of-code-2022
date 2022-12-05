#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as elf_calorie_file:
    elf = 0
    calories = 0
    most_calories = calories
    
    cal = elf_calorie_file.readline()
    
    while (cal != ""):
        
        print(cal)

        if cal == "\n":
            elf +=1
            calories = 0
            cal = elf_calorie_file.readline()
            continue

        calories += int(cal)
        if calories > most_calories:
            most_calories = calories

        cal = elf_calorie_file.readline()

print(f"Elf with most calories: {elf}\nCarrying {most_calories} calories!")