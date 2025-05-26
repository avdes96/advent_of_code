import argparse
from collections import defaultdict


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def get_antennas(grid: list[str]) -> dict[str, list[tuple[int, int]]]:
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] != ".":
                antennas[grid[y][x]].append((x, y))
    return antennas


def get_all_combos(antennas: dict[str, list[tuple[int, int]]]) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    combos = set()
    for locs in antennas.values():
        for i in range(len(locs) - 1):
            for j in range(i + 1, len(locs)):
                combos.add((locs[i], locs[j]))
    return combos


def in_bounds(grid: list[str], x: int, y: int) -> bool:
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)


def calc_antinodes(grid: list[str], antennas: dict[str, list[tuple[int, int]]], dist: int = 2, resonance: bool = False) -> set[tuple[int, int]]:
    combos = get_all_combos(antennas)
    antinodes = set()
    for antenna_A, antenna_B in combos:
        dx = antenna_A[0] - antenna_B[0]
        dy = antenna_A[1] - antenna_B[1]

        if resonance:
            for scaler in (-1, 1):
                antinode = (antenna_A[0], antenna_A[1])
                while in_bounds(grid, antinode[0], antinode[1]):
                    antinodes.add(antinode)
                    antinode = (antinode[0] + scaler * dx, antinode[1] + scaler * dy)
        else:
            antinode_A = (antenna_A[0] + -1 * dist * dx, antenna_A[1] + -1 * dist * dy)
            antinode_B = (antenna_B[0] + dist * dx, antenna_B[1] + dist * dy)
            for antinode in (antinode_A, antinode_B):
                if in_bounds(grid, antinode[0], antinode[1]):
                    antinodes.add(antinode)
    return antinodes


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 8")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    grid = get_data(filename)
    antennas = get_antennas(grid)
    antinodes = calc_antinodes(grid, antennas)
    print(f'The answer to part 1 is {len(antinodes)}.')
    antinodes = calc_antinodes(grid, antennas, resonance=True)
    print(f'The answer to part 2 is {len(antinodes)}.')


if __name__ == "__main__":
    main()
