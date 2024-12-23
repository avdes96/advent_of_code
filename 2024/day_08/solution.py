def get_data() -> list[str]:
	with open("input.txt") as f:
		data = f.readlines()
	data = [line.strip() for line in data]
	return data

def get_antennas(grid: list[str]) -> list[tuple[int, int]]:
	antennas = {}
	for y in range(len(grid)):
		for x in range(len(grid)):
			if grid[y][x] != ".":
				if grid[y][x] not in antennas:
					antennas[grid[y][x]] = []
				antennas[grid[y][x]].append((x, y))
	return antennas

def get_all_combos(antennas: dict[str, list[tuple[int, int]]]) -> set[tuple[tuple[int, int], tuple[int, int]]]:
	combos = set()
	for locs in antennas.values():
		for i in range(len(locs) - 1):
			for j in range(i + 1, len(locs)):
				combos.add((locs[i], locs[j]))
	return combos

def in_bounds(grid: list[str], x: int, y: int) -> bool:
	return x >= 0 and y >= 0 and x < len(grid[0]) and y < len(grid)

def calc_antinodes(grid: list[str], antennas: dict[str, list[tuple[int, int]]], dist: int = 2, resonance: bool = False) -> set[tuple[int, int]]:
	combos = get_all_combos(antennas)
	antinodes = set()
	for antenna_A, antenna_B in combos:
		dx = antenna_A[0] - antenna_B[0]
		dy = antenna_A[1] - antenna_B[1]

		if resonance:
			for scaler in (-1, 1):
				antinode = (antenna_A[0], antenna_A[1])
				while in_bounds(grid, antinode[0], antinode[1]):
					antinodes.add(antinode)
					antinode = (antinode[0] + scaler * dx, antinode[1] + scaler * dy)
		else:
			antinode_A = (antenna_A[0] + -1 * dist * dx, antenna_A[1] + -1 * dist * dy)
			antinode_B = (antenna_B[0] + dist * dx, antenna_B[1] + dist * dy)
			for antinode in (antinode_A, antinode_B):
				if in_bounds(grid, antinode[0], antinode[1]):
					antinodes.add(antinode)
	return antinodes


def answers() -> None:
	grid = get_data()
	antennas = get_antennas(grid)
	
	antinodes = calc_antinodes(grid, antennas)
	print(f'The answer to part 1 is {len(antinodes)}.')
	
	antinodes = calc_antinodes(grid, antennas, resonance=True)
	print(f'The answer to part 2 is {len(antinodes)}.')	

if __name__ == "__main__":
	answers()