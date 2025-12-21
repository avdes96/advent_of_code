from argparse import ArgumentParser
from functools import cache


def get_data(filename: str) -> dict[str, list[str]]:
    graph = {}
    with open(filename) as f:
        for line in f:
            in_node, out_nodes = line.strip().split(": ")
            graph[in_node] = out_nodes.split(" ")
    return graph


def num_paths(graph: dict[str, list[str]]) -> int:
    @cache
    def helper(node: str) -> int:
        if node == "out":
            return 1
        return sum(helper(nbr) for nbr in graph[node])
    return helper("you")


def num_paths_advanced(graph: dict[str, list[str]]) -> int:
    @cache
    def helper(node: str, seen_dac: bool, seen_fft: bool) -> int:
        if node == "out":
            return 1 if (seen_dac and seen_fft) else 0
        if node == "dac":
            seen_dac = True
        if node == "fft":
            seen_fft = True
        return sum(helper(nbr, seen_dac, seen_fft) for nbr in graph[node])
    return helper("svr", False, False)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 11")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    graph = get_data(filename)
    print(f"The answer to part 1 is {num_paths(graph)}.")
    print(f"The answer to part 2 is {num_paths_advanced(graph)}.")


if __name__ == "__main__":
    main()
