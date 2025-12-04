from argparse import ArgumentParser


def get_data(filename: str) -> set[tuple[int, int]]:
    rolls = set()
    with open(filename) as f:
        for r, row in enumerate(f):
            row = row.strip()
            for c, col in enumerate(row):
                if col == "@":
                    rolls.add((r, c))
    return rolls


def is_open(rolls: set[tuple[int, int]], r: int, c: int, max_nbrs: int = 3) -> bool:
    adj = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if (nr, nc) in rolls:
                adj += 1
    return adj <= max_nbrs


def remove_rolls(rolls: set[tuple[int, int]]) -> tuple[set[tuple[int, int]], int]:
    to_remove = set()
    for r, c in rolls:
        if is_open(rolls, r, c):
            to_remove.add((r, c))
    return rolls - to_remove, len(to_remove)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 4")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    rolls = get_data(filename)
    rolls, removed = remove_rolls(rolls)
    total_removed = removed
    print(f"The answer to part 1 is {removed}.")
    while removed != 0:
        rolls, removed = remove_rolls(rolls)
        total_removed += removed
    print(f"The answer to part 2 is {total_removed}.")


if __name__ == "__main__":
    main()
