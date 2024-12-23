def get_data() -> list[tuple[int, list[int]]]:
	with open('input.txt') as f:
		text = f.readlines()
	data = []
	for line in text:
		target, numbers = line.strip().split(": ")
		target = int(target)
		numbers = [int(n) for n in numbers.split(" ")]
		data.append((target, numbers))
	return data

def meets_target(numbers: list[int], target: int, current: int, idx: int = 1, use_concat: bool = False) -> bool:
	assert idx >= 1
	if current > target: return False

	if idx == len(numbers):
		return True if current == target else False
	
	if use_concat:
		if meets_target(numbers, target, int(str(current) + str(numbers[idx])), idx + 1, use_concat): return True
	if meets_target(numbers, target, current * numbers[idx], idx + 1, use_concat): return True
	return meets_target(numbers, target, current + numbers[idx], idx + 1, use_concat)

def answers() -> None:
	data = get_data()
	answer_part_1, answer_part_2 = 0, 0
	for target, numbers in data:
		if meets_target(numbers, target, numbers[0]):
			answer_part_1 += target
		if meets_target(numbers, target, numbers[0], use_concat=True):
			answer_part_2 += target
	print(f"The answer to part 1 is {answer_part_1}.")
	print(f"The answer to part 2 is {answer_part_2}.")

if __name__ == '__main__':
	answers()	