import argparse
from re import match


def get_data(filename: str) -> list[tuple[str, int, str]]:
    with open(filename, "r") as f:
        lines = f.read().split("\n")
    pattern = r"^([a-z-]+)-(\d+)\[(\w+)\]$"
    data = []
    for line in lines:
        line = line.strip()
        m = match(pattern, line)
        if m is None:
            raise ValueError(f"{line} not in correct format: {pattern}")
        name, sector_id, checksum = m.group(1), int(m.group(2)), m.group(3)
        data.append((name, sector_id, checksum))
    return data


def get_checksum(name: str, checksum_len: int = 5) -> str:
    counts = [{'count': 0, 'id': chr(i + ord('a'))} for i in range(26)]
    for char in name:
        if char == '-':
            continue
        counts[ord(char) - ord('a')]['count'] += 1
    counts.sort(key=lambda x: (x['count'], -1 * ord(x['id'])), reverse=True)
    relevant_values = [x['id'] for x in counts[:checksum_len]]
    return "".join(relevant_values)


def decode_name(name: str, sector_id: int) -> str:
    new_name = ""
    for char in name:
        if char == '-':
            new_name += " "
        else:
            new_name += chr(ord('a') + ((ord(char) - ord('a') + sector_id) % 26))
    return new_name


def main() -> None:
    parser = argparse.ArgumentParser(description="Advent of Code 2016 - Day 4")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    answer_part_1 = 0
    answer_part_2 = None
    for name, sector_id, checksum in data:
        if get_checksum(name) == checksum:
            answer_part_1 += sector_id
        decoded_name = decode_name(name, sector_id)
        if 'northpole' in decoded_name:
            if answer_part_2 is not None:
                raise ValueError("Multiple occurances of northpole in data.")
            answer_part_2 = sector_id
    print(f"The answer to part 1 is {answer_part_1}.")
    print(f"The answer to part 2 is {answer_part_2}.")


if __name__ == "__main__":
    main()
