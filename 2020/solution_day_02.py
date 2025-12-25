from argparse import ArgumentParser
from typing import Callable
import re


def get_data(filename: str) -> list[tuple[int, int, str, str]]:
    with open(filename, "r") as f:
        data = []
        for line in f:
            pattern = r"^(\d+)-(\d+) (\w): (\w+)$"
            m = re.match(pattern, line.strip())
            if m is None:
                raise ValueError(f"{line} not in expected form {pattern}")
            info = (int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))
            data.append(info)
    return data


def valid_func(lower: int, upper: int, char: str, password: str) -> bool:
    return lower <= password.count(char) <= upper


def valid_func_advanced(idx1: int, idx2: int, char: str, password: str) -> bool:
    return (password[idx1 - 1] == char) != (password[idx2 - 1] == char)


def get_solution(
    data: list[tuple[int, int, str, str]],
    valid_func: Callable[[int, int, str, str], bool],
) -> int:
    return sum(1 if valid_func(*values) else 0 for values in data)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2020 - Day 2")
    parser.add_argument(
        "input_filename", type=str, help="File containing problem input."
    )
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {get_solution(data, valid_func)}.")
    print(f"The answer to part 2 is {get_solution(data, valid_func_advanced)}.")


if __name__ == "__main__":
    main()
