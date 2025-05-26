import argparse
from re import findall


class Machine:
    def __init__(self, A_x: int, A_y: int, B_x: int, B_y: int, prize_x: int, prize_y: int) -> None:
        self.A_x = A_x
        self.A_y = A_y
        self.B_x = B_x
        self.B_y = B_y
        self.prize_x = prize_x
        self.prize_y = prize_y
        self.recalibrated = False

    def recalibrate(self, recalibration_x: int = 10_000_000_000_000, recalibration_y: int = 10_000_000_000_000) -> None:
        if not self.recalibrated:
            self.prize_x += recalibration_x
            self.prize_y += recalibration_y
            self.recalibrated = True

    def _calc_button_presses(self) -> tuple[int, int]:
        '''
        Let n_A and n_B be the number of button presses for A and B respectively.
        Then we want:
        n_A * A_x + n_B * B_x = prize_x
        n_A * A_y + n_B * B_y = prize_y
        => n_A = (B_y * prize_x - B_x * prize_y) / (A_x * B_y - A_y * B_x)
        Since n_A must be an int, we also know:
        (B_y * prize_x - B_x * prize_y) % (A_x * B_y - A_y * B_x) = 0
        Therefore:
        n_B = prize_x - (n_A * A_x)) / B_x and prize_x - (n_A * A_x)) % B_x == 0
        We return (-1, -1) to indicate no solution.
        '''
        if (self.B_y * self.prize_x - self.B_x * self.prize_y) % (self.A_x * self.B_y - self.A_y * self.B_x) != 0:
            return -1, -1
        n_A = int((self.B_y * self.prize_x - self.B_x * self.prize_y) / (self.A_x * self.B_y - self.A_y * self.B_x))
        if n_A < 0:
            return -1, -1

        if (self.prize_x - (n_A * self.A_x)) % self.B_x != 0:
            return -1, -1
        n_B = int((self.prize_x - (n_A * self.A_x)) / self.B_x)
        if n_B < 0:
            return -1, -1

        assert n_A * self.A_y + n_B * self.B_y == self.prize_y, \
            f"LHS = {n_A * self.A_y + n_B + self.B_y}, RHS = {self.prize_y}"
        return n_A, n_B

    def calc_minimum_cost(self) -> int:
        n_A, n_B = self._calc_button_presses()
        if n_A < 0 or n_B < 0:
            assert n_A < 0 and n_B < 0, "Error in calculation."
            return 0
        return self._cost(n_A, n_B)

    def _cost(self, n_A: int, n_B: int, cost_A: int = 3, cost_B: int = 1):
        return (n_A * cost_A) + (n_B * cost_B)

    def __str__(self) -> str:
        return f"Button A: X+{self.A_x}, Y+{self.A_y}; Button B: X+{self.B_x}, Y+{self.B_y}; Prize: X={self.prize_x}, Y={self.prize_y}"


def get_data(filename: str) -> list[Machine]:
    with open(filename) as f:
        data = f.readlines()
    machines = []
    for i in range(0, len(data), 4):
        a_x, a_y = map(int, findall(r'\d+', data[i]))
        b_x, b_y = map(int, findall(r'\d+', data[i + 1]))
        prize_x, prize_y = map(int, findall(r'\d+', data[i + 2]))
        machines.append(Machine(a_x, a_y, b_x, b_y, prize_x, prize_y))
    return machines


def get_solution(recalibrate_values: bool = False) -> int:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 13")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    machines = get_data(filename)
    total_cost = 0
    for machine in machines:
        if recalibrate_values:
            machine.recalibrate()
        total_cost += machine.calc_minimum_cost()
    return total_cost


def part_1() -> None:
    answer = get_solution()
    print(f"The answer to part 1 is {answer}.")


def part_2() -> None:
    answer = get_solution(recalibrate_values=True)
    print(f"The answer to part 2 is {answer}.")


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
