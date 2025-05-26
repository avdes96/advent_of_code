import argparse


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def search_grid(grid: list[str], word: str = "XMAS") -> int:
    answer = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if search_horizontal(grid, x, y, word):
                answer += 1
            if search_vertical(grid, x, y, word):
                answer += 1
            if search_upward_diagonal(grid, x, y, word):
                answer += 1
            if search_leftword_diagonal(grid, x, y, word):
                answer += 1
    return answer


def search_horizontal(grid: list[str], x: int, y: int, word: str) -> bool:
    return search_section(grid, x, y, word, x_scaler=1, y_scaler=0)


def search_vertical(grid: list[str], x: int, y: int, word: str) -> bool:
    return search_section(grid, x, y, word, x_scaler=0, y_scaler=1)


def search_upward_diagonal(grid: list[str], x: int, y: int, word: str) -> bool:
    return search_section(grid, x, y, word, x_scaler=1, y_scaler=-1)


def search_leftword_diagonal(grid: list[str], x: int, y: int, word: str) -> bool:
    return search_section(grid, x, y, word, x_scaler=1, y_scaler=1)


def search_section(grid: list[str], x: int, y: int, word: str, x_scaler: int, y_scaler: int) -> bool:
    section = ""
    for i in range(len(word)):
        if not in_bounds(grid, x + i * x_scaler, y + i * y_scaler):
            return False
        section += grid[y + i * y_scaler][x + i * x_scaler]
    return section in [word, word[::-1]]


def in_bounds(grid: list[str], x: int, y: int) -> bool:
    return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)


def part_1(grid: list[str]) -> None:
    answer = search_grid(grid)
    print(f'The answer for part 1 is {answer}.')


def part_2(grid: list[str]) -> None:
    answer = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "A":
                if valid_cross(grid, x, y):
                    answer += 1

    print(f"The answer to part 2 is {answer}.")


def valid_cross(grid: list[str], x: int, y: int) -> bool:
    letters = {'S': 2, 'M': 2}
    opposite = {'S': 'M', 'M': 'S'}
    for i in [-1, 1]:
        for j in [-1, 1]:
            if not in_bounds(grid, x + i, y + j):
                return False
            letter = grid[y + j][x + i]
            if letter in letters.keys():
                letters[letter] -= 1
                if letters[letter] < 0:
                    return False
                if not in_bounds(grid, x + i * -1, y + j * -1) \
                        or grid[y + j * -1][x + i * -1] != opposite[letter]:
                    return False
            else:
                return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 4")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    grid = get_data(filename)
    part_1(grid)
    part_2(grid)


if __name__ == "__main__":
    main()
