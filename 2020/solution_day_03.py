from argparse import ArgumentParser
from math import prod


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().split("\n")


def trees_on_route(grid: list[str], dr: int, dc: int) -> int:
    r, c, trees = 0, 0, 0
    while r < len(grid):
        if grid[r][c % len(grid[0])] == '#':
            trees += 1
        r += dr
        c += dc
    return trees


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2020 - Day 3")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    grid = get_data(filename)
    print(f"The answer to part 1 is {trees_on_route(grid, 1, 3)}.")
    dr_dc_list = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print(f"The answer to part 2 is {prod(trees_on_route(grid, dr, dc) for dr, dc in dr_dc_list)}.")


if __name__ == "__main__":
    main()
