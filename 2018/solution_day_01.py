from argparse import ArgumentParser


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().split("\n")))


def find_first_repeat(data: list[int]) -> int:
    seen = set()
    current = 0
    while True:
        for n in data:
            current += n
            if current in seen:
                return current
            seen.add(current)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2018 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {sum(data)}.")
    print(f"The answer to part 2 is {find_first_repeat(data)}.")


if __name__ == "__main__":
    main()
