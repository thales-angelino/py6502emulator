import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import ldx


class TestLDX(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_ldx_immediate(self):
        expected_cycles = 2
        value = 0xfa
        self.memory.memory[emulator.START_ADDRESS] = ldx.LDX_IMMEDIATE_OPCODE
        self.memory.memory[0xfffd] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.x, value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ldx_absolute(self):
        expected_cycles = 4
        value = 0x32
        self.memory.memory[emulator.START_ADDRESS] = ldx.LDX_ABSOLUTE_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.x, value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ldx_absolutey(self):
        expected_cycles = 4
        value = 0x38
        self.memory.memory[emulator.START_ADDRESS] = ldx.LDX_ABSOLUTEY_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x0301] = value
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.x, value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ldx_zeropage(self):
        expected_cycles = 3
        value = 0x77
        self.memory.memory[emulator.START_ADDRESS] = ldx.LDX_ZEROPAGE_OPCODE
        self.memory.memory[0xfffd] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.x, value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_zeropagey(self):
        expected_cycles = 4
        value = 0x67
        self.memory.memory[emulator.START_ADDRESS] = ldx.LDX_ZEROPAGEY_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.y = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.x, value, "Register X should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

if __name__ == '__main__':
    unittest.main()