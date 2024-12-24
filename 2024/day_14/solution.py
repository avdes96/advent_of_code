import re
import statistics


class Grid:
	def __init__(self, height: int, width: int) -> None:
		self.height = height
		self.width = width
		self.robots = []
	
	def add_robot(self, x: int, y: int, dx: int, dy: int) -> None:
		self.robots.append(Robot(x, y, dx, dy, self))

	def update_n_seconds(self, seconds: int) -> None:
		for robot in self.robots:
			robot.position_after_n_seconds(seconds)
	
	def safety_factor(self) -> int:
		quadrants = {}
		for robot in self.robots:
			q = robot.quadrant()
			if q > 0:
				quadrants[q] = quadrants.get(q, 0) + 1
		answer = 1
		for v in quadrants.values():
			answer *= v
		return answer
	
	def which_quadrant(self, x: int, y: int) -> int:
		width_middle = self.width // 2
		height_middle = self.height // 2

		if x < width_middle and y < height_middle:
			return 1
		elif x > width_middle and y < height_middle:
			return 2
		elif x < width_middle and y > height_middle:
			return 3
		elif x > width_middle and y > height_middle:
			return 4
		return 0
	
	def get_var(self) -> float:
		return (statistics.variance([robot.position()[0] for robot in self.robots]) \
			+ statistics.variance([robot.position()[1] for robot in self.robots])) / 2
		
	
	def draw(self) -> None:
		grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
		for robot in self.robots:
			x, y = robot.position()
			grid[y][x] = '#'
		
		for row in grid:
			print("".join(row))

class Robot:
	def __init__(self, x: int, y: int, dx: int, dy: int, grid: Grid) -> None:
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.grid = grid
	
	def position_after_n_seconds(self, n: int) -> None:
		self.x = (self.x + self.dx * n) % self.grid.width
		self.y = (self.y + self.dy * n) % self.grid.height

	def position(self) -> tuple[int, int]:
		return (self.x, self.y)

	def quadrant(self) -> int:
		return self.grid.which_quadrant(self.x, self.y)


def get_data(file_name: str) -> Grid:
	if "test" in file_name:
		height, width = 7, 11
	else:
		height, width = 103, 101
	grid = Grid(height, width)

	with open(file_name) as file:
		for line in file:
			numbers = re.findall(r'-?\d+', line.strip())
			x, y, dx, dy = (int(c) for c in numbers)
			grid.add_robot(x, y, dx, dy)
	return grid

def display_picture_at_time_t(t: int) -> None:
	grid = get_data("input.txt")
	grid.update_n_seconds(t)
	grid.draw()

def part_1() -> None:
	grid = get_data("input.txt")
	grid.update_n_seconds(100)	
	print(f"The answer to part 1 is {grid.safety_factor()}.")

def part_2() -> None:
	variances = []
	grid = get_data("input.txt")
	seconds = 10000
	# Logic is picture will occur when robots are closest together.
	# i.e, varience in x and y is minimised.  
	for i in range(1, seconds + 1):
		grid.update_n_seconds(1)
		var = grid.get_var()
		variances.append((i, var))
	answer = min(variances, key = lambda x:(x[1], x[0]))[0]
	print(f"The answer to part 2 is {answer}.")
	display_picture_at_time_t(answer)

if __name__ == "__main__":
	part_1()
	part_2()