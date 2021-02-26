import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import php


class TestPHP(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_php(self):
        expected_value = 0x8a
        expected_cycles = 3
        expected_carry = 0
        expected_zero = 1
        expected_interrupt_disable = 0
        expected_decimal_mode = 1
        expected_break_command = 0
        expected_overflow = 0
        expected_negative = 1
        self.cpu.processor_status['carry'] = expected_carry
        self.cpu.processor_status['zero'] = expected_zero
        self.cpu.processor_status['interrupt_disable'] = expected_interrupt_disable
        self.cpu.processor_status['decimal_mode'] = expected_decimal_mode
        self.cpu.processor_status['break_command'] = expected_break_command
        self.cpu.processor_status['overflow'] = expected_overflow
        self.cpu.processor_status['negative'] = expected_negative
        used_stack_address = 0x1ff
        self.memory.memory[emulator.START_ADDRESS] = php.PHP_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[used_stack_address], expected_value, "Stack at %s should contain: %s" % (hex(used_stack_address), hex(expected_value)))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()