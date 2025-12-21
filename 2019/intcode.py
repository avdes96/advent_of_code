class IntCode_Computer():
    def __init__(self, program: list[int]) -> None:
        self.program = program
        self.reset()

    def reset(self) -> None:
        self.memory = [i for i in self.program]
        self._ptr = 0

    def run(self) -> None:
        while True:
            opcode = self.memory[self._ptr]
            self._ptr += 1
            match opcode:
                case 1:
                    self._add()
                case 2:
                    self._mul()
                case 99:
                    return

    def _add(self) -> None:
        addr_A = self.memory[self._ptr]
        addr_B = self.memory[self._ptr + 1]
        addr_out = self.memory[self._ptr + 2]

        val_A = self.memory[addr_A]
        val_B = self.memory[addr_B]
        val_out = val_A + val_B
        self.memory[addr_out] = val_out

        self._ptr += 3

    def _mul(self) -> None:
        addr_A = self.memory[self._ptr]
        addr_B = self.memory[self._ptr + 1]
        addr_out = self.memory[self._ptr + 2]

        val_A = self.memory[addr_A]
        val_B = self.memory[addr_B]
        val_out = val_A * val_B
        self.memory[addr_out] = val_out

        self._ptr += 3

    def overwrite_memory(self, pos: int, val: int) -> None:
        self.memory[pos] = val

    def get_value_at_position(self, pos: int) -> int:
        return self.memory[pos]
