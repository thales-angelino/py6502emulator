import unittest
import emulator_6502 as emulator
from instructions import sbc


class TestSBC(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset() 

    def test_sbc_scenario_1(self):
        operand = 0xf0
        expected_value = 0x5f
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x50
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_scenario_2(self):
        operand = 0xb0
        expected_value = 0x9f
        expected_overflow = 1
        expected_carry = 0
        self.cpu.a = 0x50
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_scenario_3(self):
        operand = 0x70
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x50
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_scenario_4(self):
        operand = 0x30
        expected_value = 0x1f
        expected_overflow = 0
        expected_carry = 1
        self.cpu.a = 0x50
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_scenario_5(self):
        operand = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_scenario_6(self):
        operand = 0xb0
        expected_value = 0x1f
        expected_overflow = 0
        expected_carry = 1
        self.cpu.a = 0xd0
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_scenario_7(self):
        operand = 0x70
        expected_value = 0x5f
        expected_overflow = 1
        expected_carry = 1
        self.cpu.a = 0xd0
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_scenario_8(self):
        operand = 0x30
        expected_value = 0x9f
        expected_overflow = 0
        expected_carry = 1
        self.cpu.a = 0xd0
        self.cpu.sbc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_sbc_immediate(self):
        expected_cycles = 2
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_IMMEDIATE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_sbc_absolute(self):
        expected_cycles = 4
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_ABSOLUTE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_sbc_absolutex(self):
        expected_cycles = 4
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_ABSOLUTEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x0300] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_sbc_absolutey(self):
        expected_cycles = 4
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_ABSOLUTEY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff # LSB FIRST!!!
        self.memory.memory[emulator.START_ADDRESS + 2] = 0x02
        self.memory.memory[0x0301] = value
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_sbc_zeropage(self):
        expected_cycles = 3
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_ZEROPAGE_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_sbc_zeropagex(self):
        expected_cycles = 4
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_ZEROPAGEX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_sbc_indirectx(self):
        expected_cycles = 6
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_INDIRECTX_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x008f] = 0x74
        self.memory.memory[0x0090] = 0x20
        self.memory.memory[0x2074] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_sbc_indirecty(self):
        expected_cycles = 5
        value = 0xf0
        expected_value = 0xdf
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.memory.memory[emulator.START_ADDRESS] = sbc.SBC_INDIRECTY_OPCODE
        self.memory.memory[emulator.START_ADDRESS + 1] = 0x80
        self.memory.memory[0x0080] = 0x74
        self.memory.memory[0x0081] = 0x20
        self.memory.memory[0x2075] = value
        self.cpu.y = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)


if __name__ == '__main__':
    unittest.main()