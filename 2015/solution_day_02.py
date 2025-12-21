import argparse
from re import findall


def get_data(filename: str) -> list[tuple[int, int, int]]:
    data = []
    with open(filename) as f:
        for line in f:
            numbers = tuple(map(int, findall(r'\d+', line)))
            data.append(numbers)
    return data


def get_amount_wrapping_paper(length: int, width: int, height: int) -> int:
    side_areas = (length * width, length * height, width * height)
    return 2 * sum(side_areas) + min(side_areas)


def get_amount_ribbon(length: int, width: int, height: int) -> int:
    side_perimeters = ((length + width) * 2, (length + height) * 2, (width + height) * 2)
    volume = length * width * height
    return min(side_perimeters) + volume


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 2")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    answer_part_1 = 0
    answer_part_2 = 0
    for length, width, height in data:
        answer_part_1 += get_amount_wrapping_paper(length, width, height)
        answer_part_2 += get_amount_ribbon(length, width, height)
    print(f'The answer to part 1 is {answer_part_1}.')
    print(f'The answer to part 2 is {answer_part_2}.')


if __name__ == "__main__":
    main()
