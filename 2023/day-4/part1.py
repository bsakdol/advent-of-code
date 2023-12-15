#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 4, Part 1

Calculates the total number of points the scratchcards are worth.
"""

def calculate_winning_points(matching_numbers: list[str]) -> int:
    """
    Calculate the total points for a given list of matching numbers.

    Args:
        matching_numbers (list[str]): A list of numbers that have matched.

    Returns:
        int: The calculated points based on the number of matches.
    """
    return 2**(len(matching_numbers)-1)

def match_numbers(winning_numbers: list, card_numbers: list) -> int:
    """
    Match numbers between the winning numbers and card numbers, calculate points
     for matches.

    Args:
        winning_numbers (list): List of winning numbers.
        card_numbers (list): List of numbers on a card.

    Returns:
        int: The points earned based on the matched numbers.
    """
    matched_numbers = []

    winners = winning_numbers.split(" ")
    possibles = card_numbers.split(" ")

    for num in possibles:
        if num in winners and num is not "":
            matched_numbers.append(num)

    if len(matched_numbers) > 0:
        return calculate_winning_points(matched_numbers)
    else:
        return 0

def calculate_point_value(cards: list[str]):
    """
    Calculate the total point value for a list of cards.

    Args:
        cards (list[str]): A list of card numbers as strings.

    Returns:
        int: The total point value for the cards.
    """
    total_points = []

    _, numbers = cards.split(":")
    winning_numbers, card_numbers = numbers.split("|")
    total_points.append(match_numbers(winning_numbers, card_numbers))

    return sum(total_points)

def sum_of_scratchcards(cards: list[str]) -> int:
    """
    Calculate the sum of points for a list of scratchcards.

    Args:
        cards (list[str]): A list of scratchcard numbers.

    Returns:
        int: The total sum of points from all scratchcards.
    """
    return sum(calculate_point_value(card.strip()) for card in cards)

def main(input_file: str):
    """
    Main function to execute the script logic.

    Reads each line from the specified input file and processes them to calculate the total sum.

    Args:
        input_file (str): The path to the puzzle input file.
    """
    try:
        with open(input_file, encoding="utf-8") as file:
            data = file.readlines()
        total_sum = sum_of_scratchcards(data)

        print(f"Total Number of Points: {total_sum}")

    except FileNotFoundError:
        print(f"Error: '{input_file}' file not found.")

if __name__ == '__main__':
    main("puzzle_input")
