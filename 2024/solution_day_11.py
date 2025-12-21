import argparse


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readline().strip().split(" ")


def get_total_stones(line: list[str], iterations: int) -> int:
    answer = 0
    resulting_stones_lookup, transformation_lookup = {}, {}
    for stone in line:
        answer += get_resulting_stones(stone, resulting_stones_lookup, transformation_lookup, iterations)
    return answer


def transform_stone(digit: str, transformation_lookup: dict[str, list[str]]) -> list[str]:
    if digit in transformation_lookup:
        return transformation_lookup[digit]
    elif digit == '0':
        transformation = ['1']
    elif len(digit) % 2 == 0:
        m = len(digit) // 2
        transformation = [str(int(digit[:m])), str(int(digit[m:]))]
    else:
        transformation = [str(int(digit) * 2024)]
    transformation_lookup[digit] = transformation
    return transformation


def get_resulting_stones(stone: str, resulting_stones_lookup: dict[str, dict[int, int]], transformation_lookup: dict[str, list[str]], max_depth: int, depth: int = 0) -> int:
    if stone in resulting_stones_lookup:
        if depth in resulting_stones_lookup[stone]:
            return resulting_stones_lookup[stone][depth]

    if depth == max_depth:
        return 1

    transformation = transform_stone(stone, transformation_lookup)
    resulting_stones = get_resulting_stones(
        transformation[0], resulting_stones_lookup, transformation_lookup, max_depth, depth + 1)
    if len(transformation) == 2:
        resulting_stones += get_resulting_stones(transformation[1],
                                                 resulting_stones_lookup, transformation_lookup, max_depth, depth + 1)

    if stone not in resulting_stones_lookup:
        resulting_stones_lookup[stone] = {}
    resulting_stones_lookup[stone][depth] = resulting_stones
    return resulting_stones


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 11")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    line = get_data(filename)
    print(f"The answer for part 1 is {get_total_stones(line, 25)}.")
    print(f"The answer for part 2 is {get_total_stones(line, 75)}.")


if __name__ == '__main__':
    main()
