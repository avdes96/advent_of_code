class Space:
	def __init__(self, start_idx: int, size: int):
		self._start_idx = start_idx
		self._size = size

	def update_after_block_insertion(self, block_size: int) -> None:
		self._start_idx += block_size
		self._size -= block_size
	
	@property
	def start_idx(self):
		return self._start_idx
	
	@property
	def size(self):
		return self._size

def get_data() -> str:
	with open('input.txt') as f:
		return f.read().strip()

def make_block_list(data: str) -> tuple[list[int], list[Space]]:
	file_id = 0
	block_list, space_map = [], []
	total_blocks = 0
	for i, char in enumerate(data):
		size = int(char)
		if i % 2 == 0:
			to_add = [file_id]
			file_id += 1
		else:
			space_map.append(Space(total_blocks, size))
			to_add = [-1]
		block_list += to_add * size
		total_blocks += size
	return block_list, space_map

def calc_checksum(block_list: list[int]) -> int:
	answer = 0
	for i, val in enumerate(block_list):
		if val != -1:
			answer += i * val
	return answer


def part_1() -> None:
	data = get_data()
	block_list, _ = make_block_list(data)
	l, r = 0, len(block_list) - 1
	while l < r:
		if block_list[l] != -1:
			l += 1
		else:
			block_list[l], block_list[r] = block_list[r], block_list[l]
			r -= 1
	answer = calc_checksum(block_list)
	print(f"The answer to part 1 is {answer}.")

def part_2() -> None:
	data = get_data()
	block_list, space_map = make_block_list(data)
	r = len(block_list) - 1
	moved_ids = set()
	while r >= 0:
		if block_list[r] != -1 and block_list[r] != moved_ids:
			file_id, block_end = block_list[r], r
			while block_list[r] == file_id:
				r -= 1
			block_start = r + 1
			block_size = block_end - block_start + 1
			for space in space_map:
				if space.start_idx >= block_start:
					break
				if space.size >= block_size:
					block_list = perform_swap(block_list, space, block_start, block_end)
					moved_ids.add(file_id)
					break
					
		else:
			r -= 1
	answer = calc_checksum(block_list)
	print(f"The answer to part 2 is {answer}.")
	
def perform_swap(block_list: list[int], space: Space, block_start: int, block_end: int) -> list[int]:
	space_start_idx, space_size = space.start_idx, space.size
	assert block_list[block_start] == block_list[block_end]
	file_id = block_list[block_start]
	block_size = block_end - block_start + 1
	remaining_space = space_size - block_size
	new_block_list = block_list[:space_start_idx] + [file_id] * block_size + [-1] * remaining_space + block_list[space_start_idx + max(block_size, space_size):]
	assert len(block_list) == len(new_block_list)
	for i in range(block_start, block_end + 1):
		new_block_list[i] = -1
	space.update_after_block_insertion(block_size)
	return new_block_list

if __name__ == "__main__":
	part_1()
	part_2()