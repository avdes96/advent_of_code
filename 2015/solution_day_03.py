import argparse


class Person:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def up(self) -> None:
        self.y -= 1

    def down(self) -> None:
        self.y += 1

    def left(self) -> None:
        self.x -= 1

    def right(self) -> None:
        self.x += 1

    @property
    def pos(self) -> tuple[int, int]:
        return self.x, self.y


def get_data(filename: str) -> str:
    with open(filename) as f:
        return f.read().strip()


def update_position(person: Person, direction: str) -> None:
    match direction:
        case '>': person.right()
        case '<': person.left()
        case '^': person.up()
        case 'v': person.down()
        case _: raise ValueError(f"Direction {direction} not supported.")


def get_solution(directions: str, num_people: int, start_x: int = 0, start_y: int = 0) -> int:
    people = [Person() for _ in range(num_people)]
    seen = set()
    seen.add((start_x, start_y))
    for idx, direction in enumerate(directions):
        person_idx = idx % num_people
        update_position(people[person_idx], direction)
        seen.add((people[person_idx].pos))
    return len(seen)


def main():
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 3")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    directions = get_data(filename)
    print(f"The answer to part 1 is {get_solution(directions, num_people=1)}.")
    print(f"The answer to part 2 is {get_solution(directions, num_people=2)}.")


if __name__ == '__main__':
    main()
