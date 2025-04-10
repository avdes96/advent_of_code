from __future__ import annotations
from itertools import permutations
from re import search
from typing import Generator

class Person:
	def __init__(self, name: str) -> None:
		self.name = name
		self.lookup = {}
	
	def happiness_next_to(self, other_person: Person) -> int:
		return self.lookup[other_person]
	
	def add_person(self, other_person: Person, happiness: int) -> None:
		self.lookup[other_person] = happiness

	
def get_data() -> list[Person]:
	people = {}
	pattern = r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."
	with open("input.txt") as f:
		for line in f:
			m = search(pattern, line)
			name_A, gain_or_lose, amt, name_B = m.groups()
			factor = 1 if gain_or_lose == "gain" else -1
			if name_A not in people:
				people[name_A] = Person(name_A)
			if name_B not in people:
				people[name_B] = Person(name_B)
			people[name_A].add_person(people[name_B], factor * int(amt))
	return list(people.values())


def get_best_score(all_people: list[Person]) -> int:
	def get_permutations(all_people: list[Person]) -> Generator[list[Person], None, None]:
		# As table is circular, we can keep person at idx 0 fixed
		for table in permutations(all_people[1:]):
			yield [all_people[0]] + list(table)

	def get_score(table: list[Person]) -> int:
		n = len(table)
		total = 0
		for i in range(n):
			l, r = (i - 1) % n, (i + 1) % n
			total += table[i].happiness_next_to(table[l]) + table[i].happiness_next_to(table[r])
		return total
	return max(get_score(table) for table in get_permutations(all_people))


def part_1() -> None:
	people = get_data()
	print(f"The answer to part 1 is {get_best_score(people)}.")


def part_2() -> None:
	people = get_data()
	me = Person("Me")
	for person in people:
		me.add_person(person, 0)
		person.add_person(me, 0)
	people.append(me)
	print(f"The answer to part 2 is {get_best_score(people)}.")
	

if __name__ == "__main__":
	part_1()
	part_2()