from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import Generator

def get_data() -> list[str]:
	with open("input.txt") as f:
		return f.read().splitlines()

def get_next_moves(x: int, y: int, direction: str) -> Generator[tuple[int, int, str, int], None, None]:
	# Yields (new_x, new_y, new_direction, cost_of_move)
	dx, dy = get_dx_dy(direction)
	move_ahead = (x + dx, y + dy, direction, 1)
	yield move_ahead

	cw_dir = get_next_dir(direction, is_clockwise=True)
	turn_cw = (x, y, cw_dir, 1000)
	yield turn_cw

	acw_dir = get_next_dir(direction, is_clockwise=False)
	turn_acw = (x, y, acw_dir, 1000)
	yield turn_acw

def get_optimal_path(grid: list[str], start_dir: str = "E") -> tuple[int | float, set[tuple[int, int]]]:
	start, end = locate_start(grid), locate_end(grid)
	start_x, start_y = start
	lowest_scores = defaultdict(lambda: float("inf"))
	best_score = float("inf")
	best_paths = defaultdict(set)
	queue = []
	heappush(queue, (0, 0, start_x, start_y, start_dir))
	seen = set()

	while queue:
		_, score, x, y, direction = heappop(queue)
		if score > best_score:
			continue
		for new_x, new_y, new_dir, cost_of_move in get_next_moves(x, y, direction):
			if grid[new_y][new_x] != '#' and (new_x, new_y, new_dir) not in seen:
				new_score = score + cost_of_move
				priority = new_score + manhattan_dist((new_x, new_y), end)
				if new_score <= lowest_scores[(new_x, new_y, new_dir)]:
					lowest_scores[(new_x, new_y, new_dir)] = new_score
					if new_score < lowest_scores[(new_x, new_y, new_dir)]:
						best_paths[(new_x, new_y, new_dir)] = set()
					best_paths[(new_x, new_y, new_dir)].add((x, y, direction))
					if (new_x, new_y) == end:
						best_score = min(best_score, new_score)
						continue
					seen.add((x, y, direction))
					heappush(queue, (priority, new_score, new_x, new_y, new_dir))
	squares_on_route = get_squares_on_shortest_routes(best_paths, end)
	return best_score, squares_on_route

def manhattan_dist(a: tuple[int, int], b: tuple[int, int]) -> int:
	a_x, a_y = a
	b_x, b_y = b
	return abs(a_x - b_x) + abs(a_y - b_y)

def get_squares_on_shortest_routes(best_paths: defaultdict[tuple[int, int, str], set[tuple[int, int, str]]], end: tuple[int, int]) -> set[tuple[int, int]]:
	queue = deque()
	end_x, end_y = end
	for d in ['N', 'E', 'S', 'W']:
		queue.append((end_x, end_y, d))
	seen = set()
	while queue:
		x, y, direction = queue.popleft()
		for prev in best_paths[(x, y, direction)]:
			queue.append(prev)
		seen.add((x, y))
	return seen

def get_next_dir(direction: str, is_clockwise: bool) -> str:
	dirs = ('N', 'E', 'S', 'W')
	idx = dirs.index(direction)
	if is_clockwise:
		return dirs[(idx + 1) % len(dirs)]
	return dirs[(idx - 1) % len(dirs)]

def get_dx_dy(direction: str) -> tuple[int, int]:
	match direction:
		case 'E': return (1, 0)
		case 'W': return (-1, 0)
		case 'S': return (0, 1)
		case 'N': return (0 , -1)
	raise ValueError(f"Direction {direction} not valid.")

def locate_point(grid: list[str], char: str) -> tuple[int, int]:
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == char:
				return x, y
	raise ValueError(f"{char} not in grid.")

def locate_start(grid: list[str]) -> tuple[int, int]:
	return locate_point(grid, 'S')

def locate_end(grid: list[str]) -> tuple[int, int]:
	return locate_point(grid, 'E')

def get_solution() -> None:
	grid = get_data()
	best_score, seats_on_path = get_optimal_path(grid)
	print(f"The answer to part 1 is {best_score}.")
	print(f"The answer to part 2 is {len(seats_on_path)}.")

if __name__ == "__main__":
	get_solution()