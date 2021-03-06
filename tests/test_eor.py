import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import eor


class TestEOR(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_eor_immediate(self):
        expected_cycles = 2
        value = 0xa0
        self.cpu.a = 0x0a
        expected_value = 0xaa
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_IMMEDIATE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_eor_absolute(self):
        expected_cycles = 4
        value = 0xa0
        self.cpu.a = 0x00
        expected_value = 0xa0
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_eor_absolutex(self):
        expected_cycles = 4
        value = 0xa0
        expected_value = 0x5f
        self.cpu.a = 0xff
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_ABSOLUTEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x0300] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_eor_absolutey(self):
        expected_cycles = 4
        value = 0xaa
        expected_value = 0x55
        self.cpu.a = 0xff
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_ABSOLUTEY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x0301] = value
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_eor_zeropage(self):
        expected_cycles = 3
        value = 0xa0
        expected_value = 0xa0
        self.cpu.a = 0x00
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_eor_zeropagex(self):
        expected_cycles = 4
        value = 0x0a
        expected_value = 0xf5
        self.cpu.a = 0xff
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_ZEROPAGEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_eor_indirectx(self):
        expected_cycles = 6
        value = 0xa0
        expected_value = 0xaa
        self.cpu.a = 0x0a
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_INDIRECTX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = 0x74
        self.memory.memory[0x0090] = 0x20
        self.memory.memory[0x2074] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_eor_indirecty(self):
        expected_cycles = 5       
        value = 0xa0
        expected_value = 0xa0
        self.cpu.a = 0x00
        self.memory.memory[emulator.START_ADDRESS] = eor.EOR_INDIRECTY_OPCODE
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