import argparse


class Computer:
    def __init__(self, val_reg_a: int = 0, val_reg_b: int = 0) -> None:
        self._regs = {"a": val_reg_a, "b": val_reg_b}

    def value_in_reg(self, reg: str) -> int:
        return self._regs[reg]

    def run_instructions(self, instructions: list[str]) -> None:
        ptr = 0
        while ptr < len(instructions):
            instruction = instructions[ptr]
            command, vals = instruction.split(" ", maxsplit=1)
            match command:
                case "hlf":
                    reg = vals
                    self._regs[reg] //= 2
                    ptr += 1
                case "tpl":
                    reg = vals
                    self._regs[reg] *= 3
                    ptr += 1
                case "inc":
                    reg = vals
                    self._regs[reg] += 1
                    ptr += 1
                case "jmp":
                    offset = int(vals)
                    ptr += offset
                case "jie":
                    reg, offset = vals.split(", ")
                    offset = int(offset)
                    if self._regs[reg] % 2 == 0:
                        ptr += offset
                    else:
                        ptr += 1
                case "jio":
                    reg, offset = vals.split(", ")
                    offset = int(offset)
                    if self._regs[reg] == 1:
                        ptr += offset
                    else:
                        ptr += 1
                case _: raise ValueError(f"{command} not supported.")


def get_data(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def get_solution(instructions: list[str], val_reg_a: int = 0) -> int:
    computer = Computer(val_reg_a=val_reg_a)
    computer.run_instructions(instructions)
    return computer.value_in_reg("b")


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2015 - Day 23")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    instructions = get_data(filename)
    print(f"The answer to part 1 is {get_solution(instructions)}.")
    print(f"The answer to part 2 is {get_solution(instructions, val_reg_a = 1)}.")


if __name__ == "__main__":
    main()
