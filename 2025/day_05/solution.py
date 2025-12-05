from argparse import ArgumentParser


def get_data(filename: str) -> tuple[list[tuple[int, int]], list[int]]:
    with open(filename) as f:
        intervals_str, ingredients_str = f.read().split("\n\n")
    intervals = []
    for interval_str in intervals_str.split("\n"):
        intervals.append(tuple(map(int, interval_str.split("-"))))
    ingredients = list(map(int, ingredients_str.split("\n")))
    return intervals, ingredients


def reduce_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_intervals = sorted(intervals)
    stack = [sorted_intervals[0]]
    for interval in sorted_intervals[1:]:
        if interval[0] <= stack[-1][-1]:
            prev = stack.pop()
            stack.append((prev[0], max(prev[1], interval[1])))
        else:
            stack.append(interval)
    return stack


def num_fresh_total(intervals: list[tuple[int, int]]) -> int:
    reduced_intervals = reduce_intervals(intervals)
    return sum(i[1] - i[0] + 1 for i in reduced_intervals)


def is_fresh(ingredient: int, intervals: list[tuple[int, int]]) -> bool:
    for start, end in intervals:
        if start <= ingredient <= end:
            return True
    return False


def num_fresh_from_given_ingredients(ingredients: list[int], intervals: list[tuple[int, int]]) -> int:
    return sum(1 if is_fresh(i, intervals) else 0 for i in ingredients)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 5")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    intervals, ingredients = get_data(filename)
    print(f"The answer to part 1 is {num_fresh_from_given_ingredients(ingredients, intervals)}.")
    print(f"The answer to part 2 is {num_fresh_total(intervals)}.")


if __name__ == "__main__":
    main()
