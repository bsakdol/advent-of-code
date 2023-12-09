#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 2, Part 2

Calculates the total sum of products of the minimum number of each color cube required for a set of games.
"""

import math

def get_minimum_cubes(game_info: str) -> int:
    """Calculate the product of the minimum number of cubes needed for a game.

    Args:
        game_info (str): A string containing the number of cubes and their colors.

    Returns:
        int: The product of the minimum number of each color cube.
    """
    cubes_needed = {"red": 0, "green": 0, "blue": 0}

    _, handfuls = game_info.split(":")
    for cubes in handfuls.split(";"):
        for cube in cubes.split(","):
            quantity, color = cube.split()
            cubes_needed[color] = max(cubes_needed[color], int(quantity))

    return math.prod(cubes_needed.values())

def sum_minimum_cubes(games: list[str]) -> int:
    """Sum the products of cubes for all games.

    Args:
        games (list[str]): A list of game information strings.

    Returns:
        int: The sum of the products of cubes for all games.
    """
    return sum(get_minimum_cubes(game) for game in games)

def main(input_file: str):
    """Main function to execute the script logic.

    Reads each line from the specified input file and processes them to calculate the total sum.

    Args:
        input_file (str): The path to the puzzle input file.
    """
    try:
        with open(input_file, encoding="utf-8") as file:
            data = file.readlines()
        total_sum = sum_minimum_cubes(data)

        print(f"Total Sum of Powers: {total_sum}")

    except FileNotFoundError:
        print(f"Error: '{input_file}' file not found.")

if __name__ == '__main__':
    main("puzzle_input.txt")
