from hashlib import md5

def get_data() -> str:
	with open("input.txt") as f:
		return f.read().strip()

def get_solution(n_zeros: int) -> int:
	prefix = get_data()
	found = False
	postfix = 0
	while not found:
		attempt = prefix + str(postfix)
		digest = md5(attempt.encode()).hexdigest()
		if digest[:n_zeros] == '0' * n_zeros:
			found = True
		else:
			postfix += 1
	return postfix

def part_1() -> None:
	print(f"The answer to part 1 is {get_solution(5)}.")

def part_2() -> None:
	print(f"The answer to part 2 is {get_solution(6)}.")

if __name__ == '__main__':
	part_1()
	part_2()
