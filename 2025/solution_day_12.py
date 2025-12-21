from argparse import ArgumentParser
from dataclasses import dataclass
from re import match


@dataclass(frozen=True)
class Present:
    ID: int
    shape: tuple[str, ...]


@dataclass(frozen=True)
class Region:
    height: int
    width: int
    required_presents: tuple[int, ...]


def get_data(filename: str) -> tuple[list[Present], list[Region]]:
    with open(filename, "r") as f:
        data = f.read().split("\n\n")
    all_present_strs, all_regions_strs = data[:-1], data[-1].split("\n")
    presents = [parse_present_str(present_str) for present_str in all_present_strs]
    regions = [parse_region_str(region_str) for region_str in all_regions_strs]
    return presents, regions


def parse_present_str(present_str: str) -> Present:
    rows = present_str.split("\n")
    m = match(r"(\d+):", rows[0])
    if m is None:
        raise ValueError(f"present {rows} not in expected form")
    ID = int(m.group(1))
    shape = tuple(rows[1:])
    if len(shape) == 0:
        raise ValueError(f"shape must be of non-zero size")
    return Present(ID, shape)


def parse_region_str(region_str: str) -> Region:
    dimensions, reqs = region_str.split(": ")
    m = match(r"(\d+)x(\d+)", dimensions)
    if m is None:
        raise ValueError(f"dimensions {dimensions} not in expected form")
    height, width = map(int, m.groups())
    reqs = tuple(map(int, reqs.split()))
    return Region(height, width, reqs)


def region_does_not_have_space_for_required_presents(region: Region, presents: list[Present]) -> bool:
    # Check if the number of squares needed for presents exceeds the total squares in region.
    total_area = region.height * region.width
    needed_space = 0
    for i, n_presents in enumerate(region.required_presents):
        present = presents[i]
        needed_space += n_presents * sum(row.count("#") for row in present.shape)
    return needed_space > total_area


def region_comfortably_fits_all_required_presents(region: Region, presents: list[Present]) -> bool:
    # Check if the region can hold all the presents by lining them up in rows (with no overlap).
    # We check against the biggest possible present size.
    max_height = max(len(present.shape) for present in presents)
    max_width = max(max(len(row) for row in present.shape) for present in presents)
    min_presents = (region.height // max_height) * (region.width // max_width)
    num_presents = sum(region.required_presents)
    return num_presents <= min_presents


def main() -> None:
    parser = ArgumentParser(description="Advent of Code 2025 - Day 12")
    parser.add_argument("input_filename", type=str, help="File containing problem input.")
    args = parser.parse_args()
    filename = args.input_filename
    presents, regions = get_data(filename)
    answer = 0
    for region in regions:
        if region_does_not_have_space_for_required_presents(region, presents):
            continue
        if region_comfortably_fits_all_required_presents(region, presents):
            answer += 1
        # The input seems designed such that all regions either comfortably have enough space
        # or not. It is was ambiguous, we could use a backtracking algorithm to confirm.
    print(f"The answer to part 1 is {answer}.")
    print("Part 2 is automatically completed on collection of all other stars.")


if __name__ == "__main__":
    main()
