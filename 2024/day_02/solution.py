import argparse
from collections.abc import Callable
from enum import Enum


class Direction(Enum):
    INCREASING = 0
    DECREASING = 1
    UNDETERMINED = 2


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        data = f.read().splitlines()
    return data


def solve(filename: str, row_safe_function: Callable[[list], bool]) -> int:
    data = get_data(filename)
    answer = 0
    for line in data:
        line = list(map(int, line.strip().split(" ")))
        if row_safe_function(line):
            answer += 1
    return answer


def row_safe_part_1(row: list[int]) -> bool:
    direction = Direction.UNDETERMINED
    for i in range(1, len(row)):
        val_l, val_r = row[i - 1], row[i]
        if val_l == val_r:
            return False
        elif val_l < val_r:
            if direction is Direction.UNDETERMINED:
                direction = Direction.INCREASING
            elif direction is Direction.DECREASING:
                return False
            if val_r - val_l > 3:
                return False
        else:
            if direction is Direction.UNDETERMINED:
                direction = Direction.DECREASING
            elif direction is Direction.INCREASING:
                return False
            if val_l - val_r > 3:
                return False
    return True


def row_safe_part_2(row: list[int]) -> bool:
    def row_safe_part_2_helper(row: list, l: int, r: int, level_removed: bool, direction: Direction) -> bool:
        if r >= len(row):
            return True
        val_l, val_r = row[l], row[r]
        if val_l < val_r:
            if not (direction is Direction.DECREASING or val_r - val_l > 3):
                if row_safe_part_2_helper(row, l + 1, r + 1, level_removed, Direction.INCREASING):
                    return True
        elif val_l > val_r:
            if not (direction is Direction.INCREASING or val_l - val_r > 3):
                if row_safe_part_2_helper(row, l + 1, r + 1, level_removed, Direction.DECREASING):
                    return True
        if level_removed:
            return False
        if l == 0:
            new_row = row[1:]
            if row_safe_part_2_helper(new_row, 0, 1, True, Direction.UNDETERMINED):
                return True
        new_row = row[:r] + row[r+1:]
        if row_safe_part_2_helper(new_row, l, r, True, direction):
            return True
        return False
    return row_safe_part_2_helper(row, 0, 1, False, Direction.UNDETERMINED)


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 2")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    print(f"The answer for part 1 is {solve(filename, row_safe_part_1)}.")
    print(f"The answer for part 2 is {solve(filename, row_safe_part_2)}.")


if __name__ == '__main__':
    main()
