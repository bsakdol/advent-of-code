#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 3, Part 2

Calculates the total sum of part numbers adjacent to a symbol in an engine schematic.
"""

NOT_SYMBOLS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
GEAR_SYMBOL = {"*"}

def is_symbol(char: str) -> bool:
    """
    Checks if a character is a symbol (excluding periods).

    Args:
        char (str): A single character.

    Returns:
        bool: False if the character is a valid symbol.
    """
    return char.strip() != "" and char in GEAR_SYMBOL

def is_digit_at(grid: list[list[str]], cell_x: int, cell_y: int) -> bool:
    """
    Checks if the character in the cell is a digit.

    Args:
        grid (list[list[str]]): The list of strings representing lines from the calibration document.
        cell_x (int): The x-coordinate (column) of the grid.
        cell_y (int): The y-coordinate (row) of the grid.

    Returns:
        bool: Returns true if the character in the cell is a digit.
    """
    return 0 <= cell_y < len(grid) and 0 <= cell_x < len(grid[0]) and grid[cell_y][cell_x].isdigit()

def extract_number(grid: list[list[str]], start_x: int, end_x: int, y: int) -> int:
    """
    Joins the individual digits into a single number.

    Args:
        grid (list[list[str]]): The list of strings representing lines from the calibration document.
        start_x (int): The x-coordinate (column) representing the beginning position of the entire number.
        end_x (int): The x-coordinate (column) representing the ending position of the entire number.
        y (int): The y-coordinate (row) of the entire number.

    Returns:
        int: The entire number.
    """
    return int("".join(grid[y][start_x:end_x]))

def find_bounds(grid: list[list[str]], x: int, y: int) -> tuple:
    """
    Determines the starting and ending position of a number in the grid.

    Args:
        grid (list[list[str]]): The list of strings representing lines from the calibration document.
        x (int): The x-coordinate (column) where the detected number is positioned.
        y (int): The y-coordinate (row) where the detected number is positioned.

    Returns:
        tuple: The starting and ending position of the number in the grid.
    """
    start_x, end_x = x, x

    while start_x > 0 and is_digit_at(grid, start_x - 1, y):
        start_x -= 1

    while end_x < len(grid[0]) and is_digit_at(grid, end_x, y):
        end_x += 1

    return start_x, end_x

def get_numbers_adjacent_to_symbols (grid: list[list[str]], x: int, y: int) -> int:
    """
    Find numbers adjacent to valid symbols in the grid.

    Args:
        grid (list[list[str]]): The list of strings representing lines from the calibration document.
        x (int): The x-coordinate (column) of the cell to check.
        y (int): The y-coordinate (row) of the cell cell to check.

    Returns:
        int: The gear ratio of the engine parts.
    """
    all_numbers = []
    digit_above = y > 0 and is_digit_at(grid, x, y-1)
    digit_below = y < len(grid)-1 and is_digit_at(grid, x, y+1)

    # Check the cells above and below the symbol
    for yy in [-1, 1]:
        if (yy == -1 and digit_above) or (yy == 1 and digit_below):
            start_x, end_x = find_bounds(grid, x, y+yy)
            all_numbers.append(extract_number(grid, start_x, end_x, y+yy))

    # Check the cells left and right of the symbol
    for xx in [-1, 1]:
        if is_digit_at(grid, x+xx, y):
            start_x, end_x = find_bounds(grid, x+xx, y)
            all_numbers.append(extract_number(grid, start_x, end_x, y))

    # Check the diagonal cells only if a number was not found above or below the symbol
    for yy, xx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if not (yy == -1 and digit_above) and not (yy == 1 and digit_below) and is_digit_at(grid, x+xx, y+yy):
            start_x, end_x = find_bounds(grid, x+xx, y+yy)
            all_numbers.append(extract_number(grid, start_x, end_x, y+yy))

    if len(all_numbers) == 2:
        gear_ratio = all_numbers[0] * all_numbers[1]
        return gear_ratio
    else:
        return 0


def sum_of_part_numbers(grid: list[list[str]]) -> int:
    """
    Sum the part numbers adjacent to a symbol in the engine schematic.

    Args:
        data (list[str]): The list of strings representing lines from the calibration document.

    Returns:
        int: The final sum of calibration values.
    """
    all_numbers = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if is_symbol(cell):
                all_numbers.append(get_numbers_adjacent_to_symbols(grid, x, y))

    return sum(all_numbers)

def main(input_file: str):
    """
    Main function to execute the script logic.

    Reads each line from the specified input file and processes them to calculate the total sum.

    Args:
        input_file (str): The path to the puzzle input file.
    """
    try:
        with open(input_file, encoding="utf-8") as file:
            data = [list(line.strip()) for line in file]
        total_sum = sum_of_part_numbers(data)

        print(f"Total Sum of Part Numbers: {total_sum}")

    except FileNotFoundError:
        print(f"Error: '{input_file}' file not found.")

if __name__ == '__main__':
    main("puzzle_input.txt")
