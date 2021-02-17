import unittest
from emulator_6502 import emulator_6502 as emulator
from emulator_6502.instructions import adc


class TestADC(unittest.TestCase):
    def setUp(self):
        self.memory = emulator.Memory()
        self.cpu = emulator.CPU(self.memory)
        self.cpu.reset()

    def test_adc_scenario_1(self):
        operand = 0x10
        expected_value = 0x60
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x50
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_2(self):
        operand = 0x50
        expected_value = 0xa0
        expected_overflow = 1
        expected_carry = 0
        self.cpu.a = 0x50
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_3(self):
        operand = 0x90
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x50
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_4(self):
        operand = 0xd0
        expected_value = 0x20
        expected_overflow = 0
        expected_carry = 1
        self.cpu.a = 0x50
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_5(self):
        operand = 0x10
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_6(self):
        operand = 0x50
        expected_value = 0x20
        expected_overflow = 0
        expected_carry = 1
        self.cpu.a = 0xd0
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_7(self):
        operand = 0x90
        expected_value = 0x60
        expected_overflow = 1
        expected_carry = 1
        self.cpu.a = 0xd0
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_8(self):
        operand = 0xd0
        expected_value = 0xa0
        expected_overflow = 0
        expected_carry = 1
        self.cpu.a = 0xd0
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_scenario_9(self):
        operand = 0x10
        expected_value = 0xe1
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0xd0
        self.cpu.processor_status['carry'] = 1
        self.cpu.adc(operand)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)
        self.assertEqual(self.cpu.a, expected_value, "CPU Register A should be %s" % hex(expected_value))

    def test_adc_immediate(self):
        expected_cycles = 2
        value = 0xd0
        self.cpu.a = 0x10
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_IMMEDIATE_OPCODE
        self.memory.memory[0xfffd] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_adc_absolute(self):
        expected_cycles = 4
        value = 0xd0
        self.cpu.a = 0x10
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_ABSOLUTE_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x02ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_adc_absolutex(self):
        expected_cycles = 4
        value = 0xd0
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x10
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_ABSOLUTEX_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x0300] = value
        self.cpu.x = 0x01
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_adc_absolutey(self):
        expected_cycles = 4
        value = 0xd0
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x10
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_ABSOLUTEY_OPCODE
        self.memory.memory[0xfffd] = 0xff # LSB FIRST!!!
        self.memory.memory[0xfffe] = 0x02
        self.memory.memory[0x0301] = value
        self.cpu.y = 0x02
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_adc_zeropage(self):
        expected_cycles = 3
        value = 0xd0
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x10
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_ZEROPAGE_OPCODE
        self.memory.memory[0xfffd] = 0xff
        self.memory.memory[0x00ff] = value
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_adc_zeropagex(self):
        expected_cycles = 4
        value = 0xd0
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x10
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_ZEROPAGEX_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x008f] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_adc_indirectx(self):
        expected_cycles = 6
        value = 0xd0
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x10
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_INDIRECTX_OPCODE
        self.memory.memory[0xfffd] = 0x80
        self.memory.memory[0x008f] = 0x74
        self.memory.memory[0x0090] = 0x20
        self.memory.memory[0x2074] = value
        self.cpu.x = 0x0f
        self.cpu.execute(1)
        self.assertEqual(self.cpu.a, expected_value, "Register A should contain: %s" % hex(expected_value))
        self.assertEqual(self.cpu.cycles, expected_cycles, "CPU cycles should be %d" % expected_cycles)
        self.assertEqual(self.cpu.processor_status['carry'], expected_carry, "CPU Carry flag should be %d" % expected_carry)
        self.assertEqual(self.cpu.processor_status['overflow'], expected_overflow, "CPU Overflow flag should be %d" % expected_overflow)

    def test_adc_indirecty(self):
        expected_cycles = 5       
        value = 0xd0
        expected_value = 0xe0
        expected_overflow = 0
        expected_carry = 0
        self.cpu.a = 0x10
        self.memory.memory[emulator.START_ADDRESS] = adc.ADC_INDIRECTY_OPCODE
        self.memory.memory[0xfffd] = 0x80
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