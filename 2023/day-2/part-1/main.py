#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 2
===========================
Identifies the games that would have been possible if the bag of cubes only contained 12 red cubes, 13 green cubes, and
14 blue cubes. Then, sums the ID number of the possible game numbers.
"""

import re

# Constants
CUBE_QUANTITIES = {"red": 12, "green": 13, "blue": 14}
GAME_ID_REGEX = re.compile(r"^Game\s(\d+):")


def get_game_id(game_info: str) -> int:
    """
    Retrieves the game number from the game information.

    Args:
        game_info (str): The information about the game.

    Returns:
        int: The number (ID) of the game.
    """
    match = GAME_ID_REGEX.search(game_info)

    return int(match.group(1)) if match else 0


def is_game_possible(game_info: str) -> bool:
    """
    Determines if the game is possible based on the cube quantities.

    Args:
        game_info (str): The information about the game.

    Returns:
        bool: True if the game is possible, False otherwise.
    """
    _, cube_info = game_info.split(":") # I had to look this up (1)
    for handfuls in cube_info.split(";"):
        for cube in handfuls.split(","):
            quantity, color = cube.split()
            if int(quantity) > CUBE_QUANTITIES.get(color, 0):
                return False
    return True


def sum_possible_game_ids(games: list[str]) -> int:
    """
    Calculates the sum of the IDs of possible games.

    Args:
        games (list[str]): A list of game information strings.

    Returns:
        int: The sum of the valid game ID numbers.
    """
    return sum(get_game_id(game) for game in games if is_game_possible(game))


def main():
    """
    Main function to execute the script logic.

    Reads each line from 'puzzle_input.txt' and processes them to calculate the sum of possible game IDs.
    """
    try:
        with open("puzzle_input.txt", encoding="utf-8") as file:
            data = file.readlines()
        total_sum = sum_possible_game_ids(data)

        print(f"Total Sum of Game ID Numbers: {total_sum}")

    except FileNotFoundError:
        print("Error: 'puzzle_input.txt' file not found.")


if __name__ == '__main__':
    main()

# 1: I couldn't figure out how to get rid of the linter error for an unused variable `game_id`. The `_,` is basically
#    saying we don't care about the first variable and it can be thrown away.
