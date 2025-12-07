from argparse import ArgumentParser
from operator import add, mul
from re import findall
from typing import Callable


class Question:
    def __init__(self, op: Callable[[int, int], int]) -> None:
        self.numbers = []
        self.operator = op

    def add_number(self, n: int) -> None:
        self.numbers.append(n)

    def answer(self) -> int:
        if len(self.numbers) == 0:
            return 0
        ans = self.numbers[0]
        for n in self.numbers[1:]:
            ans = self.operator(ans, n)
        return ans


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().split("\n")


def parse_data_into_questions(data: list[str]) -> list[Question]:
    operators = findall(r"(\+|\*)", data[-1])
    function_mapping = {"+": add, "*": mul}
    questions = [Question(function_mapping[op]) for op in operators]

    for line in data[:-1]:
        numbers = list(map(int, findall(r"(\d+)", line)))
        assert len(numbers) == len(questions), f"Expected {len(questions)} numbers, got {len(numbers)}"
        for i in range(len(numbers)):
            questions[i].add_number(numbers[i])
    return questions


def parse_data_into_questions_advanced(data: list[str]) -> list[Question]:
    def find_question_ranges() -> list[tuple[int, int, Question]]:
        operator_line = data[-1]
        intervals = []
        start = None
        function_mapping = {"+": add, "*": mul}
        for idx, char in enumerate(operator_line):
            if char == " ":
                continue
            assert char in function_mapping, f"operator {char} not recognised"
            if start == None:
                start = idx
                continue
            intervals.append((start, idx - 2, Question(function_mapping[operator_line[start]])))
            start = idx
        assert start is not None, f"error parsing operator line: {operator_line}"
        intervals.append((start, len(operator_line) - 1, Question(function_mapping[operator_line[start]])))
        return intervals

    intervals = find_question_ranges()
    digit_lines_reversed = data[:-1][::-1]
    questions = []
    for start, end, question in intervals:
        for i in range(start, end + 1):
            number = 0
            digits = 0
            for line in digit_lines_reversed:
                if line[i] == " ":
                    continue
                number += (10 ** digits) * int(line[i])
                digits += 1
            question.add_number(number)
        questions.append(question)
    return questions


def find_solution(data: list[str], parsing_func: Callable[[list[str]], list[Question]]) -> int:
    questions = parsing_func(data)
    return sum(q.answer() for q in questions)


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 6")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    print(f"The answer to part 1 is {find_solution(data, parse_data_into_questions)}.")
    print(f"The answer to part 2 is {find_solution(data, parse_data_into_questions_advanced)}.")


if __name__ == "__main__":
    main()
