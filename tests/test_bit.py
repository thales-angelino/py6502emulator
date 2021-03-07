import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import bit


class TestBIT(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_bit_absolute(self):
        expected_cycles = 4
        value = 0xaa
        self.cpu.a = 0xff
        self.cpu.processor_status['overflow'] = 1
        self.memory.memory[emulator.START_ADDRESS] = bit.BIT_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.processor_status['overflow'], 0, "Overflow should contain 0")
        self.assertEqual(self.cpu.processor_status['negative'], 1, "Negative should contain 1")
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_bit_zeropage(self):
        expected_cycles = 3
        value = 0xaa
        self.cpu.a = 0xff
        self.cpu.processor_status['overflow'] = 1
        self.memory.memory[emulator.START_ADDRESS] = bit.BIT_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.processor_status['overflow'], 0, "Overflow should contain 0")
        self.assertEqual(self.cpu.processor_status['negative'], 1, "Negative should contain 1")
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()