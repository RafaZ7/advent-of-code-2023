import itertools
import math
import re
from functools import reduce
from typing import Callable


def parse(raw_input):
    lines = raw_input.strip().splitlines()

    network = {}
    instructions = lines[0]

    for line in lines[2:]:
        lhs, rhs = line.split("=")
        lhs = lhs.strip()
        rhs = re.findall(r"\b\w+\b", rhs)
        network[lhs] = rhs

    return instructions, network


def solver(
    instructions: str, network: dict, initial_value: str, checker: Callable
) -> int:
    value = initial_value
    for steps, instruction in enumerate(itertools.cycle(instructions), 1):
        if instruction == "L":
            value = network[value][0]
        elif instruction == "R":
            value = network[value][1]

        if checker(value):
            return steps


def compute_lcm(numbers):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to compute LCM.")

    return reduce(lcm, numbers)


if __name__ == "__main__":
    with open("data/day08.txt") as f:
        raw_input = f.read()

    instructions, network = parse(raw_input)

    # First part
    first_part_solution = solver(instructions, network, "AAA", lambda x: x == "ZZZ")
    print("Part 1 solution: ", first_part_solution)

    # Second part
    a_nodes = [key for key in network.keys() if key.endswith("A")]
    steps_list = [
        solver(instructions, network, node, lambda x: x.endswith("Z"))
        for node in a_nodes
    ]
    print("Part 2 solution: ", compute_lcm(steps_list))
