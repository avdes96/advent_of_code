def get_data() -> str:
	with open('input.txt') as f:
		return f.read().strip()

def update_position(position: list[int, int], direction: str):
	match direction:
		case '>': position[0] += 1
		case '<': position[0] -= 1
		case '^': position[1] -= 1
		case 'v': position[1] += 1
		case _: raise ValueError(f"Direction {direction} not supported.")

def get_solution(num_people: int, start_x: int = 0, start_y: int = 0):
	directions = get_data()
	positions = [[start_x, start_y] for _ in range(num_people)]
	seen = set()
	seen.add((start_x, start_y))
	for idx, direction in enumerate(directions):
		person_idx = idx % num_people
		update_position(positions[person_idx], direction)
		seen.add(tuple(positions[person_idx]))
	return len(seen)

def part_1() -> None:
	print(f"The answer to part 1 is {get_solution(1)}.")

def part_2() -> None:
	print(f"The answer to part 2 is {get_solution(2)}.")

if __name__ == '__main__':
	part_1()
	part_2()
