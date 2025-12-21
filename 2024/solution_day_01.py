import argparse


def get_data(filename: str) -> tuple[list[int], list[int]]:
    left_lst, right_lst = [], []
    with open(filename) as f:
        for line in f:
            a, b = line.strip().split("   ")
            left_lst.append(int(a))
            right_lst.append(int(b))
    return left_lst, right_lst


def part_1(left_lst: list[int], right_lst: list[int]) -> None:
    left_lst.sort()
    right_lst.sort()
    answer = 0
    for i in range(len(left_lst)):
        answer += abs(left_lst[i] - right_lst[i])

    print(f"The answer for part 1 is {answer}.")


def part_2(left_lst: list[int], right_lst: list[int]) -> None:
    counts = {}
    for r in right_lst:
        counts[r] = counts.get(r, 0) + 1
    answer = 0
    for l in left_lst:
        answer += l * counts.get(l, 0)

    print(f"The answer for part 2 is {answer}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    left_lst, right_lst = get_data(filename)
    part_1(left_lst, right_lst)
    part_2(left_lst, right_lst)


if __name__ == "__main__":
    main()
