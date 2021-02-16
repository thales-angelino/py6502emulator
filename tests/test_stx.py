import unittest
import emulator_6502 as emulator
from instructions import stx


class TestSTX(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_stx_absolute(self):
        expected_cycles = 4
        value = 0xf0
        self.cpu.x = value
        self.memory.memory[emulator.START_ADDRESS] = stx.STX_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x02ff], value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_stx_zeropage(self):
        expected_cycles = 3
        value = 0xf0
        self.cpu.x = value
        self.memory.memory[emulator.START_ADDRESS] = stx.STX_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x00ff], value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_stx_zeropagey(self):
        expected_cycles = 4
        value = 0xf0
        self.cpu.x = value
        self.memory.memory[emulator.START_ADDRESS] = stx.STX_ZEROPAGEY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.cpu.y = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x008f], value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()