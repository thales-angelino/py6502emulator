import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import _and


class TestAND(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_and_immediate(self):
        expected_cycles = 2
        value = 0xaa
        self.cpu.a = 0xff
        expected_value = 0xaa
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_IMMEDIATE_OPCODE
        self.memory.memory[0xfffd] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_and_absolute(self):
        expected_cycles = 4
        value = 0xaa
        self.cpu.a = 0xff
        expected_value = 0xaa
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_ABSOLUTE_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_and_absolutex(self):
        expected_cycles = 4
        value = 0xaa
        expected_value = 0xaa
        self.cpu.a = 0xff
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_ABSOLUTEX_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x0300] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_and_absolutey(self):
        expected_cycles = 4
        value = 0xaa
        expected_value = 0xaa
        self.cpu.a = 0xff
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_ABSOLUTEY_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x0301] = value
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_and_zeropage(self):
        expected_cycles = 3
        value = 0xaa
        expected_value = 0xaa
        self.cpu.a = 0xff
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_ZEROPAGE_OPCODE
        self.memory.memory[0xfffd] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_and_zeropagex(self):
        expected_cycles = 4
        value = 0xaa
        expected_value = 0xaa
        self.cpu.a = 0xff
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_ZEROPAGEX_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_and_indirectx(self):
        expected_cycles = 6
        value = 0xaa
        expected_value = 0x0a
        self.cpu.a = 0x0f
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_INDIRECTX_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x008f] = 0x74
        self.memory.memory[0x0090] = 0x20
        self.memory.memory[0x2074] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_and_indirecty(self):
        expected_cycles = 5       
        value = 0xaa
        expected_value = 0xa0
        self.cpu.a = 0xf0
        self.memory.memory[emulator.START_ADDRESS] = _and.AND_INDIRECTY_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x0080] = 0x74
        self.memory.memory[0x0081] = 0x20
        self.memory.memory[0x2075] = value
        self.cpu.y = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()