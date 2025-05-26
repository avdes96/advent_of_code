import argparse


def get_data(filename: str) -> tuple[set[str], list[str]]:
    with open(filename) as f:
        data = f.readlines()
    towels = set(data[0].strip().split(", "))
    requests = [line.strip() for line in data[2:]]
    return towels, requests


def is_possible(request: str, possible: dict[str, bool]) -> bool:
    if request in possible:
        return possible[request]

    for i in range(len(request)):
        if is_possible(request[:i], possible) and is_possible(request[i:], possible):
            possible[request] = True
            return True
    possible[request] = False
    return False


def part_1(towels: set[str], requests: list[str], print_answer: bool = True) -> int:
    possible = {towel: True for towel in towels}
    answer = 0
    for request in requests:
        if is_possible(request, possible):
            answer += 1
    if print_answer:
        print(f"The answer to part 1 is {answer}.")
    return answer


def number_combos(request: str, towels: set[str], number_combos_lookup: dict[str, int]) -> int:
    if request in number_combos_lookup:
        return number_combos_lookup[request]

    n = 1 if request in towels else 0
    if len(request) == 1:
        return n

    for i in range(1, len(request)):
        left = request[:i]
        right = request[i:]
        if left in towels:
            n += number_combos(right, towels, number_combos_lookup)
    number_combos_lookup[request] = n
    return n


def part_2(towels: set[str], requests: list[str]) -> None:
    answer = 0
    n_possible = 0
    number_combos_lookup = {}
    for request in requests:
        n = number_combos(request, towels, number_combos_lookup)
        answer += n
        if n > 0:
            n_possible += 1
    print(f"The answer to part 2 is {answer}.")
    # We can confirm answer to part 1 using part 2 method
    assert n_possible == part_1(
        towels, requests, print_answer=False), "Answers using part 1 and part 2 methods do not match."


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 19")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    towels, requests = get_data(filename)
    part_1(towels, requests)
    part_2(towels, requests)


if __name__ == '__main__':
    main()
