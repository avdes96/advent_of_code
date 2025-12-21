import argparse


class Person:
    def __init__(self, x: int = 0, y: int = 0, direction: str = 'E') -> None:
        self.x = x
        self.start_x = x
        self.y = y
        self.start_y = y
        self.direction = direction
        self.visited = set([(x, y)])

    def _rotate(self, rotation: str) -> None:
        assert rotation in ['L', 'R'], f"Rotation {rotation} not valid."
        d_idx = {"L": -1, "R": 1}[rotation]
        directions = ['N', 'E', 'S', 'W']
        idx = (directions.index(self.direction) + d_idx) % len(directions)
        self.direction = directions[idx]

    def _walk(self) -> None:
        dx, dy = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}[self.direction]
        self.x += dx
        self.y += dy

    def follow_instructions(self, instructions: list[str], end_at_loc_first_visited_twice: bool = False) -> None:
        for instruction in instructions:
            rotation, steps = instruction[0], int(instruction[1:])
            self._rotate(rotation)
            for _ in range(steps):
                self._walk()
                if end_at_loc_first_visited_twice and (self.x, self.y) in self.visited:
                    return
                self.visited.add((self.x, self.y))

    def distance_from_start(self) -> int:
        return abs(self.start_x - self.x) + abs(self.start_y - self.y)


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().strip().split(", ")


def get_solution(filename: str, end_at_loc_first_visited_twice: bool = False) -> int:
    instructions = get_data(filename)
    person = Person()
    person.follow_instructions(instructions, end_at_loc_first_visited_twice)
    return person.distance_from_start()


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2016 - Day 1")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    print(f"The answer for part 1 is {get_solution(filename)}.")
    print(f"The answer for part 2 is {get_solution(filename, end_at_loc_first_visited_twice=True)}.")


if __name__ == '__main__':
    main()
