import argparse


def get_data(filename: str) -> list[tuple[int, list[int]]]:
    def parse_line(line: str) -> tuple[int, list[int]]:
        target, numbers = line.split(": ")
        target = int(target)
        numbers = list(map(int, numbers.split(" ")))
        return target, numbers

    with open(filename) as f:
        return list(map(parse_line, f.read().splitlines()))


def meets_target(numbers: list[int], target: int, current: int, idx: int = 1, use_concat: bool = False) -> bool:
    assert idx >= 1
    if current > target:
        return False

    if idx == len(numbers):
        return True if current == target else False

    if use_concat:
        if meets_target(numbers, target, int(str(current) + str(numbers[idx])), idx + 1, use_concat):
            return True
    if meets_target(numbers, target, current * numbers[idx], idx + 1, use_concat):
        return True
    return meets_target(numbers, target, current + numbers[idx], idx + 1, use_concat)


def answers(data: list[tuple[int, list[int]]]) -> None:
    answer_part_1, answer_part_2 = 0, 0
    for target, numbers in data:
        if meets_target(numbers, target, numbers[0]):
            answer_part_1 += target
            answer_part_2 += target  # If it equals without using concat, we don't need to check it using concat
        elif meets_target(numbers, target, numbers[0], use_concat=True):
            answer_part_2 += target
    print(f"The answer to part 1 is {answer_part_1}.")
    print(f"The answer to part 2 is {answer_part_2}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 7")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    answers(data)


if __name__ == '__main__':
    main()
