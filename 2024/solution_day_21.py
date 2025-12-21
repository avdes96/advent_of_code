import argparse
from collections import deque


class Keypad:
    def __init__(self) -> None:
        self.keys = self._init_keys()
        self.row, self.col = self._init_start_pos()
        self.button_sequences = self._create_button_sequences()

    def _create_button_sequences(self) -> dict[tuple[str, str], list[str]]:
        button_sequences = {}
        all_keys = self._find_all_keys()
        for i in range(len(all_keys)):
            for j in range(len(all_keys)):
                start, end = all_keys[i], all_keys[j]
                if start != end:
                    sequences = self._find_shortest_paths(all_keys[i], all_keys[j])
                    sequences = [sequence + "A" for sequence in sequences]
                else:
                    sequences = ["A"]
                button_sequences[(start, end)] = sequences
        return button_sequences

    def _find_shortest_paths(self, start: str, end: str) -> list[str]:
        shortest_paths = []
        r, c = self._get_row_col(start)
        q = deque([(r, c, "")])
        while q:
            r, c, path = q.popleft()
            if not shortest_paths or len(path) <= len(shortest_paths[0]):
                for dr, dc, arrow in [(0, 1, ">"), (0, -1, "<"), (1, 0, "v"), (-1, 0, "^")]:
                    current_key = self.keys[r + dr][c + dc]
                    if current_key == ".":
                        continue
                    new_path = path + arrow
                    if current_key == end:
                        if not shortest_paths or len(new_path) == len(shortest_paths[0]):
                            shortest_paths.append(new_path)
                        continue
                    q.append((r + dr, c + dc, new_path))
        return shortest_paths

    def _find_all_keys(self) -> list[str]:
        keys = []
        for r in self.keys:
            for c in r:
                if c != ".":
                    keys.append(c)
        return keys

    def _init_keys(self) -> list[list[str]]:
        raise NotImplementedError("_init_keys method not implemented.")

    def _init_start_pos(self) -> tuple[int, int]:
        return self._get_row_col("A")

    def _get_row_col(self, key: str) -> tuple[int, int]:
        for r in range(len(self.keys)):
            for c in range(len(self.keys[0])):
                if self.keys[r][c] == key:
                    return r, c
        raise ValueError(f"{key} not in keys.")


class Numeric_Keypad(Keypad):
    def __init__(self) -> None:
        super().__init__()

    def _init_keys(self) -> list[list[str]]:
        return [
            ['.', '.', '.', '.', '.'],
            ['.', '7', '8', '9', '.'],
            ['.', '4', '5', '6', '.'],
            ['.', '1', '2', '3', '.'],
            ['.', '.', '0', 'A', '.'],
            ['.', '.', '.', '.', '.'],
        ]


class Directional_Keypad(Keypad):
    def __init__(self) -> None:
        super().__init__()

    def _init_keys(self) -> list[list[str]]:
        return [
            ['.', '.', '.', '.', '.'],
            ['.', '.', '^', 'A', '.'],
            ['.', '<', 'v', '>', '.'],
            ['.', '.', '.', '.', '.'],
        ]


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def find_shortest_sequence(code: str, num_robots: int) -> int:
    def helper(target: str, max_depth: int, numeric_keypad: Numeric_Keypad,
               directional_keypad: Directional_Keypad, cache: dict[tuple[str, str, int], int], current: int = 0) -> int:
        if current == max_depth:
            return len(target)
        keypad = numeric_keypad if current == 0 else directional_keypad
        target = "A" + target
        sequence_length = 0
        for i in range(len(target) - 1):
            start, end = target[i], target[i+1]
            if (start, end, current) not in cache:
                button_sequences = keypad.button_sequences[(start, end)]
                best = float("inf")
                for sequence in button_sequences:
                    best = min(best, helper(sequence, max_depth, numeric_keypad, directional_keypad, cache, current + 1))
                cache[(start, end, current)] = best
            sequence_length += cache[(start, end, current)]
        return sequence_length
    max_depth = num_robots + 1
    numeric_keypad, directional_keypad = Numeric_Keypad(), Directional_Keypad()
    cache = {}
    return helper(code, max_depth, numeric_keypad, directional_keypad, cache)


def get_solution(codes: list[str], num_robots: int) -> int:
    answer = 0
    for code in codes:
        answer += int(code[:-1]) * find_shortest_sequence(code, num_robots)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 21")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    codes = get_data(filename)
    answer_part_1 = get_solution(codes, 2)
    print(f"The answer to part 1 is {answer_part_1}.")
    answer_part_2 = get_solution(codes, 25)
    print(f"The answer to part 2 is {answer_part_2}.")


if __name__ == "__main__":
    main()
