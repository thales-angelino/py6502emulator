import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import lda


class TestLDA(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_lda_immediate(self):
        expected_cycles = 2
        value = 0xfa
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_IMMEDIATE_OPCODE
        self.memory.memory[0xfffd] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_absolute(self):
        expected_cycles = 4
        value = 0x32
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_ABSOLUTE_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_absolutex(self):
        expected_cycles = 4
        value = 0x41
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_ABSOLUTEX_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x0300] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_absolutey(self):
        expected_cycles = 4
        value = 0x38
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_ABSOLUTEY_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x0301] = value
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_zeropage(self):
        expected_cycles = 3
        value = 0x77
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_ZEROPAGE_OPCODE
        self.memory.memory[0xfffd] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_zeropagex(self):
        expected_cycles = 4
        value = 0x67
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_ZEROPAGEX_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_indirectx(self):
        expected_cycles = 6
        value = 0x68
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_INDIRECTX_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x008f] = 0x74
        self.memory.memory[0x0090] = 0x20
        self.memory.memory[0x2074] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_lda_indirecty(self):
        expected_cycles = 5 # FAIL
        value = 0x67
        self.memory.memory[emulator.START_ADDRESS] = lda.LDA_INDIRECTY_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x0080] = 0x74
        self.memory.memory[0x0081] = 0x20
        self.memory.memory[0x2075] = value
        self.cpu.y = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

if __name__ == '__main__':
    unittest.main()