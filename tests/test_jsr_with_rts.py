import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import jsr, rts


class TestJSRWithRTS(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_jsr_with_rts(self):
        self.memory.memory[emulator.START_ADDRESS] = jsr.JSR_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x40 # LE byte first! 
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x30
        self.memory.memory[0x3040] = rts.RTS_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, 0x3040, "Program counter should be: 0x3040")
        self.assertEqual(self.cpu.cycles, 6, "CPU cycles should be 6")
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, emulator.START_ADDRESS+3, "Program counter should be: 0x603")
        self.assertEqual(self.cpu.cycles, 12, "CPU cycles should be 12")


if __name__ == '__main__':
    unittest.main()