from argparse import ArgumentParser


def get_data(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().split("\n")


def find_common_item(strs: list[str]) -> str:
    if len(strs) < 2:
        raise ValueError(
            f"Must have at least two strings to find common item; got {len(strs)}"
        )
    common_item = set(list(strs[0]))
    for s in strs[1:]:
        common_item = common_item.intersection(set(list(s)))
    common_item = list(common_item)
    if len(common_item) == 0:
        raise ValueError("No common item.")
    if len(common_item) > 1:
        raise ValueError("More than 1 common item.")
    return common_item[0]


def find_common_item_in_rucksack(rucksack: str) -> str:
    left, right = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    return find_common_item([left, right])


def find_badge_item(members: list[str]) -> str:
    if len(members) != 3:
        raise ValueError(f"Members is of len {len(members)}; should be of len 3.")
    return find_common_item(members)


def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord("a") + 1
    if item.isupper():
        return ord(item) - ord("A") + 27
    raise ValueError(f"Item {item} is not valid.")


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2022 - Day 3")
    parser.add_argument(
        "input_filename", type=str, help="File containing problem input."
    )
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)

    answer_part_1 = 0
    for rucksack in data:
        common_item = find_common_item_in_rucksack(rucksack)
        answer_part_1 += get_priority(common_item)
    print(f"The answer to part 1 is {answer_part_1}.")

    answer_part_2 = 0
    for i in range(0, len(data), 3):
        badge_item = find_badge_item(data[i : i + 3])
        answer_part_2 += get_priority(badge_item)
    print(f"The answer to part 2 is {answer_part_2}.")


if __name__ == "__main__":
    main()
