from re import findall

def get_data() -> list[tuple[int, int, int]]:
	data = []
	with open("input.txt") as f:
		for line in f:
			numbers = tuple(map(int, findall( r'\d+', line)))
			data.append(numbers)
	return data

def get_amount_wrapping_paper(length: int, width: int, height: int) -> int:
	side_areas = (length * width, length * height, width * height)
	return 2 * sum(side_areas) + min(side_areas)

def get_amount_ribbon(length: int, width: int, height: int) -> int:
	side_perimeters = ((length + width) * 2, (length + height) * 2, (width + height) * 2)
	volume = length * width * height
	return min(side_perimeters) + volume

def part_1() -> None:
	data = get_data()
	answer = 0
	for length, width, height in data:
		answer += get_amount_wrapping_paper(length, width, height)
	print(f'The answer to part 1 is {answer}.')
	

def part_2() -> None:
	answer = 0
	data = get_data()
	for length, width, height in data:
		answer += get_amount_ribbon(length, width, height)
	print(f'The answer to part 2 is {answer}.')

if __name__ == "__main__":
	part_1()
	part_2()
