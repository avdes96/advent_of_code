import argparse
from re import match


def get_data(filename: str) -> list[tuple[int, int, int]]:
    pattern = r"^(\d+)\s+(\d+)\s+(\d+)$"
    data = []
    with open(filename) as f:
        for line in f:
            m = match(pattern, line.strip())
            if m is None:
                raise ValueError(f"{line.strip()} not in expected form: {pattern}")
            data.append(tuple(map(int, m.groups())))
    return data


def valid_triangle(triangle: tuple[int, int, int]) -> bool:
    if len(triangle) != 3:
        raise ValueError(f"Triangle should have 3 sides, argument is {len(triangle)} long.")
    a, b, c = triangle
    return (a + b > c) and (a + c > b) and (b + c > a)


def flip_data_from_horizontal_to_vertical(data: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    flipped_data = []
    for i in range(0, len(data), 3):
        for j in range(3):
            flipped_data.append((data[i][j], data[i + 1][j], data[i + 2][j]))
    return flipped_data


def number_valid_triangles(data: list[tuple[int, int, int]]) -> int:
    return sum(1 for t in data if valid_triangle(t))


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2016 - Day 3")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {number_valid_triangles(data)}.")
    data = flip_data_from_horizontal_to_vertical(data)
    print(f"The answer to part 2 is {number_valid_triangles(data)}.")


if __name__ == "__main__":
    main()
