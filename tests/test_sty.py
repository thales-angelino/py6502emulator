import unittest
import emulator_6502 as emulator
from instructions import sty


class TestSTY(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_sty_absolute(self):
        expected_cycles = 4
        value = 0xf0
        self.cpu.y = value
        self.memory.memory[emulator.START_ADDRESS] = sty.STY_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x02ff], value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sty_zeropage(self):
        expected_cycles = 3
        value = 0xf0
        self.cpu.y = value
        self.memory.memory[emulator.START_ADDRESS] = sty.STY_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x00ff], value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sty_zeropagex(self):
        expected_cycles = 4
        value = 0xf0
        self.cpu.y = value
        self.memory.memory[emulator.START_ADDRESS] = sty.STY_ZEROPAGEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x008f], value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()