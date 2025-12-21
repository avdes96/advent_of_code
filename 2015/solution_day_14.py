import argparse
from enum import Enum
from re import search


class Reindeer_State(Enum):
    FLYING = 0
    RESTING = 1


class Reindeer:
    def __init__(self, name: str, speed: int, flying_time: int, rest_time: int) -> None:
        self._name = name
        self._speed = speed
        self._flying_time = flying_time
        self._rest_time = rest_time
        self.reset()

    def update_n_seconds(self, n: int) -> None:
        time = 0
        while time < n:
            if self._state == Reindeer_State.FLYING:
                if self._time_in_current_state < self._flying_time:
                    self._distance += self._speed
                    self._time_in_current_state += 1
                    time += 1
                else:
                    self._state = Reindeer_State.RESTING
                    self._time_in_current_state = 0
            elif self._state == Reindeer_State.RESTING:
                if self._time_in_current_state < self._rest_time:
                    self._time_in_current_state += 1
                    time += 1
                else:
                    self._state = Reindeer_State.FLYING
                    self._time_in_current_state = 0

    def add_point(self) -> None:
        self._points += 1

    @property
    def distance(self) -> int:
        return self._distance

    @property
    def points(self) -> int:
        return self._points

    def reset(self) -> None:
        self._distance = 0
        self._state = Reindeer_State.FLYING
        self._time_in_current_state = 0
        self._points = 0


class Race:
    def __init__(self) -> None:
        self.reindeers = []

    def add_reindeer(self, reindeer: Reindeer) -> None:
        self.reindeers.append(reindeer)

    def race_for_n_seconds(self, n: int) -> None:
        for _ in range(n):
            for reindeer in self.reindeers:
                reindeer.update_n_seconds(1)
            best_dist = self.distance_leader().distance
            for reindeer in self.reindeers:
                if reindeer.distance == best_dist:
                    reindeer.add_point()

    def distance_leader(self) -> Reindeer:
        return max(self.reindeers, key=lambda r: r.distance)

    def points_leader(self) -> Reindeer:
        return max(self.reindeers, key=lambda r: r.points)


def get_data(filename: str) -> Race:
    race = Race()
    pattern = r'^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$'
    with open(filename) as f:
        for line in f:
            pattern_match = search(pattern, line.strip())
            assert pattern_match is not None, f"'{line}' is not in expected form."
            name, speed, flying_time, rest_time = pattern_match.groups()
            race.add_reindeer(Reindeer(name, int(speed), int(flying_time), int(rest_time)))
    return race


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 14")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    race = get_data(filename)
    race_time = 1000 if "test" in filename else 2503
    race.race_for_n_seconds(race_time)
    print(f"The answer to part 1 is {race.distance_leader().distance}.")
    print(f"The answer to part 2 is {race.points_leader().points}.")


if __name__ == '__main__':
    main()
