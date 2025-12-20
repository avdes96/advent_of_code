from argparse import ArgumentParser


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split("\n\n")


def parse_data(data: list[str]) -> list[int]:
    return [sum(map(int, items_str.split("\n"))) for items_str in data]


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2022 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    collated_data = parse_data(data)
    sorted_data = sorted(collated_data, reverse=True)
    print(f"The answer to part 1 is {sorted_data[0]}.")
    print(f"The answer to part 2 is {sum(sorted_data[:3])}.")


if __name__ == "__main__":
    main()
