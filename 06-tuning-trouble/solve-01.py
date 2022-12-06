#!/usr/bin/env python3.8

in_file_name = "test-input.txt"
in_file_name = "puzzle-input.txt"

with open(in_file_name) as signal_file:
    signal = signal_file.readline()

    for s in range(len(signal) - 4):
        print(f"{signal[s:s+4]}")
        marker = signal[s:s+4]
        if marker[0] not in marker[1:] and marker[1] not in marker[2:] and marker[2] != marker[3]:
            print(f"Marker found after {s + 4} characters processed")
            break

