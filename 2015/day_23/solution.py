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


def get_data() -> list[str]:
	with open("input.txt") as f:
		return f.read().splitlines()
	
	
def get_solution(val_reg_a: int = 0) -> int:
	instructions = get_data()
	computer = Computer(val_reg_a=val_reg_a)
	computer.run_instructions(instructions)
	return computer.value_in_reg("b")

	
if __name__ == "__main__":
	print(f"The answer to part 1 is {get_solution()}.")
	print(f"The answer to part 2 is {get_solution(val_reg_a = 1)}.")
