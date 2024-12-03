import re

def get_data() -> str:
	with open("input.txt") as f:
		data = f.read()
	return data

def part_1() -> None:
	data = get_data()
	answer = 0
	pattern=r"mul\(\d+,\d+\)"
	for match in re.finditer(pattern, data):
		digit_pattern = '\d+'
		digits = re.findall(digit_pattern, match.group(0))
		answer += int(digits[0]) * int(digits[1])
	print(f"The answer for part 1 is {answer}.")

def part_2() -> None:
	data = get_data()
	answer = 0
	pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
	multiply = True
	for match in re.finditer(pattern, data):
		if match.group(0) == "do()":
			multiply = True
		elif match.group(0) == "don't()":
			multiply = False
		else:
			if multiply:
				digit_pattern = '\d+'
				digits = re.findall(digit_pattern, match.group(0))
				answer += int(digits[0]) * int(digits[1])
	print(f"The answer for part 2 is {answer}.")

if __name__ == '__main__':
	part_1()
	part_2()