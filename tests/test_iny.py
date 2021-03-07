import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import iny


class TestINY(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_iny(self):
        self.memory.memory[emulator.START_ADDRESS] = iny.INY_IMPLIED_OPCODE
        self.cpu.y = 0xaf
        self.cpu.execute(1)
        self.assertEqual(self.cpu.y, 0xb0, "Y register should be: 0xb0")
        self.assertEqual(self.cpu.cycles, 2, "CPU cycles should be 2")


if __name__ == '__main__':
    unittest.main()