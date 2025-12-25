from argparse import ArgumentParser
from dataclasses import dataclass
import re


@dataclass
class Section:
    start: int
    end: int


def get_data(filename: str) -> list[tuple[Section, Section]]:
    pattern = r"^(\d+)-(\d+),(\d+)-(\d+)$"
    data = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            m = re.match(pattern, line)
            if m is None:
                raise ValueError(f"{line} is not in expected format {pattern}")
            data.append((Section(int(m.group(1)), int(m.group(2))),
                         Section(int(m.group(3)), int(m.group(4)))))
    return data


def sections_fully_overlap(section_A: Section, section_B: Section) -> bool:
    return (section_A.start <= section_B.start and section_A.end >= section_B.end) \
        or (section_B.start <= section_A.start and section_B.end >= section_A.end)


def sections_overlap(section_A: Section, section_B: Section) -> bool:
    earlier_section, later_section = section_A, section_B
    if section_B.start < section_A.start:
        earlier_section, later_section = section_B, section_A
    return earlier_section.start <= later_section.start <= earlier_section.end


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2022 - Day 4")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    data = get_data(filename)
    full_overlaps, any_overlaps = 0, 0
    for section_A, section_B in data:
        if sections_fully_overlap(section_A, section_B):
            full_overlaps += 1
        if sections_overlap(section_A, section_B):
            any_overlaps += 1
    print(f"The answer to part 1 is {full_overlaps}.")
    print(f"The answer to part 2 is {any_overlaps}.")


if __name__ == "__main__":
    main()
