def get_data() -> list[str]:
	with open("input.txt") as f:
		return f.read().splitlines()

def get_memory_length(line: str) -> int:
	memory_length, idx = 0, 0
	while idx < len(line):
		char = line[idx]
		if char != '"':
			memory_length += 1
			if char == '\\':
				if line[idx+1] == 'x':
					idx += 4
				else:
					idx += 2
			else:
				idx += 1
		else:
			idx += 1
	return memory_length

def get_encoded_length(line: str) -> int:
	length = 0
	for char in line:
		if char == '"':
			length += 2
		elif char == '\\':
			length += 2
		else:
			length += 1
	return length + 2  # For the opening quote and closing quote marks


def get_solution() -> None:
	data = get_data()
	answer_part_1 = 0
	answer_part_2 = 0
	for line in data:
		code_rep_length = len(line)
		memory_length = get_memory_length(line)
		encoded_length = get_encoded_length(line)
		answer_part_1 += code_rep_length - memory_length
		answer_part_2 += encoded_length - code_rep_length
	print(f"The answer to part 1 is {answer_part_1}.")
	print(f"The answer to part 2 is {answer_part_2}.")


if __name__ == '__main__':
	get_solution()