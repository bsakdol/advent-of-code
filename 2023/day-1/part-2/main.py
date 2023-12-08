#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 1, Part 2
===========================
Creates a sum of all numbers in the calibration document, where the calibration
values are the first and last number (digit or text) of each line.
"""

import regex

# Constants
TEXT_NUMBER_MAPPING = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

NUMBER_REGEX_PATTERN = '\\d|one|two|three|four|five|six|seven|eight|nine'


def convert_text_to_number(text: str) -> str:
    """
    Converts a spelled out number to the numeric form.

    Args:
        text (str): The textual number.

    Returns:
        str: The numeric number.
    """
    return TEXT_NUMBER_MAPPING.get(text, text)


def concat_line_numbers(line: str) -> int:
    """
    Concatinates the number(s) in the line to form a single number.

    Args:
        line (str): The individual line from the calibration document.

    Returns:
        int: The combined digits that form a single number.
    """
    line_numbers = regex.findall(NUMBER_REGEX_PATTERN, line, overlapped=True)

    first_number = convert_text_to_number(line_numbers[0])

    if len(line_numbers) == 1:
        last_number = first_number
    else:
        last_number = convert_text_to_number(line_numbers[-1])

    return int(first_number + last_number)


def sum_calibration_numbers(data: list[str]) -> int:
    """
    Calculate the sum of calibration values.

    Args:
        data (list[str]): The list of strings representing lines from the calibration document.

    Returns:
        int: The final sum of calibration values.
    """
    return sum(concat_line_numbers(line) for line in data)


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
