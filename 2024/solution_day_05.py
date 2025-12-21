import argparse
from collections import defaultdict


def get_data(filename: str) -> tuple[defaultdict[str, list[str]], list[str]]:
    with open(filename) as f:
        rules_str, updates_str = f.read().split("\n\n")
    rules = rules_str.split("\n")
    rule_set = construct_rule_set(rules)
    updates = updates_str.split("\n")
    return rule_set, updates


def construct_rule_set(rules: list[str]) -> defaultdict[str, list[str]]:
    rule_set = defaultdict(list)
    for rule in rules:
        before, after = rule.split("|")
        rule_set[after].append(before)
    return rule_set


def pages_in_correct_order(update: list[str], rule_set: defaultdict[str, list[str]]) -> bool:
    for i in range(len(update) - 1):
        for j in range(i, len(update)):
            if update[j] in rule_set[update[i]]:
                return False
    return True


def sort_list(lst: list[str], rule_set: defaultdict[str, list[str]]) -> list[str]:
    if len(lst) == 1:
        return lst
    m = len(lst) // 2
    left, right = sort_list(lst[:m], rule_set), sort_list(lst[m:], rule_set)
    return merge(left, right, rule_set)


def merge(left: list[str], right: list[str], rule_set: defaultdict[str, list[str]]) -> list[str]:
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2024 - Day 5")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    rule_set, updates, = get_data(filename)
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
    main()
