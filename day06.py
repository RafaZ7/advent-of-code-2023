# https://adventofcode.com/2023/day/6
import numpy as np


def parse_string(input_string):
    lines = input_string.strip().split("\n")
    time_values = list(map(int, lines[0].split()[1:]))
    distance_values = list(map(int, lines[1].split()[1:]))
    result = list(zip(time_values, distance_values))
    return result


def concatenate_tuples(tuple_list):
    concatenated_values = tuple(
        map(lambda x: int("".join(map(str, x))), zip(*tuple_list))
    )
    return concatenated_values


def find_number_of_winning_strategies(time, distance):
    """
    We can find the number of winning strategies by solving the following equation:
    (time - t) * t = distance

    Using the quadratic formula, we get:
    t = (time +- sqrt(time^2 - 4 * distance)) / 2

    So we just need to find how many integers are in the interval defined by the above formula.
    """
    lower_bound = (1 / 2) * (time - np.sqrt(time**2 - 4 * distance))
    upper_bound = (1 / 2) * (time + np.sqrt(time**2 - 4 * distance))

    lower_bound = np.floor(lower_bound)
    upper_bound = np.ceil(upper_bound)

    return int(upper_bound - lower_bound - 1)


if __name__ == "__main__":
    with open("data/day06.txt") as f:
        input_string = f.read()

    list_of_tuples = parse_string(input_string)

    # Part 1
    result_1 = np.prod([find_number_of_winning_strategies(*t) for t in list_of_tuples])
    print("Part 1: ", result_1)

    # Part 2
    one_tuple = concatenate_tuples(list_of_tuples)
    result_2 = find_number_of_winning_strategies(*one_tuple)
    print("Part 2: ", result_2)
