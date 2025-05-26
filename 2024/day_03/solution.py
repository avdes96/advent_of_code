import argparse
from re import findall, finditer


def get_data(filename: str) -> str:
    with open(filename) as f:
        data = f.read().strip()
    return data


def part_1(data: str) -> None:
    answer = 0
    pattern = r"mul\(\d+,\d+\)"
    for match in finditer(pattern, data):
        digit_pattern = r'\d+'
        digits = findall(digit_pattern, match.group(0))
        answer += int(digits[0]) * int(digits[1])
    print(f"The answer for part 1 is {answer}.")


def part_2(data: str) -> None:
    answer = 0
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    multiply = True
    for match in finditer(pattern, data):
        if match.group(0) == "do()":
            multiply = True
        elif match.group(0) == "don't()":
            multiply = False
        else:
            if multiply:
                digit_pattern = r'\d+'
                digits = findall(digit_pattern, match.group(0))
                answer += int(digits[0]) * int(digits[1])
    print(f"The answer for part 2 is {answer}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 3")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    part_1(data)
    part_2(data)


if __name__ == '__main__':
    main()
