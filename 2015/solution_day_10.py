import argparse


def get_data(filename: str) -> str:
    with open(filename) as f:
        return f.read().strip()


def transform_string(string: str) -> str:
    idx = 1
    digit, n = string[0], 1
    output = ""
    while idx < len(string):
        if string[idx] != digit:
            output += str(n) + str(digit)
            digit, n = string[idx], 1
        else:
            n += 1
        idx += 1
    output += str(n) + str(digit)
    return output


def get_string_after_n_transformations(string: str, n: int) -> str:
    for _ in range(n):
        string = transform_string(string)
    return string


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 10")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    start = get_data(filename)
    output = get_string_after_n_transformations(start, 40)
    print(f"The answer to part 1 is {len(output)}.")
    output = get_string_after_n_transformations(output, 10)
    print(f"The answer to part 2 is {len(output)}.")


if __name__ == '__main__':
    main()
