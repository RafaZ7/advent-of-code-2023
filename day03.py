import re

from dataclasses import dataclass
import numpy as np

REGEX_SPECIAL_CHARACTER = r"[^\d.]"
REGEX_DIGITS = r"\d+"


@dataclass
class SpecialCharacter:
    char: str
    row: int
    position: int


@dataclass
class Number:
    number: int
    row: int
    init: int
    end: int

    def is_adjacent_to_character(self, special_character: SpecialCharacter) -> bool:
        return (
            abs(self.init - special_character.position) <= 1
            or abs(self.end - special_character.position) <= 1
            or (self.init <= special_character.position <= self.end)
        )


if __name__ == "__main__":

    with open("data/day3.txt", "r") as f:
        raw_input = f.read()

    special_characters = []
    numbers = []

    splitted_input = raw_input.strip().split("\n")
    for i, row in enumerate(splitted_input):
        numbers_row = [
            Number(int(m.group()), i, m.start(), m.end() - 1)
            for m in re.finditer(REGEX_DIGITS, row)
        ]
        special_characters_row = [
            SpecialCharacter(m.group(), i, m.start())
            for m in re.finditer(REGEX_SPECIAL_CHARACTER, row)
        ]

        numbers.append(numbers_row)
        special_characters.append(special_characters_row)

    # First part
    final_list_of_numbers = []
    for row, special_characters_row in enumerate(special_characters):
        for special_character in special_characters_row:
            for row_number in [row - 1, row, row + 1]:
                if row_number < 0 or row_number >= len(numbers):
                    continue
                for number in numbers[row_number]:
                    if (
                        number.is_adjacent_to_character(special_character)
                        and number not in final_list_of_numbers
                    ):
                        final_list_of_numbers.append(number)

    first_part_result = sum(number.number for number in final_list_of_numbers)
    print(f"Part 1: {first_part_result}")

    # Second part
    gear_list = []
    for row, special_characters_row in enumerate(special_characters):
        for special_character in special_characters_row:
            if special_character.char != "*":
                continue
            this_character_gear = []

            for row_number in [row - 1, row, row + 1]:
                if row_number < 0 or row_number >= len(numbers):
                    continue
                for number in numbers[row_number]:
                    if number.is_adjacent_to_character(special_character):
                        this_character_gear.append(number)
            gear_list.append(this_character_gear)

    part_2_result = sum(
        [np.prod([g.number for g in gear]) for gear in gear_list if len(gear) == 2]
    )
    print(f"Part 2: {part_2_result}")
