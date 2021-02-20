import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import inc


class TestINC(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_inc_absolute(self):
        expected_zero = 0
        expected_negative = 1
        expected_cycles = 6
        value = 0x7f
        address = 0x02ff
        expected_value = 0x80
        self.memory.memory[emulator.START_ADDRESS] = inc.INC_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[address] = value
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address] , expected_value, "CPU memory should be %d" % expected_value)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_inc_absolutex(self):
        expected_cycles = 7
        expected_zero = 1
        expected_negative = 0
        value = 0xff
        expected_value = 0x00
        address = 0x0300
        self.memory.memory[emulator.START_ADDRESS] = inc.INC_ABSOLUTEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[address] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address], expected_value, "CPU memory should be %d" % expected_value)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_inc_zeropage(self):
        expected_cycles = 5
        expected_zero = 0
        expected_negative = 0
        value = 0x00
        expected_value = 0x01
        address = 0x00ff
        self.memory.memory[emulator.START_ADDRESS] = inc.INC_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.memory.memory[address] = value
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address], expected_value, "CPU memory should be %d" % expected_value)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)

    def test_inc_zeropagex(self):
        expected_cycles = 6
        expected_zero = 1
        expected_negative = 0
        value = 0xff
        expected_value = 0x00
        address = 0x008f
        self.memory.memory[emulator.START_ADDRESS] = inc.INC_ZEROPAGEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[address] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address], expected_value, "CPU memory should be %d" % expected_value)
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['zero'], expected_zero, "CPU zero flag should be %d" % expected_zero)
        self.assertEqual(self.cpu.processor_status['negative'], expected_negative, "CPU negative flag should be %d" % expected_negative)


if __name__ == '__main__':
    unittest.main()