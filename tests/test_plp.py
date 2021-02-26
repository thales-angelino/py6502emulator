import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import plp


class TestPLP(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_plp(self):
        value = 0x8a
        expected_cycles = 4
        expected_carry = 0
        expected_zero = 1
        expected_interrupt_disable = 0
        expected_decimal_mode = 1
        expected_break_command = 0
        expected_overflow = 0
        expected_negative = 1
        used_stack_address = 0x1ff
        self.memory.memory[used_stack_address] = value
        self.cpu.stack_pointer = 0xfe
        self.memory.memory[emulator.START_ADDRESS] = plp.PLP_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "carry should contain: %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "zero should contain: %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['interrupt_disable'], expected_interrupt_disable, "interrupt_disable should contain: %d" % expected_interrupt_disable)
        self.assertEqual(self.cpu.processor_status['decimal_mode'], expected_decimal_mode, "decimal_mode should contain: %d" % expected_decimal_mode)
        self.assertEqual(self.cpu.processor_status['break_command'], expected_break_command, "break_command should contain: %d" % expected_break_command)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "overflow should contain: %d" % expected_overflow)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "negative should contain: %d" % expected_negative)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()