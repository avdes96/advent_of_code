from argparse import ArgumentParser
from functools import cache


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split("\n")


def find_largest_number(line: str, digits: int) -> int:
    @cache
    def max_from_idx(rev: str, idx: int, taken: int) -> int:
        if taken == digits or idx == len(line):
            return 0
        ignore = max_from_idx(rev, idx + 1, taken)
        take = int(rev[idx]) * (10 ** taken) + max_from_idx(rev, idx + 1, taken + 1)
        return max(ignore, take)
    return max_from_idx(line[::-1], 0, 0)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 3")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    answer_1 = 0
    answer_2 = 0
    for line in data:
        answer_1 += find_largest_number(line, 2)
        answer_2 += find_largest_number(line, 12)
    print(f"The answer to part 1 is {answer_1}.")
    print(f"The answer to part 2 is {answer_2}.")


if __name__ == "__main__":
    main()
