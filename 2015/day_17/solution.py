def get_data() -> tuple[int, list[int]]:
	file_name = "input.txt"
	target = 25 if "test" in file_name else 150
	with open(file_name) as f:
		containers = list(map(int, f.read().splitlines()))
	return target, containers

def get_solution() -> None:
	target, containers = get_data()
	containers.sort()
	combinations = [[]]
	for size in containers:
		combinations += [[size] + combo for combo in combinations if size + sum(combo) <= target]
	num_valid_containers = 0
	min_containers = float('inf')
	counts = {}
	for combo in combinations:
		if sum(combo) == target:
			num_valid_containers += 1
			num_containers = len(combo)
			counts[num_containers] = counts.get(num_containers, 0) + 1
			min_containers = min(min_containers, num_containers)
	print(f"The answer to part 1 is {num_valid_containers}.")
	print(f"The answer to part 2 is {counts[min_containers]}.")

if __name__ == "__main__":
	get_solution()
