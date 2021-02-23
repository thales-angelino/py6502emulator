import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import sei


class TestSEI(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_sei(self):
        expected_cycles = 2
        value = 1
        self.memory.memory[emulator.START_ADDRESS] = sei.SEI_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.processor_status['interrupt_disable'], value, "interrupt_disable should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()