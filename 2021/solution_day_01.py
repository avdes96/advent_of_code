from argparse import ArgumentParser


def get_data(filename: str) -> list[int]:
    with open(filename, "r") as f:
        return list(map(int, f.read().split("\n")))


def get_solution(data: list[int], window_size: int) -> int:
    l, r = 0, window_size
    answer = 0
    while r < len(data):
        if data[r] > data[l]:
            answer += 1
        l += 1
        r += 1
    return answer


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2021 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {get_solution(data, window_size=1)}.")
    print(f"The answer to part 2 is {get_solution(data, window_size=3)}.")


if __name__ == "__main__":
    main()
