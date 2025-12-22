from argparse import ArgumentParser


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().split("\n")))


def total_fuel(mass: int) -> int:
    total = 0
    while mass > 8:
        mass = mass // 3 - 2
        total += mass
    return total


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2019 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {sum((mass // 3) - 2 for mass in data)}.")
    print(f"The answer to part 2 is {sum(total_fuel(mass) for mass in data)}.")


if __name__ == '__main__':
    main()
