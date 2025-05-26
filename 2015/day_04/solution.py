import argparse
from hashlib import md5


def get_data(filename: str) -> str:
    with open(filename) as f:
        return f.read().strip()


def get_solution(prefix: str, n_zeros: int) -> int:
    found = False
    postfix = 0
    while not found:
        attempt = prefix + str(postfix)
        digest = md5(attempt.encode()).hexdigest()
        if digest[:n_zeros] == '0' * n_zeros:
            found = True
        else:
            postfix += 1
    return postfix


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 4")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    prefix = get_data(filename)
    print(f"The answer to part 1 is {get_solution(prefix, n_zeros=5)}.")
    print(f"The answer to part 2 is {get_solution(prefix, n_zeros=6)}.")


if __name__ == '__main__':
    main()
