from collections import deque
from collections.abc import Hashable

class Union_Find:
	def __init__(self) -> None:
		self.parent, self.size = {}, {}

	def find(self, node: Hashable) -> Hashable:
		if node not in self.parent:
			self.parent[node] = node
			self.size[node] = 1
		elif node != self.parent[node]:
			self.parent[node] = self.find(self.parent[node])
		return self.parent[node]

	def union(self, A: Hashable, B: Hashable) -> None:
		par_A, par_B = self.find(A), self.find(B)
		if par_A != par_B:
			if self.size[par_A] >= self.size[par_B]:
				self.parent[par_B] = self.parent[par_A]
				if self.size[par_A] == self.size[par_B]:
					self.size[par_A] += 1
			else:
				self.parent[par_A] = self.parent[par_B]
		
def get_data(filename: str="input.txt") -> tuple[int, int, list[tuple[int, int]]]:
	if "test" in filename:
		height, width = 7, 7
	else:
		height, width = 71, 71
	
	data = []
	with open(filename) as f:
		for line in f:
			x, y = map(int, line.strip().split(","))
			data.append((x, y))
	return height, width, data

def grid_after_n_turns(height: int, width: int, data: list[tuple[int, int]], n: int) -> list[list[str]]:
	grid = [["." for _ in range(width)] for _ in range(height)]
	for i in range(n):
		x, y = data[i]
		grid[y][x] = '#'
	return grid

def in_bounds(x: int, y: int, height: int, width: int) -> bool:
	return x >= 0 and y >= 0 and x < width and y < height

def find_shortest_route(grid: list[list[str]], start_x: int, start_y: int, end_x: int, end_y: int) -> int | None:
	queue = deque()
	queue.append((start_x, start_y, 0))
	height, width = len(grid), len(grid[0])
	seen = set()
	while queue:
		x, y, steps = queue.popleft()
		if (x, y) == (end_x, end_y):
			return steps
		for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nx, ny = x + dx, y + dy
			if in_bounds(nx, ny, height, width) and grid[ny][nx] != '#' \
			and (nx, ny) not in seen:
				seen.add((nx, ny))
				queue.append((nx, ny, steps + 1))
	return None # Meaning end isn't reachable

def determine_first_square_to_close_path(height: int, width: int, data: list[tuple[int, int]]) -> tuple[int, int] | None:
	# Logic is to start at end state end and remove obstacle squares until start and end are connected
	data_set = set(data)
	start, end = (0, 0), (height-1, width-1)
	uf = Union_Find()
	open_squares = [(x, y) for x in range(width) for y in range(height) if (x, y) not in data_set]
	open_squares_set = set(open_squares)
	order_of_removal = open_squares + data[::-1]

	for x, y in order_of_removal:
		for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
			nx, ny = x + dx, y + dy
			if in_bounds(nx, ny, height, width) and (nx, ny) in open_squares_set:
				uf.union((x, y), (nx, ny))
		if uf.find(start) == uf.find(end):
			return x, y
		open_squares_set.add((x, y))
	return None # No solution found

def part_1() -> None:
	height, width, data = get_data()
	grid = grid_after_n_turns(height, width, data, 1024)
	answer = find_shortest_route(grid, 0, 0, height-1, width-1)
	print(f"The answer to part 1 is {answer}.")

def part_2() -> None:
	height, width, data = get_data()
	answer_x, answer_y = determine_first_square_to_close_path(height, width, data)
	print(f"The answer to part 2 is {answer_x},{answer_y}.")

if __name__ == "__main__":
	part_1()
	part_2()