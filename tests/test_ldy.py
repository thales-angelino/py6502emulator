import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import ldy


class TestLDY(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_ldy_immediate(self):
        expected_cycles = 2
        value = 0xfa
        self.memory.memory[emulator.START_ADDRESS] = ldy.LDY_IMMEDIATE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.y, value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ldy_absolute(self):
        expected_cycles = 4
        value = 0x32
        self.memory.memory[emulator.START_ADDRESS] = ldy.LDY_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.y, value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ldy_absolutex(self):
        expected_cycles = 4
        value = 0x41
        self.memory.memory[emulator.START_ADDRESS] = ldy.LDY_ABSOLUTEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x0300] = 0x41
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.y, value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ldy_zeropage(self):
        expected_cycles = 3
        value = 0x77
        self.memory.memory[emulator.START_ADDRESS] = ldy.LDY_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.y, value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ldy_zeropagex(self):
        expected_cycles = 4
        value = 0x67
        self.memory.memory[emulator.START_ADDRESS] = ldy.LDY_ZEROPAGEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.y, value, "Register Y should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

if __name__ == '__main__':
    unittest.main()