from argparse import ArgumentParser


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().split("\n")))


def get_solution(instructions: list[int], use_advance_rule: bool = False) -> int:
    idx = 0
    steps = 0
    while 0 <= idx < len(instructions):
        offset = instructions[idx]
        if use_advance_rule:
            if offset >= 3:
                instructions[idx] -= 1
            else:
                instructions[idx] += 1
        else:
            instructions[idx] += 1
        idx += offset
        steps += 1
    return steps


if __name__ == "__main__":
    parser = ArgumentParser(description="Advent of Code 2017 - Day 5")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data_part_1 = get_data(filename)
    print(f"The answer to part 1 is {get_solution(data_part_1)}.")
    data_part_2 = get_data(filename)
    print(f"The answer to part 2 is {get_solution(data_part_2, use_advance_rule=True)}.")
