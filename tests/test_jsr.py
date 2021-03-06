import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import jsr


class TestJSRWithRTS(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_jsr_with_rts(self):
        self.memory.memory[emulator.START_ADDRESS] = jsr.JSR_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x40
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x30
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, 0x3040, "Program counter should be: 0x3040")
        self.assertEqual(self.cpu.cycles, 6, "CPU cycles should be 6")
        self.assertEqual(self.memory.memory[0x1ff], 0x06, "Stack Address[0x1ff] should contain 0x06")
        self.assertEqual(self.memory.memory[0x1fe], 0x02, "Stack Address[0x1fe] should contain 0x02")
        self.assertEqual(self.cpu.stack_pointer, 0xfd, "Stack pointer should be: 0xfd")


if __name__ == '__main__':
    unittest.main()