import argparse
from dataclasses import dataclass
from re import match


@dataclass
class Instruction:
    direction: str
    amt: int


def get_data(filename: str) -> list[Instruction]:
    pattern = r"(L|R)(\d+)"
    data = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            m = match(pattern, line)
            if m is None:
                raise ValueError(f"Line not in expected format: {pattern}")
            direction, amt = m.groups()
            data.append(Instruction(direction=direction, amt=int(amt)))
    return data


def part_1_method(instructions: list[Instruction], dial: int = 50, max_num: int = 99) -> int:
    answer = 0
    for instruction in instructions:
        multiplier = 1 if instruction.direction == 'R' else -1
        dial = (dial + (multiplier * instruction.amt)) % (max_num + 1)
        if dial == 0:
            answer += 1
    return answer


def part_2_method(instructions: list[Instruction], dial: int = 50, max_num: int = 99) -> int:
    answer = 0
    for instruction in instructions:
        before = dial
        dial += instruction.amt * (1 if instruction.direction == 'R' else -1)
        answer += abs(dial) // (max_num + 1) + (1 if (before != 0 and dial <= 0) else 0)
        dial = dial % (max_num + 1)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2025 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {part_1_method(data)}.")
    print(f"The answer to part 2 is {part_2_method(data)}.")


if __name__ == "__main__":
    main()
