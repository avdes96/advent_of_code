from dataclasses import dataclass, fields
from math import prod
from re import search
from typing import Generator

@dataclass(frozen=True)
class Ingredient:
	capacity: int
	durability: int
	flavour: int
	texture: int
	calories: int

class Cookie:
	def __init__(self, ingredients: list[tuple[Ingredient, int]] = []) -> None:
		self.ingredients = {}
		for ingredient, amt in ingredients:
			self.add_ingredient(ingredient, amt)

	def add_ingredient(self, ingredient: Ingredient, amt: int) -> None:
		self.ingredients[ingredient] = amt

	@property
	def calories(self) -> int:
		return sum(ingredient.calories * amt for ingredient, amt in self.ingredients.items())

	@property
	def score(self, fields_to_exclude: set[str] = {"calories"}) -> int:
		score_per_attribute = {}
		for ingredient, amt in self.ingredients.items():
			for attr in fields(ingredient):
				attr = attr.name
				if attr not in fields_to_exclude:	
					score_per_attribute[attr] = score_per_attribute.get(attr, 0) + amt * getattr(ingredient, attr)
		return prod(max(value, 0) for value in score_per_attribute.values())

def get_data() -> list[Ingredient]:
	ingredients = []
	pattern = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
	with open("input.txt") as f:
		for line in f:
			mtch = search(pattern, line)
			_, capacity, durability, flavour, texture, calories = mtch.groups()
			ingredients.append(Ingredient(int(capacity), int(durability), int(flavour), int(texture), int(calories)))
	return ingredients

def all_valid_permutations(n: int, k: int) -> Generator[list[int], None, None]:
	if k == 1:
		yield [n]
		return
	for i in range(n, -1, -1):
		for rest in all_valid_permutations(n - i, k - 1):
			yield [i] + rest

def get_solution(ingredients: list[Ingredient], total_amt: int = 100, calories_must_equal: int | None = None) -> int:
	answer = 0
	for amts in all_valid_permutations(total_amt, len(ingredients)):
		cookie = Cookie(list(zip(ingredients, amts)))
		if calories_must_equal is None or cookie.calories == calories_must_equal:
			answer = max(answer, cookie.score)
	return answer
				  
if __name__ == "__main__":
	ingredients = get_data()
	answer_part_1 = get_solution(ingredients)
	print(f"The answer to part 1 is {answer_part_1}.")
	answer_part_2 = get_solution(ingredients, calories_must_equal=500)
	print(f"The answer to part 2 is {answer_part_2}.")