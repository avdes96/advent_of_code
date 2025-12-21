from argparse import ArgumentParser
from collections import deque
from functools import cache


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split("\n")


def find_start(grid: list[str]) -> tuple[int, int]:
    for i, c in enumerate(grid[0]):
        if c == "S":
            return (0, i)
    raise ValueError(f"First line of grid does not contain S: {grid[0]}")


def find_num_splits(grid: list[str]) -> int:
    start = find_start(grid)
    q = deque([start])
    seen = set()
    splits = 0
    while q:
        r, c = q.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))
        if grid[r][c] == "^":
            splits += 1
            q.append((r, c-1))
            q.append((r, c+1))
            continue
        if r + 1 == len(grid):
            continue
        q.append((r + 1, c))
    return splits


def find_num_timelines(grid: list[str]) -> int:
    @cache
    def helper(r: int, c: int) -> int:
        if r == len(grid):
            return 0
        if grid[r][c] == "^":
            return 1 + helper(r, c + 1) + helper(r, c - 1)
        return helper(r + 1, c)

    start = find_start(grid)
    return 1 + helper(*start)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 7")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    grid = get_data(filename)
    print(f"The answer to part 1 is {find_num_splits(grid)}.")
    print(f"The answer to part 2 is {find_num_timelines(grid)}.")


if __name__ == "__main__":
    main()
