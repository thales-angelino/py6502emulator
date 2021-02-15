import unittest
import emulator_6502 as emulator
from instructions import rol


class TestROL(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_rol_accumulator(self):
        expected_cycles = 2
        self.cpu.a = 0xa0
        expected_value = 0x41
        expected_carry = 1
        self.cpu.processor_status['carry'] = 1
        self.memory.memory[emulator.START_ADDRESS] = rol.ROL_ACCUMULATOR_OPCODE
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)

    def test_rol_absolute(self):
        expected_cycles = 6
        value = 0xa0
        address = 0x02ff
        expected_value = 0x41
        expected_carry = 1
        self.cpu.processor_status['carry'] = 1
        self.memory.memory[emulator.START_ADDRESS] = rol.ROL_ABSOLUTE_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[address] = value
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address], expected_value, "Memory M should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)

    def test_rol_absolutex(self):
        expected_cycles = 7
        value = 0xa0
        address = 0x0300
        expected_value = 0x41
        expected_carry = 1
        self.cpu.processor_status['carry'] = 1
        self.memory.memory[emulator.START_ADDRESS] = rol.ROL_ABSOLUTEX_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[address] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address], expected_value, "Memory M should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)

    def test_rol_zeropage(self):
        expected_cycles = 5
        value = 0x01
        address = 0x00ff
        expected_value = 0x03
        expected_carry = 0
        self.cpu.processor_status['carry'] = 1
        self.memory.memory[emulator.START_ADDRESS] = rol.ROL_ZEROPAGE_OPCODE
        self.memory.memory[0xfffd] = 0xff
        self.memory.memory[address] = value
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address], expected_value, "Memory M should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)

    def test_rol_zeropagex(self):
        expected_cycles = 6
        value = 0xa0
        address = 0x008f
        expected_value = 0x41
        expected_carry = 1
        self.cpu.processor_status['carry'] = 1
        self.memory.memory[emulator.START_ADDRESS] = rol.ROL_ZEROPAGEX_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[address] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.memory.memory[address], expected_value, "Memory M should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)


if __name__ == '__main__':
    unittest.main()