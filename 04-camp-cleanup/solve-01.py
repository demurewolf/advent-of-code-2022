#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as camp_section_file:
    double_booked_count = 0

    for assignment in camp_section_file:
        section1, section2 = assignment.split(",")
        elf1_lower_section, elf1_upper_section = section1.split("-")
        elf2_lower_section, elf2_upper_section = section2.split("-")

        elf1_lower_section, elf1_upper_section = int(elf1_lower_section), int(elf1_upper_section)
        elf2_lower_section, elf2_upper_section = int(elf2_lower_section), int(elf2_upper_section)
        
        #print(f"Testing: {elf1_lower_section}, {elf1_upper_section} -- {elf2_lower_section}, {elf2_upper_section}")

        if (elf1_lower_section >= elf2_lower_section and elf1_upper_section <= elf2_upper_section) or (elf2_lower_section >= elf1_lower_section and elf2_upper_section <= elf1_upper_section):
            #print("Found a double booking!")
            double_booked_count += 1

    print(f"There are a total of {double_booked_count} assignment pairs that fully contain the other")