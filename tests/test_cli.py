import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import cli


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_cli(self):
        expected_cycles = 2
        value = 0
        self.memory.memory[emulator.START_ADDRESS] = cli.CLI_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.processor_status['interrupt_disable'], value, "Interrupt should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()