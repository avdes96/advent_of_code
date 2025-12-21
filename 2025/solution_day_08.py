from argparse import ArgumentParser
from collections import defaultdict
from collections.abc import Hashable
from dataclasses import dataclass
from math import prod


@dataclass(frozen=True)
class Point:
    ID: int
    x: int
    y: int
    z: int


class Union_Find:
    def __init__(self) -> None:
        self.parent = {}
        self.rank = defaultdict(lambda: 1)

    def find(self, node: Hashable) -> Hashable:
        if node not in self.parent:
            self.parent[node] = node
        elif node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, A: Hashable, B: Hashable) -> bool:
        par_A, par_B = self.find(A), self.find(B)
        if par_A == par_B:
            return True
        if par_A != par_B:
            if self.rank[par_A] >= self.rank[par_B]:
                self.parent[par_B] = self.parent[par_A]
                if self.rank[par_A] == self.rank[par_B]:
                    self.rank[par_A] += 1
            else:
                self.parent[par_A] = self.parent[par_B]
        return False

    def group_sizes(self) -> dict[Hashable, int]:
        out = defaultdict(int)
        for a in self.parent:
            out[self.find(a)] += 1
        return out


def get_data(filename: str) -> dict[int, Point]:
    out = {}
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            x, y, z = map(int, line.split(","))
            out[i] = Point(i, x, y, z)
    return out


def euclidean_dist(A: Point, B: Point) -> int:
    return (A.x - B.x)**2 + (A.y-B.y)**2 + (A.z-B.z)**2


def order_points(data: dict[int, Point]) -> list[tuple[Point, Point, int]]:
    distances = []
    for i in range(1, len(data)):
        for j in range(i):
            point_A = data[i]
            point_B = data[j]
            distances.append((point_A, point_B, euclidean_dist(point_A, point_B)))
    distances.sort(key=lambda x: x[-1])
    return distances


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 8")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    ordered_points = order_points(data)
    answer_1 = None
    answer_2 = None
    uf = Union_Find()
    for i, val in enumerate(ordered_points):
        point_A, point_B, _ = val
        in_same_group = uf.union(point_A, point_B)
        if not in_same_group:
            answer_2 = point_A.x * point_B.x
        if i == 1000:
            answer_1 = prod(sorted(uf.group_sizes().values(), reverse=True)[:3])

    print(f"The answer to part 1 is {answer_1}.")
    print(f"The answer to part 2 is {answer_2}.")


if __name__ == "__main__":
    main()
