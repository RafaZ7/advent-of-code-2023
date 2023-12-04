import re
from dataclasses import dataclass
from typing import Self

number_regex = re.compile(r"\d+")


@dataclass
class Card:
    winners: list[int]
    my_numbers: list[int]

    @classmethod
    def from_string(cls, string: str) -> Self:
        winners, my_numbers = string.split(":")[1].split("|")
        winners = [int(number) for number in number_regex.findall(winners)]
        my_numbers = [int(number) for number in number_regex.findall(my_numbers)]
        return cls(winners, my_numbers)

    @property
    def matches(self) -> int:
        return len(set(self.winners).intersection(set(self.my_numbers)))

    @property
    def points(self) -> int:
        return int(2 ** (self.matches - 1))


if __name__ == "__main__":
    with open("data/day04.txt") as f:
        raw_input = f.read().strip().split("\n")

    # First problem
    card_set = [Card.from_string(line) for line in raw_input]
    result_1 = sum(card.points for card in card_set)
    print("Result 1: ", result_1)

    # Second problem
    counter_deck = {i: 1 for i in range(1, len(raw_input) + 1)}

    for card_number, card in enumerate(card_set, 1):
        matches = card.matches
        number_of_cards = counter_deck[card_number]
        for next_card_number in range(card_number + 1, card_number + matches + 1):
            if next_card_number > len(raw_input):
                break
            counter_deck[next_card_number] += number_of_cards

    result_2 = sum(counter for counter in counter_deck.values())
    print("Result 2: ", result_2)
