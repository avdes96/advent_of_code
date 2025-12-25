from argparse import ArgumentParser


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().strip()))


def get_solution(data: list[int], offset: int) -> int:
    answer = 0
    for idx in range(len(data)):
        other_idx = (idx + offset) % len(data)
        if data[idx] == data[other_idx]:
            answer += data[idx]
    return answer


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2017 - Day 1")
    parser.add_argument(
        "input_filename", type=str, help="File containing problem input."
    )
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {get_solution(data, 1)}.")
    print(f"The answer to part 2 is {get_solution(data, len(data) // 2)}.")


if __name__ == "__main__":
    main()
