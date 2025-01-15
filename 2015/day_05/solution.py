def get_data() -> list[str]:
	with open("input.txt") as f:
		return f.read().splitlines()

def string_nice(string: str) -> bool:
	vowels = set(['a', 'e', 'i', 'o', 'u'])
	num_vowels = 0
	contains_double = False
	invalid_pairs = set(['ab', 'cd', 'pq','xy'])
	for i in range(len(string)):
		if string[i] in vowels:
			num_vowels += 1
		if i < len(string) - 1:
			if string[i] == string[i+1]:
				contains_double = True
			if string[i:i+2] in invalid_pairs:
				return False
	return num_vowels >= 3 and contains_double

def string_nice_update(string: str) -> bool:
	pair_repeat, letter_between_repeat = False, False
	seen = {}
	for i in range(len(string)):
		if i < len(string) - 2:
			if string[i] == string[i + 2]:
				letter_between_repeat = True
		if i < len(string) - 1:
			pair = string[i:i+2]
			if pair in seen:
				if seen[pair][1] != i:
					pair_repeat = True
			else:
				seen[pair] = (i, i + 1)
	return pair_repeat and letter_between_repeat

def get_solution() -> None:
	data = get_data()
	answer_part_1 = 0
	answer_part_2 = 0
	for string in data:
		if string_nice(string):
			answer_part_1 += 1
		if string_nice_update(string):
			answer_part_2 += 1

	print(f"The answer to part 1 is {answer_part_1}.")
	print(f"The answer to part 2 is {answer_part_2}.")

if __name__ == "__main__":
	get_solution()