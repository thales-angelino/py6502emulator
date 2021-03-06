import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import rts


class TestRTS(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_jsr_with_rts(self):
        self.memory.memory[0x1fe] = 0x3f
        self.memory.memory[0x1ff] = 0x30
        self.cpu.stack_pointer = 0xfd
        self.memory.memory[emulator.START_ADDRESS] = rts.RTS_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, 0x3040, "Program counter should be: 0x3040")
        self.assertEqual(self.cpu.cycles, 6, "CPU cycles should be 6")
        self.assertEqual(self.memory.memory[0x1ff], 0x00, "Stack Address[0x1ff] should contain 0x00")
        self.assertEqual(self.memory.memory[0x1fe], 0x00, "Stack Address[0x1fe] should contain 0x00")
        self.assertEqual(self.cpu.stack_pointer, 0xff, "Stack pointer should be: 0xff")


if __name__ == '__main__':
    unittest.main()