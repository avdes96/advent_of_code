from argparse import ArgumentParser
from hashlib import md5
from typing import Callable


def get_data(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read().strip()


def create_password(prefix: str, update_func: Callable[[list[str], str, int], list[str]], n_zeros: int = 5) -> str:
    i = 0
    password = ["_" for _ in range(8)]
    while "_" in password:
        hash_str = prefix + str(i)
        hash_res = md5(hash_str.encode()).hexdigest()
        if hash_res[:n_zeros] == '0' * n_zeros:
            password = update_func(password, hash_res, n_zeros)
        i += 1
    return "".join(password)


def update_simple(password: list[str], hash_res: str, n_zeros: int) -> list[str]:
    password[password.index("_")] = hash_res[n_zeros]
    return password


def update_complex(password: list[str], hash_res: str, n_zeros: int) -> list[str]:
    pos, char = hash_res[n_zeros], hash_res[n_zeros + 1]
    if not pos.isdigit():
        return password
    pos = int(pos)
    if pos < len(password) and password[pos] == '_':
        password[pos] = char
    return password


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2016 - Day 5")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    prefix = get_data(filename)
    print(f"The answer to part 1 is {create_password(prefix, update_simple)}.")
    print(f"The answer to part 2 is {create_password(prefix, update_complex)}.")


if __name__ == "__main__":
    main()
