from collections import defaultdict

def get_data() -> defaultdict[str, set[str]]:
	with open('input.txt') as f:
		graph = defaultdict(set)
		for line in f:
			node_A, node_B = line.strip().split("-")
			graph[node_A].add(node_B)
			graph[node_B].add(node_A)
		return graph

def find_closed_loops_of_len_n(graph: defaultdict[str, set[str]], n: int = 3) -> set[str]:
	def find_closed_loops_of_len_n_helper(graph: defaultdict[str, set[str]], current: str, start: str, \
									   depth: int, n: int, path: set[str], loops: set[str]) -> None:
		path.add(current)
		if depth == n:
			if start in graph[current]:
				loops.add(",".join(sorted(list(path))))
		else:
			for nbr in graph[current]:
				if nbr not in path:
					find_closed_loops_of_len_n_helper(graph, nbr, start, depth + 1, n, path, loops)
		path.remove(current)
		return
	
	loops = set()
	for node in graph:
		path = set()
		find_closed_loops_of_len_n_helper(graph, node, node, 1, n, path, loops)
	return loops

def bron_kerbosch(graph: defaultdict[str, set]) -> defaultdict[int, list[set]]:
	# Algorithm explained in: https://www.youtube.com/watch?v=j_uQChgo72I&t=990s
	def bron_kerbosch_recursive(r: set, p: set, x: set, graph: defaultdict[str, set],\
							 cliques: defaultdict[int, list[set]]) -> None:
		if not p and not x:
			cliques[len(r)].append(r)
			return
		pivot = tuple(p.union(x))[0]
		pivot_nbrs = graph[pivot]
		for nbr in p.difference(pivot_nbrs):
			bron_kerbosch_recursive(r.union({nbr}), p.intersection(graph[nbr]), x.intersection(graph[nbr]), graph, cliques)
			p = p.difference({nbr})
			x = x.union({nbr})

	r = set()
	p = set(graph.keys())
	x = set()
	cliques = defaultdict(list)
	bron_kerbosch_recursive(r, p, x, graph, cliques)
	return cliques

def part_1() -> int:
	graph = get_data()
	loops =	find_closed_loops_of_len_n(graph)
	nodes_that_start_with_t = {node for node in graph if node[0] == "t"}
	answer = 0
	for loop in loops:
		nodes_in_loop = set(loop.split(","))
		if nodes_in_loop.intersection(nodes_that_start_with_t):
			answer += 1
	print(f"The answer to part 1 is {answer}.")
				
def part_2() -> None:
	graph = get_data()
	cliques = bron_kerbosch(graph)
	assert len(cliques[max(cliques)]) == 1, "There should be only one maximum sized clique."
	answer = ",".join(sorted(list(cliques[max(cliques)][0])))
	print(f"The answer to part 2 is {answer}.")
	
if __name__ == '__main__':
	part_1()
	part_2()