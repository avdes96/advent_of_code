def get_data() -> list[str]:
	with open("input.txt") as f:
		data = f.readlines()
	data = [line.strip() for line in data]
	return data

def part_1() -> None:
	data = get_data()
	answer = search_grid(data)
	print(f'The answer for part 1 is {answer}.')

def search_grid(grid: list[str], word: str="XMAS") -> int:
	answer = 0
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if search_horizontal(grid, x, y, word): 
				answer += 1
			if search_vertical(grid, x, y, word): 
				answer += 1
			if search_upward_diagonal(grid, x, y, word): 
				answer += 1
			if search_leftword_diagonal(grid, x, y, word): 
				answer += 1
	return answer

def search_horizontal(grid: list[str], x: int, y: int, word: str) -> bool:
	return search_section(grid, x, y, word, x_scaler=1, y_scaler=0)

def search_vertical(grid: list[str], x: int, y: int, word: str) -> bool:
	return search_section(grid, x, y, word, x_scaler=0, y_scaler=1)

def search_upward_diagonal(grid: list[str], x: int, y: int, word: str) -> bool:
	return search_section(grid, x, y, word, x_scaler=1, y_scaler=-1)
	
def search_leftword_diagonal(grid: list[str], x: int, y: int, word: str) -> bool:
	return search_section(grid, x, y, word, x_scaler=1, y_scaler=1)

def search_section(grid: list[str], x: int, y: int, word: str, x_scaler, y_scaler) -> bool:
	section = ""
	for i in range(len(word)):
		if not in_bounds(grid, x + i * x_scaler, y + i * y_scaler):
			return False
		section += grid[y + i * y_scaler][x + i * x_scaler]
	return section in [word, word[::-1]]

def in_bounds(grid: list[str], x: int, y: int) -> bool:
	if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
		return False
	return True

def part_2() -> None:
	grid = get_data()
	answer = 0
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == "A":
				if valid_cross(grid, x, y):
					answer += 1

	print(f"The answer to part 2 is {answer}.")

def valid_cross(grid: list[str], x: int, y: int) -> bool:
	letters = {'S': 2, 'M': 2}
	opposite = {'S': 'M', 'M': 'S'}
	for i in [-1, 1]:
		for j in [-1 , 1]:
			if not in_bounds(grid, x + i, y + j):
				return False
			letter = grid[y + j][x + i]
			if letter in letters.keys():
				letters[letter] -= 1
				if letters[letter] < 0:
					return False
				if not in_bounds(grid, x + i * -1, y + j * -1) \
				or grid[y + j * -1][x + i * -1] != opposite[letter]:
					return False
			else:
				return False
	return True

if __name__ == "__main__":
	part_1()
	part_2()