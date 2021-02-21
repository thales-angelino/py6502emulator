import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import jmp


class TestJMP(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_jmp_absolute(self):
        expected_cycles = 3
        address = 0x02f0
        self.memory.memory[emulator.START_ADDRESS] = jmp.JMP_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xf0 # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, address, "Program counter should be %d" % address)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_jmp_indirect(self):
        expected_cycles = 5
        lsb = 0xfc
        msb = 0xba
        expected_value = 0xbafc
        address = 0x02f0
        self.memory.memory[emulator.START_ADDRESS] = jmp.JMP_INDIRECT_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xf0
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[address] = lsb
        self.memory.memory[address + 1] = msb
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, expected_value, "Program counter should be %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()