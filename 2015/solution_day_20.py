import argparse
from functools import cache


def get_data(filename: str) -> int:
    with open(filename) as f:
        return int(f.read().strip())


def get_solution(min_presents: int, max_divisors: int | float, present_per_elf: int) -> int:
    house_number = 0
    while get_total_presents(house_number, max_divisors, present_per_elf) < min_presents:
        house_number += 1
    return house_number


def get_total_presents(number: int, max_divisors: int | float, present_per_elf: int) -> int:
    return sum([div for div in get_divisors(number) if number//div <= max_divisors]) * present_per_elf


@cache
def get_divisors(number: int) -> list[int]:
    i = 1
    divisors = []
    while i ** 2 <= number:
        if number % i == 0:
            divisors += [i, number // i]
        i += 1
    return divisors


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 20")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    min_presents = get_data(filename)
    answer_part_1 = get_solution(min_presents, max_divisors=float("inf"), present_per_elf=10)
    print(f"The answer to part 1 is {answer_part_1}.")
    answer_part_2 = get_solution(min_presents, max_divisors=50, present_per_elf=11)
    print(f"The answer to part 2 is {answer_part_2}.")


if __name__ == '__main__':
    main()
