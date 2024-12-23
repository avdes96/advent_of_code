class Direction:
	def __init__(self) -> None:
		self._lookup = [(0, -1), (1, 0), (0, 1), (-1, 0)]
		self._i = 0
			
	def update(self) -> None:
		self._i += 1
		if self._i >= len(self._lookup):
			self._i = 0

	def dx(self) -> int:
		return self._lookup[self._i][0]
	
	def dy(self) -> int:
		return self._lookup[self._i][1]
	
	def __str__(self) -> str:
		match self._i:
			case 0: return "U"
			case 1: return "R"
			case 2: return "D"
			case 3: return "L"
		
def get_data() -> list[list[str]]:
	with open("input.txt") as f:
		data = f.readlines()
	return [list(line.strip()) for line in data]

def find_starting_point(grid: list[list[str]]) -> tuple[int, int]:
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == '^':
				return x, y
	raise ValueError("Starting point not found.")

def in_bounds(grid: list[list[str]], x: int, y: int) -> bool:
	return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

def is_valid_sequence(grid: list[list[str]], x: int, y: int) -> tuple[bool, None | set[tuple[int, int]]]:
	direction = Direction()
	seen = set()
	while True: # We know either that the position will be out of bounds or result in a loop
		move = (x, y, str(direction))
		if move in seen:
			return False, None
		seen.add(move)
		proposed_square_valid = False
		while not proposed_square_valid:
			proposed_x, proposed_y = x + direction.dx(), y + direction.dy()
			if not in_bounds(grid, proposed_x, proposed_y):
				return True, set((x, y) for (x, y, _) in seen)
			if grid[y + direction.dy()][x + direction.dx()] == '#':
				direction.update()
			else:
				proposed_square_valid = True
		x += direction.dx()
		y += direction.dy()

def answers() -> None:
	grid = get_data()
	start_x, start_y = find_starting_point(grid)
	_, squares = is_valid_sequence(grid, start_x, start_y)
	print(f"The answer to part 1 is {len(squares)}.")
	answer = 0
	for x, y in squares:
		if grid[y][x] == ".":
			grid[y][x] = "#"
			if not is_valid_sequence(grid, start_x, start_y)[0]:
				answer += 1
			grid[y][x] = "."
	print(f"The answer to part 2 is {answer}")

if __name__ == "__main__":
	answers()
