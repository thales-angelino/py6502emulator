import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import rti


class TestRTI(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_rti(self):
        self.memory.memory[emulator.START_ADDRESS] = rti.RTI_IMPLIED_OPCODE
        self.memory.memory[0x1ff] = 0x06
        self.memory.memory[0x1fe] = 0x05
        self.memory.memory[0x1fd] = 0x01
        self.cpu.stack_pointer = 0xfc
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, 0x0605, "Program counter should be: 0x0605")
        self.assertEqual(self.cpu.cycles, 6, "CPU cycles should be 6")
        self.assertEqual(self.cpu.processor_status['carry'], 1, "Carry should be 1")


if __name__ == '__main__':
    unittest.main()