import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import txa


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_txa(self):
        expected_cycles = 2
        self.cpu.x = 0xaf
        self.memory.memory[emulator.START_ADDRESS] = txa.TXA_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, self.cpu.x, "Register A should contain: %s" % hex(self.cpu.x))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()