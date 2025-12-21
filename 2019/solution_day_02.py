from argparse import ArgumentParser

from intcode import IntCode_Computer


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().split(",")))


def find_noun_verb(computer: IntCode_Computer, to_match: int = 19690720) -> tuple[int, int]:
    for noun in range(0, 100):
        for verb in range(0, 100):
            computer.reset()
            computer.overwrite_memory(1, noun)
            computer.overwrite_memory(2, verb)
            computer.run()
            if computer.get_value_at_position(0) == to_match:
                return noun, verb
    raise ValueError("No such noun and verb pair exists")


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2019 - Day 2")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    program = get_data(filename)

    computer = IntCode_Computer(program)
    computer.overwrite_memory(1, 12)
    computer.overwrite_memory(2, 2)
    computer.run()
    print(f"The answer to part 1 is {computer.get_value_at_position(0)}.")

    noun, verb = find_noun_verb(computer)
    print(f"The answer to part 2 is {100 * noun + verb}.")


if __name__ == "__main__":
    main()
