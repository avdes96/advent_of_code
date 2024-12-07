def get_data() -> tuple[dict[str, str], list[str]]:
	with open("input.txt") as f:
		text = f.readlines()
	rules, updates = [], []
	for line in text:
		line = line.strip()
		if line:
			if '|' in line:
				rules.append(line)
			else:
				updates.append(line)
	rule_set = construct_rule_set(rules)
	return rule_set, updates

def construct_rule_set(rules: list[str]) -> dict[str, list[str]]:
	rule_set = {}
	for rule in rules:
		before, after = rule.split("|")
		if before not in rule_set:
			rule_set[before] = []
		if after not in rule_set:
			rule_set[after] = []
		rule_set[after].append(before)
	return rule_set

def pages_in_correct_order(update: list[str], rule_set: dict[str, list[str]]) -> bool:
	for i in range(len(update) - 1):
		for j in range(i, len(update)):
			if update[j] in rule_set[update[i]]:
				return False
	return True

def sort_list(lst: list[str], rule_set: dict[str, list[str]]) -> list[str]:
	if len(lst) == 1:
		return lst
	m = len(lst) // 2
	left, right = sort_list(lst[:m], rule_set), sort_list(lst[m:], rule_set)
	return merge(left, right, rule_set)

def merge(left: list[str], right: list[str], rule_set: dict[str, list[str]]) -> list[str]:
	lst = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] in rule_set[right[j]]:
			lst.append(left[i])
			i += 1
		else:
			lst.append(right[j])
			j += 1
	if i < len(left):
		lst += left[i:]
	else:
		lst += right[j:]
	return lst

def answers() -> None:
	rule_set, updates, = get_data()
	answer_part_1, answer_part_2 = 0, 0
	for update in updates:
		update = update.split(",")
		if pages_in_correct_order(update, rule_set):
			answer_part_1 += int(update[len(update) // 2])
		else:
			sorted_update = sort_list(update, rule_set)
			answer_part_2 += int(sorted_update[len(sorted_update) // 2])
	
	print(f"The answer to part 1 is {answer_part_1}.")
	print(f"The answer to part 2 is {answer_part_2}.")

if __name__ == "__main__":
	answers()