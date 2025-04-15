from __future__ import annotations
from copy import deepcopy
from re import findall, search

class Node:
	def __init__(self) -> None:
		self._text = ""
		self._children = []
	
	def add_child(self, child: Node) -> None:
		self._children.append(child)

	def update_text(self, char: str) -> None:
		self._text += char

	@property
	def text(self) -> str:
		return self._text
	
	@property
	def children(self) -> list[Node]:
		return deepcopy(self._children)

def get_data() -> str:
	with open("input.txt") as f:
		return f.read().strip()

def construct_tree(text: str, idx: int = 0) -> tuple[int, Node]:
	node = Node()
	while idx < len(text):
		char = text[idx]
		if char == "}":
			return idx + 1, node
		elif char == "{":
			idx, child = construct_tree(text, idx + 1)
			node.add_child(child)
		else:
			node.update_text(char)
			idx += 1
	return idx, node

def calculate_sum_valid_digits(node: Node) -> int:
	if search(r'(:"red")', node.text) is not None:
		return 0
	total = sum(map(int, findall(r"(-?\d+)", node.text)))
	for child in node.children:
		total += calculate_sum_valid_digits(child)
	return total

def part_1() -> None:
	data = get_data()
	print(f"The answer to part 1 is {sum(map(int, findall(r"(-?\d+)", data)))}.")
		
def part_2() -> None:
	data = get_data()
	_, tree = construct_tree(data)
	answer = calculate_sum_valid_digits(tree)
	print(f"The answer to part 2 is {answer}.")

if __name__ == "__main__":
	part_1()
	part_2()