# Advent of Code 2023 Day 2: https://adventofcode.com/2023/day/2
from dataclasses import dataclass
from typing import List, Self


@dataclass(frozen=False)
class CubeSet:
    blue: int = 0
    green: int = 0
    red: int = 0

    @classmethod
    def from_string(cls, string: str) -> Self:
        number_color_list = string.split(",")
        number_color_dict = {}
        for number_color in number_color_list:
            number, color = number_color.strip().split(" ")
            number_color_dict[color] = int(number)
        return cls(**number_color_dict)

    def is_valid(self, other: 'CubeSet') -> bool:
        return self.blue <= other.blue and self.green <= other.green and self.red <= other.red

    @property
    def power(self):
        return self.red * self.green * self.blue


@dataclass(frozen=False)
class Game:
    n: int
    cube_set: List[CubeSet]

    def is_valid(self, cube_set: CubeSet) -> bool:
        return all([game_cube_set.is_valid(cube_set) for game_cube_set in self.cube_set])

    @classmethod
    def from_string(cls, string: str) -> Self:
        n, cube_set_string = string.split(":")
        n = int(n.strip().split(" ")[1])
        cube_set = [CubeSet.from_string(cube_set) for cube_set in cube_set_string.split(";")]
        return cls(n, cube_set)

    def minimum_set(self) -> CubeSet:
        return CubeSet(
            blue=max([cube_set.blue for cube_set in self.cube_set]),
            green=max([cube_set.green for cube_set in self.cube_set]),
            red=max([cube_set.red for cube_set in self.cube_set]),
        )


def game_solver_1(games_string: str, max_set: CubeSet) -> int:
    games = [Game.from_string(game_string) for game_string in games_string.strip().split("\n")]
    return sum([game.n for game in games if game.is_valid(max_set)])


def game_solver_2(games_string: str) -> int:
    games = [Game.from_string(game_string) for game_string in games_string.strip().split("\n")]
    return sum([game.minimum_set().power for game in games])


if __name__ == "__main__":
    with open("data/day2.txt", "r") as f:
        games_string = f.read()

    final_result1 = game_solver_1(games_string, CubeSet(red=12, green=13, blue=14))
    print(f"Final result 1: {final_result1}")

    final_result2 = game_solver_2(games_string)
    print(f"Final result 2: {final_result2}")
