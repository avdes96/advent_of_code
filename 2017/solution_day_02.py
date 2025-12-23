from argparse import ArgumentParser
from typing import Callable


def get_data(filename: str) -> list[list[int]]:
    with open(filename, "r") as f:
        return [list(map(int, line.split())) for line in f.read().split("\n")]


def get_diff_between_max_and_min(line: list[int]) -> int:
    return max(line) - min(line)


def get_div_result(line: list[int]) -> int:
    for i in range(1, len(line)):
        for j in range(i):
            A, B = line[i], line[j]
            if A % B == 0:
                return A // B
            if B % A == 0:
                return B // A
    raise ValueError("No two numbers where one divides the other without remainder exists.")


def get_solution(data: list[list[int]], request_func: Callable[[list[int]], int]) -> int:
    return sum(request_func(line) for line in data)


if __name__ == "__main__":
    parser = ArgumentParser(description="Advent of Code 2017 - Day 2")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {get_solution(data, get_diff_between_max_and_min)}.")
    print(f"The answer to part 2 is {get_solution(data, get_div_result)}.")
