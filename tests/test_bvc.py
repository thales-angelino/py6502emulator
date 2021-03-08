import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import bvc


class TestBVC(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_bvc_scenario1(self):
        expected_cycles = 3
        value = 0x03
        expected_pc = 0x604
        self.memory.memory[emulator.START_ADDRESS] = bvc.BVC_RELATIVE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.processor_status['overflow'] = 0
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, expected_pc, "Program counter should contain: %s" % hex(expected_pc))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_bvc_scenario2(self):
        expected_cycles = 4
        value = 0xfc
        expected_pc = 0x5fe
        self.memory.memory[emulator.START_ADDRESS] = bvc.BVC_RELATIVE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.processor_status['overflow'] = 0
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, expected_pc, "Program counter should contain: %s" % hex(expected_pc))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_bvc_scenario3(self):
        expected_cycles = 2
        value = 0xfc
        expected_pc = 0x602
        self.cpu.processor_status['overflow'] = 1
        self.memory.memory[emulator.START_ADDRESS] = bvc.BVC_RELATIVE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.program_counter, expected_pc, "Program counter should contain: %s" % hex(expected_pc))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()