from collections import deque

def get_data(expanded_grid: bool = False) -> tuple[list[list[str]], str]:
	is_grid = True
	grid = []
	dirs = ""
	with open('input.txt') as f:
		for line in f.readlines():
			line = line.strip()
			if line == '':
				is_grid = False
			else:
				if is_grid:
					if expanded_grid:
						line = expand_line(line)
					grid.append(list(line))
				else:
					dirs += line
	return grid, dirs


def expand_line(line: str) -> str:
	expanded_line = ""
	for char in line:
		match char:
			case '#': expanded_line += '##'
			case '.': expanded_line += '..'
			case 'O': expanded_line += '[]'
			case '@': expanded_line += '@.'
			case _: raise ValueError(f'{char} not supported.')
	return expanded_line


def locate_start(grid: list[list[str]]) -> tuple[int, int]:
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == '@':
				return (x, y)
	raise KeyError("Start point not in grid.")


def get_dx_dy(direction: str) -> tuple[int, int]:
	match direction:
		case '^': return(0, -1)
		case '>': return(1, 0)
		case 'v': return(0, 1)
		case '<': return(-1, 0)
	raise ValueError(f"{direction} is not a valid direction.")


def update_grid(grid: list[list[str]], direction: str, start_x: int, start_y: int) -> tuple[int, int]:
	dx, dy = get_dx_dy(direction)
	updates = {}
	queue = deque([(start_x, start_y)])
	while queue:
		x, y = queue.popleft()
		if (x, y) not in updates:
			updates[(x, y)] = '.'
		current_square = grid[y][x]
		x += dx
		y += dy
		updates[(x, y)] = current_square
		if grid[y][x] != '.':
			if grid[y][x] == '#':
				return start_x, start_y
			queue.append((x, y))
			if direction in ('^', 'v'):
				if grid[y][x] == '[':
					queue.append((x + 1, y))
				elif grid[y][x] == ']':
					queue.append((x - 1, y))
	
	for x, y in updates:
		grid[y][x] = updates[(x, y)]
	return start_x + dx, start_y + dy


def score_grid(grid: list[list[str]], expanded_grid: bool = False) -> int:
	score = 0
	scoring_char = '[' if expanded_grid else 'O'
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == scoring_char:
				score += 100 * y + x
	return score


def print_grid(grid: list[list[str]]) -> None:
	for row in grid:
		print("".join(row))


def get_solution(expanded_grid: bool = False) -> int:
	grid, directions = get_data(expanded_grid)
	x, y = locate_start(grid)
	for direction in directions:
		x, y = update_grid(grid, direction, x, y)
	return score_grid(grid, expanded_grid)
	

if __name__ == '__main__':
	print(f"The answer to part 1 is {get_solution(expanded_grid=False)}.")
	print(f"The answer to part 2 is {get_solution(expanded_grid=True)}.")