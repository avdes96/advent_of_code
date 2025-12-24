from argparse import ArgumentParser
from math import prod


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().split("\n")))


def find_two_numbers_sum_to_target(data: list[int], target: int = 2020) -> tuple[int, int]:
    seen = set()
    for n in data:
        need = target - n
        if need in seen:
            return need, n
        seen.add(n)
    raise ValueError(f"No two numbers sum to {target}.")


def find_three_numbers_sum_to_target(data: list[int], target: int = 2020) -> tuple[int, int, int]:
    sorted_data = sorted(data)
    for t in range(len(sorted_data)):
        l, r = t + 1, len(sorted_data) - 1
        while l < r:
            total = sorted_data[t] + sorted_data[l] + sorted_data[r]
            if total == target:
                return sorted_data[t], sorted_data[l], sorted_data[r]
            elif total > target:
                r -= 1
            else:
                l += 1
    raise ValueError(f"No three numbers sum to {target}.")


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2020 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {prod(find_two_numbers_sum_to_target(data))}.")
    print(f"The answer to part 2 is {prod(find_three_numbers_sum_to_target(data))}.")


if __name__ == "__main__":
    main()
