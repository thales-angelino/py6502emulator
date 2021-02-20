import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import dey


class TestDEX(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_dey_scenario_1(self):
        expected_zero = 0
        expected_negative = 1
        expected_value = 0xff
        self.cpu.y  = 0x00
        self.cpu.dey()
        self.assertEqual(self.cpu.y , expected_value, "CPU register y should be %d" % expected_value)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_dey_scenario_2(self):
        expected_zero = 1
        expected_negative = 0
        expected_value = 0x00
        self.cpu.y  = 0x01
        self.cpu.dey()
        self.assertEqual(self.cpu.y , expected_value, "CPU register y should be %d" % expected_value)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_dey_scenario_3(self):
        expected_zero = 0
        expected_negative = 0
        expected_value = 0x7f
        self.cpu.y  = 0x80
        self.cpu.dey()
        self.assertEqual(self.cpu.y , expected_value, "CPU register y should be %d" % expected_value)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_dey_implied(self):
        expected_cycles = 2
        value = 0
        expected_value = 0x7f
        self.cpu.y  = 0x80
        self.memory.memory[emulator.START_ADDRESS] = dey.DEY_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.y , expected_value, "CPU register y should be %d" % expected_value)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()