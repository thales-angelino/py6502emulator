import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import brk


class TestBRK(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_brk(self):
        self.memory.memory[emulator.START_ADDRESS] = brk.BRK_IMPLIED_OPCODE
        self.memory.memory[emulator.INTERRUPT_VECTOR] = 0xaa
        self.memory.memory[emulator.INTERRUPT_VECTOR + 1] = 0xff
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, 0xffaa, "Program counter should be: 0xffaa")
        self.assertEqual(self.cpu.cycles, 7, "CPU cycles should be 7")
        self.assertEqual(self.memory.memory[0x1ff], 0x06, "Stack Address[0x1ff] should contain 0x06")
        self.assertEqual(self.memory.memory[0x1fe], 0x01, "Stack Address[0x1fe] should contain 0x01")
        self.assertEqual(self.cpu.stack_pointer, 0xfc, "Stack pointer should be: 0xfc")


if __name__ == '__main__':
    unittest.main()