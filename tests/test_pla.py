import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import pla


class TestPLA(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_pla_scenario1(self):
        expected_cycles = 4
        value = 0xfa
        expected_stack_pointer = 0xff
        used_stack_address = 0x1ff
        self.cpu.stack_pointer = 0xfe
        self.memory.memory[used_stack_address] = value
        self.memory.memory[emulator.START_ADDRESS] = pla.PLA_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.stack_pointer, expected_stack_pointer, "Stack pointer should contain: %s" % hex(expected_stack_pointer))
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_pla_scenario2(self):
        expected_cycles = 8
        value = 0xfa
        value2 = 0xf0
        expected_stack_pointer = 0xff
        used_stack_address = 0x1ff
        self.cpu.stack_pointer = 0xfd
        self.memory.memory[used_stack_address] = value
        self.memory.memory[used_stack_address-1] = value2
        self.memory.memory[emulator.START_ADDRESS] = pla.PLA_IMPLIED_OPCODE
        self.memory.memory[emulator.START_ADDRESS+1] = pla.PLA_IMPLIED_OPCODE
        # Stack: Last in, first out!
        self.cpu.execute(1)
        self.assertEqual(self.cpu.stack_pointer, expected_stack_pointer-1, "Stack pointer should contain: %s" % hex(expected_stack_pointer-1))
        self.assertEqual(self.cpu.a, value2, "Register A should contain: %s" % hex(value2))
        self.cpu.execute(1)
        self.assertEqual(self.cpu.stack_pointer, expected_stack_pointer, "Stack pointer should contain: %s" % hex(expected_stack_pointer))
        self.assertEqual(self.cpu.a, value, "Register A should contain: %s" % hex(value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()