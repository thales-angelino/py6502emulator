import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import tax


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_tax(self):
        expected_cycles = 2
        self.cpu.a = 0xaf
        self.memory.memory[emulator.START_ADDRESS] = tax.TAX_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.x, self.cpu.a, "Register X should contain: %s" % hex(self.cpu.a))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()