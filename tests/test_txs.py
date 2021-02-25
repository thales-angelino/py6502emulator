import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import txs


class TestTXS(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_txs(self):
        expected_value = 0x00
        expected_cycles = 2
        self.memory.memory[emulator.START_ADDRESS] = txs.TXS_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.stack_pointer, expected_value, "Stack pointer should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()