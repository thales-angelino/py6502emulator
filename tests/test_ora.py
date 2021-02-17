import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import ora


class TestORA(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_ora_immediate(self):
        expected_cycles = 2
        value = 0xa0
        self.cpu.a = 0x0a
        expected_value = 0xaa
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_IMMEDIATE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ora_absolute(self):
        expected_cycles = 4
        value = 0xa0
        self.cpu.a = 0x0f
        expected_value = 0xaf
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ora_absolutex(self):
        expected_cycles = 4
        value = 0xa0
        expected_value = 0xf0
        self.cpu.a = 0xf0
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_ABSOLUTEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x0300] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ora_absolutey(self):
        expected_cycles = 4
        value = 0xaa
        expected_value = 0xaa
        self.cpu.a = 0x00
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_ABSOLUTEY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x0301] = value
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ora_zeropage(self):
        expected_cycles = 3
        value = 0xa0
        expected_value = 0xa0
        self.cpu.a = 0x00
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ora_zeropagex(self):
        expected_cycles = 4
        value = 0x0a
        expected_value = 0xfa
        self.cpu.a = 0xf0
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_ZEROPAGEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ora_indirectx(self):
        expected_cycles = 6
        value = 0xa0
        expected_value = 0xaa
        self.cpu.a = 0x0a
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_INDIRECTX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = 0x74
        self.memory.memory[0x0090] = 0x20
        self.memory.memory[0x2074] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_ora_indirecty(self):
        expected_cycles = 5       
        value = 0xa0
        expected_value = 0xa0
        self.cpu.a = 0x00
        self.memory.memory[emulator.START_ADDRESS] = ora.ORA_INDIRECTY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x0080] = 0x74
        self.memory.memory[0x0081] = 0x20
        self.memory.memory[0x2075] = value
        self.cpu.y = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()