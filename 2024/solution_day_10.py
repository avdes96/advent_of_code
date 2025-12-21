import argparse


def get_data(filename: str) -> list[list[int]]:
    with open(filename) as f:
        return [list(map(int, line)) for line in f.read().splitlines()]


def get_score(grid: list[list[int]], x: int, y: int, seen: set[tuple[int, int]], score: int = 0, distinct: bool = False) -> int:
    if grid[y][x] == 9 and (x, y) not in seen:
        if not distinct:
            seen.add((x, y))
        return score + 1
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        proposed_x, proposed_y = x + direction[0], y + direction[1]
        if in_bounds(grid, proposed_x, proposed_y):
            if grid[proposed_y][proposed_x] - grid[y][x] == 1:
                score = get_score(grid, proposed_x, proposed_y, seen, score, distinct)
    return score


def in_bounds(grid: list[list[int]], x: int, y: int) -> bool:
    return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)


def answers(grid: list[list[int]]) -> None:
    answer_part_1 = 0
    answer_part_2 = 0
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == 0:
                answer_part_1 += get_score(grid, x, y, seen=set())
                answer_part_2 += get_score(grid, x, y, seen=set(), distinct=True)
    print(f'The answer to part 1 is {answer_part_1}.')
    print(f'The answer to part 2 is {answer_part_2}.')


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 10")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    grid = get_data(filename)
    answers(grid)


if __name__ == "__main__":
    main()
