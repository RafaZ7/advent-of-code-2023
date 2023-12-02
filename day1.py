import re

replace_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

regex_pattern1 = r"\d"
regex_pattern2 = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"


def code_extractor(code: str, regex_pattern: str) -> int:
    # Select with regex only the digits, this should return a list of only one digits
    digits = re.findall(regex_pattern, code)
    return int(f"{replace_dict[digits[0]]}{replace_dict[digits[-1]]}")


if __name__ == "__main__":

    with open("data/day1.txt", "r") as f:
        calibration_codes = f.read()

    # Part 1
    result1 = sum(code_extractor(code, regex_pattern1) for code in calibration_codes.strip().split("\n"))

    print(f"Result 1: {result1}")

    # Part 2
    result2 = sum(code_extractor(code, regex_pattern2) for code in calibration_codes.strip().split("\n"))
    print(f"Result 2: {result2}")
