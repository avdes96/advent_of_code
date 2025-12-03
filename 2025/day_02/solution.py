import argparse
from functools import cache


def get_data(filename: str) -> list[tuple[int, int]]:
    out = []
    with open(filename) as f:
        data = f.read().split(",")
    for rng in data:
        start, end = map(int, rng.split("-"))
        out.append((start, end))
    return out


def is_double_repeat(n: int) -> bool:
    n_str = str(n)
    return n_str[:len(n_str)//2] == n_str[len(n_str)//2:]


@cache
def divisors(n: int) -> list[int]:
    out = []
    for i in range(1, (n//2)+1):
        div, r = divmod(n, i)
        if r == 0:
            out.append(div)
    return out


def has_repeat(n: int) -> bool:
    str_n = str(n)
    for i in divisors(len(str_n)):
        if str_n[:i] * (len(str_n) // i) == str_n:
            return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2025 - Day 2")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    answer_1 = 0
    answer_2 = 0
    for start, end in data:
        for n in range(start, end + 1):
            if is_double_repeat(n):
                answer_1 += n
            if has_repeat(n):
                answer_2 += n
    print(f"The answer to part 1 is {answer_1}.")
    print(f"The answer to part 2 is {answer_2}.")


if __name__ == "__main__":
    main()
