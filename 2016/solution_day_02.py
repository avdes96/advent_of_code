import argparse


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split("\n")


def get_dr_dc(direction: str) -> tuple[int, int]:
    match direction:
        case 'L': return (0, -1)
        case 'R': return (0, 1)
        case 'U': return (-1, 0)
        case 'D': return (1, 0)
    raise ValueError(f"{direction} not supported.")


def get_start_r_c(start_key: str, grid: list[list[str]]) -> tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == start_key:
                return r, c
    raise ValueError(f'{start_key} not in grid.')


def get_code(grid: list[list[str]], directions: list[str], start_key: str = "5") -> str:
    r, c = get_start_r_c(start_key, grid)
    code = ""
    for sequence in directions:
        for direction in sequence:
            dr, dc = get_dr_dc(direction)
            if grid[r+dr][c+dc] != '.':
                r, c = r + dr, c + dc
        code += grid[r][c]
    return code


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2016 - Day 2")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    directions = get_data(filename)
    grid_part_1 = [[".", ".", ".", ".", "."],
                   [".", "1", "2", "3", "."],
                   [".", "4", "5", "6", "."],
                   [".", "7", "8", "9", "."],
                   [".", ".", ".", ".", "."]]
    print(f"The answer to part 1 is {get_code(grid_part_1, directions)}.")
    grid_part_2 = [[".", ".", ".", ".", ".", ".", "."],
                   [".", ".", ".", "1", ".", ".", "."],
                   [".", ".", "2", "3", "4", ".", "."],
                   [".", "5", "6", "7", "8", "9", "."],
                   [".", ".", "A", "B", "C", ".", "."],
                   [".", ".", ".", "D", ".", ".", "."],
                   [".", ".", ".", ".", ".", ".", "."]]
    print(f"The answer to part 2 is {get_code(grid_part_2, directions)}.")


if __name__ == '__main__':
    main()
