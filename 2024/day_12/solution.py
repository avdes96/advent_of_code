import argparse
from collections import deque


class Region:
    def __init__(self) -> None:
        self._squares = set()

    def add_square(self, r: int, c: int) -> None:
        self._squares.add((r, c))

    @property
    def area(self) -> int:
        return len(self._squares)

    @property
    def perimeter(self) -> int:
        perimeter = 0
        for r, c in self._squares:
            nbrs = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in self._squares:
                    nbrs += 1
            perimeter += 4 - nbrs
        return perimeter

    @property
    def corners(self) -> int:
        # Note the number of corners a region has equals the number of sides
        corners = 0
        for r, c in self._squares:
            corners += self._calculate_corners(r, c)
        return corners

    def _calculate_corners(self, r: int, c: int) -> int:
        N = (r - 1, c) in self._squares
        S = (r + 1, c) in self._squares
        E = (r, c + 1) in self._squares
        W = (r, c - 1) in self._squares
        NE = (r - 1, c + 1) in self._squares
        NW = (r - 1, c - 1) in self._squares
        SE = (r + 1, c + 1) in self._squares
        SW = (r + 1, c - 1) in self._squares

        corners = 0
        for AC, D, C in [(W, NW, N), (N, NE, E), (E, SE, S), (S, SW, W)]:
            corners += 1 if self._is_corner(AC, D, C) else 0
        return corners

    def _is_corner(self, AC: bool, D: bool, C: bool) -> bool:
        # Consider a square, and one of its four diagonal (D) nbrs.
        # Also consider the nbr anti-clockwise (AC) and clockwise (C) from D.
        # In this example, the sqaure in question is the bottom-right, denoted by A.
        # D is top-left, AC is bottom-left and C is top-right
        # The nbrs are denoted by the lowercase a and b, where a indicates the nbr is in the same
        # region as A (and b is a different region)
        # There are 3 cases where the square has A a top-right corner:
        # bb  ab  ba
        # bA  bA  aA
        # And 5 cases where there it does not have a top-right corner:
        # bb  ba  ab  aa  aa
        # aA  bA  aA  bA  aA
        # This logic also holds for the rotations of A (i.e., A is bottom-left, top-left or top-right)

        # True if neighbour is in same region, else False
        if (AC, D, C) in [(False, False, False), (False, True, False), (True, False, True)]:
            return True
        return False


def get_data(filename: str) -> list[Region]:
    regions = []
    seen = set()
    with open(filename) as f:
        grid = f.read().splitlines()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in seen:
                region = construct_region(grid, r, c, seen)
                regions.append(region)
    return regions


def construct_region(grid, r: int, c: int, seen: set[tuple[int, int]]) -> Region:
    region = Region()
    queue = deque([(r, c)])
    seen.add((r, c))
    region_char = grid[r][c]
    region.add_square(r, c)
    while queue:
        r, c = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in seen and in_bounds(grid, nr, nc) \
                    and grid[nr][nc] == region_char:
                queue.append((nr, nc))
                seen.add((nr, nc))
                region.add_square(nr, nc)
    return region


def in_bounds(grid: list[str], r: int, c: int) -> bool:
    return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])


def get_solution(filename: str) -> None:
    regions = get_data(filename)
    total_cost = 0
    total_discounted_cost = 0
    for region in regions:
        total_cost += region.area * region.perimeter
        total_discounted_cost += region.area * region.corners
    print(f"The answer to part 1 is {total_cost}.")
    print(f"The answer to part 2 is {total_discounted_cost}.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 12")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    get_solution(filename)


if __name__ == "__main__":
    main()
