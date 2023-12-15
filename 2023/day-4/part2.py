#!/usr/bin/env python3
"""
Advent of Code 2023 - Day 4, Part 2

Calculates the total number of scratchcards.
"""

def parse_card(card_line: str) -> tuple:
    """
    Parse a single card line into two sets of numbers.

    Args:
        card_line (str): A string representing a single line from the card data.

    Returns:
        tuple: A tuple containing two sets - winning_numbers and possible_numbers.
    """
    _, card = card_line.strip().split(":")
    card = card.split("|")

    winning_numbers = set(int(x) for x in card[0].split())
    possible_numbers = set(int(x) for x in card[1].split())

    return winning_numbers, possible_numbers

def calculate_wins(winning_numbers: set, possible_numbers: set) -> set:
    """
    Calculate the intersection (wins) between two sets of numbers.

    Args:
        winning_numbers (set): A set of winning numbers.
        possible_numbers (set): A set of numbers that a player has.

    Returns:
        set: A set containing the numbers that are present in both winning_numbers and possible_numbers.
    """
    return set(x for x in possible_numbers if x in winning_numbers)

def calculate_number_of_cards(cards: list[str], index: int, number_of_cards: list[int]) -> int:
    """
    Calculate and update the number of cards based on the winning numbers for the current card and update subsequent cards' numbers.

    Args:
        cards (list[str]): A list of all card lines.
        index (int): The index of the current card in the list.
        number_of_cards (list[int]): A list of numbers representing the count for each card.

    Returns:
        int: The number of cards calculated for the current index.
    """
    winning_numbers, possible_numbers = parse_card(cards[index])
    wins = calculate_wins(winning_numbers, possible_numbers)
    current_number_of_cards = number_of_cards[index]

    for x in range(index + 1, min(index + len(wins) + 1, len(cards))):
        number_of_cards[x] += current_number_of_cards

    return current_number_of_cards

def sum_of_scratchcards(cards: list[str]) -> int:
    """
    Calculate the sum of points for a list of scratchcards.

    Args:
        cards (list[str]): A list of scratchcard numbers.

    Returns:
        int: The total sum of cards after winning.
    """
    number_of_cards = [1 for _ in cards]

    return sum(calculate_number_of_cards(cards, i, number_of_cards) for i in range(len(cards)))

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

        print(f"Total Number of Cards: {total_sum}")

    except FileNotFoundError:
        print(f"Error: '{input_file}' file not found.")

if __name__ == '__main__':
    main("puzzle_input")
