import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import sta


class TestSTA(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_sta_absolute(self):
        expected_cycles = 4
        value = 0xf0
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = sta.STA_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x02ff], value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sta_absolutex(self):
        expected_cycles = 5
        value = 0xf0
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = sta.STA_ABSOLUTEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x0300], value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sta_absolutey(self):
        expected_cycles = 5
        value = 0xf0
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = sta.STA_ABSOLUTEY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x0301], value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sta_zeropage(self):
        expected_cycles = 3
        value = 0xf0
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = sta.STA_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x00ff], value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sta_zeropagex(self):
        expected_cycles = 4
        value = 0xf0
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = sta.STA_ZEROPAGEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x008f], value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sta_indirectx(self):
        expected_cycles = 6
        value = 0xf0
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = sta.STA_INDIRECTX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = 0x74
        self.memory.memory[0x0090] = 0x20
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x2074], value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_sta_indirecty(self):
        expected_cycles = 6
        value = 0xf0
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = sta.STA_INDIRECTY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x0080] = 0x74
        self.memory.memory[0x0081] = 0x20
        self.cpu.y = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[0x2075], value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()