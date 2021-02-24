import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import pha


class TestPHA(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_pha_scenario1(self):
        expected_cycles = 3
        value = 0xfa
        expected_stack_pointer = 0xfe
        used_stack_address = 0x1ff
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = pha.PHA_IMPLIED_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.stack_pointer, expected_stack_pointer, "Stack pointer should contain: %s" % hex(expected_stack_pointer))
        self.assertEqual(self.memory.memory[used_stack_address], value, "Stack at %s address should contain: %s" % (hex(used_stack_address), hex(value)))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)

    def test_pha_scenario2(self):
        expected_cycles = 6
        value = 0xfa
        expected_stack_pointer = 0xfd
        used_stack_address = 0x1fe
        self.cpu.a = value
        self.memory.memory[emulator.START_ADDRESS] = pha.PHA_IMPLIED_OPCODE
        self.memory.memory[emulator.START_ADDRESS+1] = pha.PHA_IMPLIED_OPCODE
        self.cpu.execute(2)
        self.assertEqual(self.cpu.stack_pointer, expected_stack_pointer, "Stack pointer should contain: %s" % hex(expected_stack_pointer))
        self.assertEqual(self.memory.memory[used_stack_address], value, "Stack at %s address should contain: %s" % (hex(used_stack_address), hex(value)))
        self.assertEqual(self.memory.memory[used_stack_address+1], value, "Stack at %s address should contain: %s" % (hex(used_stack_address+1), hex(value)))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)


if __name__ == '__main__':
    unittest.main()