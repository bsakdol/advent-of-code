#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 1
===========================
Creates a sum of all numbers in the calibration document, where the calibration
values are the first and last digit of each line.
"""

import re


def sum_calibration_numbers(numbers):
    """
    Calculate the sum of calibration values.

    Args:
        numbers (list): List of strings representing lines from the calibration document.

    Returns:
        int: The final sum of calibration values.
    """
    total_sum = 0

    for line in numbers:
        line_numbers = re.findall('\\d', line)

        if len(line_numbers) == 1:
            total_sum += int(line_numbers[0] * 2)
        else:
            total_sum += int(line_numbers[0] + line_numbers[-1])

    return total_sum


def main():
    """
    Main function to execute the script logic.

    Reads each line from 'puzzle_input.txt' and processes them to calculate the total sum of calibration values.
    """
    try:
        with open("puzzle_input.txt", encoding="utf-8") as file:
            data = file.readlines()
        total_sum = sum_calibration_numbers(data)
        print(total_sum)
    except FileNotFoundError:
        print("Error: 'puzzle_input.txt' file not found.")


if __name__ == '__main__':
    main()
