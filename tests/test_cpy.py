import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import cpy


class TestCPX(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_cpy_scenario_1(self):
        operand = 0x10
        expected_zero = 0
        expected_negative = 0
        expected_carry = 1
        self.cpu.y = 0x50
        self.cpu.cpy(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_cpy_scenario_2(self):
        operand = 0x50
        expected_zero = 1
        expected_negative = 0
        expected_carry = 1
        self.cpu.y = 0x50
        self.cpu.cpy(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_cpy_scenario_3(self):
        operand = 0x60
        expected_zero = 0
        expected_negative = 1
        expected_carry = 0
        self.cpu.y = 0x50
        self.cpu.cpy(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_cpy_immediate(self):
        expected_cycles = 2
        value = 0x10
        self.cpu.y = 0x50
        expected_zero = 0
        expected_negative = 0
        expected_carry = 1
        self.memory.memory[emulator.START_ADDRESS] = cpy.CPY_IMMEDIATE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_cpy_absolute(self):
        expected_cycles = 4
        value = 0x10
        self.cpu.y = 0x50
        expected_zero = 0
        expected_negative = 0
        expected_carry = 1
        self.memory.memory[emulator.START_ADDRESS] = cpy.CPY_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_cpy_zeropage(self):
        expected_cycles = 3
        value = 0x10
        self.cpu.y = 0x50
        expected_zero = 0
        expected_negative = 0
        expected_carry = 1
        self.memory.memory[emulator.START_ADDRESS] = cpy.CPY_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)


if __name__ == '__main__':
    unittest.main()