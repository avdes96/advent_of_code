import argparse
from re import search
from typing import Any


def get_instructions(filename: str) -> list[tuple[str, int, int, int, int]]:
    instructions = []
    pattern = r'(turn on|toggle|turn off) (\d+),(\d+) through (\d+),(\d+)'
    with open(filename) as f:
        for line in f:
            m = search(pattern, line.strip())
            if m is not None:
                command, start_x, start_y, end_x, end_y = m.group(1), int(
                    m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
                instructions.append((command, start_x, start_y, end_x, end_y))
            else:
                raise ValueError(f"Line {line} is in an invalid form.")
    return instructions


def initialise_grid(start_value: Any, grid_width: int = 1000, grid_height: int = 1000) -> list[list[Any]]:
    return [[start_value for _ in range(grid_width)] for _ in range(grid_height)]


def update_lights(grid: list[list[bool]], command: str, start_x: int, start_y: int, end_x: int, end_y: int) -> None:
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            match command:
                case 'turn on': grid[y][x] = True
                case 'turn off': grid[y][x] = False
                case 'toggle': grid[y][x] = not grid[y][x]
                case _: raise ValueError(f"{command} is not supported")


def update_brightness(grid: list[list[int]], command: str, start_x: int, start_y: int, end_x: int, end_y: int) -> None:
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            match command:
                case 'turn on': grid[y][x] += 1
                case 'turn off': grid[y][x] = max(0, grid[y][x] - 1)
                case 'toggle': grid[y][x] += 2
                case _: raise ValueError(f"{command} is not supported")


def lights_on(grid: list[list[bool]]) -> int:
    answer = 0
    for row in grid:
        for light in row:
            if light == True:
                answer += 1
    return answer


def get_brightness(grid: list[list[int]]) -> int:
    answer = 0
    for row in grid:
        for light_brightness in row:
            answer += light_brightness
    return answer


def part_1(instructions: list[tuple[str, int, int, int, int]]) -> None:
    grid = initialise_grid(start_value=False)
    for command, start_x, start_y, end_x, end_y in instructions:
        update_lights(grid, command, start_x, start_y, end_x, end_y)
    print(f"The answer to part 1 is {lights_on(grid)}.")


def part_2(instructions: list[tuple[str, int, int, int, int]]) -> None:
    grid = initialise_grid(start_value=0)
    for command, start_x, start_y, end_x, end_y in instructions:
        update_brightness(grid, command, start_x, start_y, end_x, end_y)
    print(f"The answer to part 2 is {get_brightness(grid)}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 6")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    instructions = get_instructions(filename)
    part_1(instructions)
    part_2(instructions)


if __name__ == '__main__':
    main()
