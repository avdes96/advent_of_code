def get_data():
	with open('input.txt') as f:
		data = f.readlines()
	
	left_lst, right_lst = [], []
	for line in data:
		a, b = line.strip().split("   ")
		left_lst.append(int(a))
		right_lst.append(int(b))

	return left_lst, right_lst

def part_1():
	left_lst, right_lst = get_data()
	left_lst.sort()
	right_lst.sort()
	answer = 0
	for i in range(len(left_lst)):
		answer += abs(left_lst[i] - right_lst[i])
	
	print(f"The answer for part 1 is {answer}.")

def part_2():
	left_lst, right_lst = get_data()
	counts = {}
	for r in right_lst:
		counts[r] = counts.get(r, 0) + 1
	answer = 0
	for l in left_lst:
		answer += l * counts.get(l, 0)
	
	print(f"The answer for part 2 is {answer}.")

if __name__ == "__main__":
	part_1()
	part_2()