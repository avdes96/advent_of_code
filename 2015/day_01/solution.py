def get_data() -> str:
	with open('input.txt') as f:
		return f.readline().strip()

def update_level(level: int, char: str) -> int:
	match char:
		case '(': level += 1
		case ')': level -= 1
		case '_': raise ValueError(f"{char} is not expected in input.")
	return level

def find_pos_of_first_occurance(sequence: str, target: int) -> int:
	level = 0
	for pos, char in enumerate(sequence):
		level = update_level(level, char)
		if level == target:
			return pos + 1
	raise ValueError(f"Target of {target} is never reached.")
	
def part_1() -> None:
	sequence = get_data()
	level = 0
	for char in sequence:
		level = update_level(level, char)
	print(f"The answer to part 1 is {level}.")

def part_2(target: int = -1) -> None:
	sequence = get_data()
	answer = find_pos_of_first_occurance(sequence, target)
	print(f"The answer to part 2 is {answer}.")
	
if __name__ == "__main__":
	part_1()
	part_2()