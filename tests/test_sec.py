import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import sec


class TestSEC(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_sec(self):
        expected_cycles = 2
        value = 1
        self.memory.memory[emulator.START_ADDRESS] = sec.SEC_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.processor_status['carry'], value, "Carry should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()