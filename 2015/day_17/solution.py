import argparse


def get_data(filename: str) -> tuple[int, list[int]]:
    target = 25 if "test" in filename else 150
    with open(filename) as f:
        containers = list(map(int, f.read().splitlines()))
    return target, containers


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 17")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    target, containers = get_data(filename)
    containers.sort()
    combinations = [[]]
    for size in containers:
        combinations += [[size] + combo for combo in combinations if size + sum(combo) <= target]
    num_valid_containers = 0
    min_containers = float('inf')
    counts = {}
    for combo in combinations:
        if sum(combo) == target:
            num_valid_containers += 1
            num_containers = len(combo)
            counts[num_containers] = counts.get(num_containers, 0) + 1
            min_containers = min(min_containers, num_containers)
    print(f"The answer to part 1 is {num_valid_containers}.")
    print(f"The answer to part 2 is {counts[min_containers]}.")


if __name__ == "__main__":
    main()
