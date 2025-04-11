from typing import Generator

def get_data() -> str:
	with open("input.txt") as f:
		return f.read().strip()

def next_password(password: str) -> str:
	if len(password) != 8:
		raise ValueError("Password must be of length 8.")
	new_password = list(password)
	idx = len(password) - 1
	while idx >= 0:
		original_char = new_password[idx]
		if original_char == "z":
			new_char = "a"
		else:
			new_char = chr(ord(original_char) + 1)
		new_password[idx] = new_char
		if original_char != "z":
			return "".join(new_password)
		idx -= 1
	return "".join(new_password)

def password_valid(password: str) -> bool:
	increasing_triple = False
	invalid_chars = set(list("iol"))
	doubles = set()
	for i in range(len(password)):
		if i >= 2:
			if ord(password[i]) == ord(password[i-1]) + 1 == ord(password[i-2]) + 2:
				increasing_triple = True
		if i >= 1:
			if password[i] == password[i-1]:
				doubles.add(password[i])
		if i in invalid_chars:
			return False
	return increasing_triple and len(doubles) >= 2

def valid_passwords(start: str) -> Generator[str, None, None]:
	password = next_password(start)
	while password != start:
		if password_valid(password):
			yield password
		password = next_password(password)

if __name__ == "__main__":
	start = get_data()
	generator = valid_passwords(start)
	print(f"The answer to part 1 is {next(generator)}.")
	print(f"The answer to part 2 is {next(generator)}.")