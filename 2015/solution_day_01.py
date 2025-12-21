import argparse


def get_data(filename: str) -> str:
    with open(filename) as f:
        return f.readline().strip()


def update_level(level: int, char: str) -> int:
    match char:
        case '(': level += 1
        case ')': level -= 1
        case '_': raise ValueError(f"{char} is not expected in input.")
    return level


def find_pos_of_first_occurance(sequence: str, target: int) -> int:
    level = 0
    for pos, char in enumerate(sequence):
        level = update_level(level, char)
        if level == target:
            return pos + 1
    raise ValueError(f"Target of {target} is never reached.")


def part_1(sequence: str) -> None:
    level = 0
    for char in sequence:
        level = update_level(level, char)
    print(f"The answer to part 1 is {level}.")


def part_2(sequence: str, target: int = -1) -> None:
    answer = find_pos_of_first_occurance(sequence, target)
    print(f"The answer to part 2 is {answer}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    sequence = get_data(filename)
    part_1(sequence)
    part_2(sequence)


if __name__ == "__main__":
    main()
