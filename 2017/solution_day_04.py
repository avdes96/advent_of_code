from argparse import ArgumentParser


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def passphrase_valid(passphrase: str, allow_anagrams: bool) -> bool:
    words = passphrase.split()
    if not allow_anagrams:
        words = list("".join(sorted(word)) for word in words)
    return len(words) == len(set(words))


def get_solution(data: list[str], allow_anagrams: bool = True) -> int:
    return sum(1 if passphrase_valid(passphrase, allow_anagrams) else 0 for passphrase in data)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2017 - Day 4")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {get_solution(data)}.")
    print(f"The answer to part 2 is {get_solution(data, allow_anagrams=False)}.")


if __name__ == "__main__":
    main()
