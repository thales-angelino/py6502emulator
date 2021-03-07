import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import inx


class TestINX(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_inx(self):
        self.memory.memory[emulator.START_ADDRESS] = inx.INX_IMPLIED_OPCODE
        self.cpu.x = 0xaf
        self.cpu.execute(1)
        self.assertEqual(self.cpu.x, 0xb0, "X register should be: 0xb0")
        self.assertEqual(self.cpu.cycles, 2, "CPU cycles should be 2")


if __name__ == '__main__':
    unittest.main()