from checks import check_processor_flags_routine

ADC_IMMEDIATE_OPCODE = 0x69
ADC_ZEROPAGE_OPCODE = 0x65
ADC_ZEROPAGEX_OPCODE = 0x75
ADC_ABSOLUTE_OPCODE = 0x6d
ADC_ABSOLUTEX_OPCODE = 0x7d
ADC_ABSOLUTEY_OPCODE = 0x79
ADC_INDIRECTX_OPCODE = 0x61
ADC_INDIRECTY_OPCODE = 0x71

LSB_7BITS_ENABLED_MASK = 0x7f 
OVERFLOW_MASK = 0x80


def adc(cpu, value):
    """
    ADC instruction

    http://www.righto.com/2012/12/the-6502-overflow-flag-explained.html

    It should also check the processor status decimal flag.
    """
    result = cpu.a + value + cpu.processor_status['carry']
    c6 = ((cpu.a & LSB_7BITS_ENABLED_MASK) +
          (value & LSB_7BITS_ENABLED_MASK) + 
          cpu.processor_status['carry']) & OVERFLOW_MASK
    if c6:
        c6 = 1
    cpu.a = (result & 0xff)

    cpu.processor_status['carry'] = 0
    if result > 0xff:
        cpu.processor_status['carry'] = 1
    
    if c6 ^ cpu.processor_status['carry']:
        cpu.processor_status['overflow'] = 1


class ADCImmediate(object):
    def __init__(self):
        super(ADCImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.fetch_byte()
        print("ADC memory byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)


class ADCZeroPage(object):
    """ADC Zero Page instruction"""
    def __init__(self):
        super(ADCZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        print("ADC absolute Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("ADC zero page byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)


class ADCZeroPageX(object):
    """ADC Zero Page X instruction"""
    def __init__(self):
        super(ADCZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        # Truncate if the address is exceeded
        if address > 0xff:
            address = address & 0xff
        byte_r = cpu.read_byte(address)
        print("ADC zero page X byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)


class ADCAbsolute(object):
    """ADC absolute instruction"""
    def __init__(self):
        super(ADCAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        byte_r = cpu.read_byte(address)
        print("ADC absolute byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)


class ADCAbsoluteX(object):
    """ADC absolute X instruction"""
    def __init__(self):
        super(ADCAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1
        byte_r = cpu.read_byte(address)
        print("ADC absolute x byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)


class ADCAbsoluteY(object):
    """ADC absolute Y instruction"""
    def __init__(self):
        super(ADCAbsoluteY, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.y
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1
        byte_r = cpu.read_byte(address)
        print("ADC absolute Y byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)


class ADCIndirectX(object):
    """ADC indirect X instruction"""
    def __init__(self):
        super(ADCIndirectX, self).__init__()

    def run(self, cpu):
        zp_address = cpu.fetch_byte() + cpu.x
        zp_address = zp_address & 0xff
        cpu.cycles += 1
        address = cpu.read_word(zp_address)
        byte_r = cpu.read_byte(address)
        print("ADC indirect X byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)


class ADCIndirectY(object):
    """ADC Indirect Y instruction"""
    def __init__(self):
        super(ADCIndirectY, self).__init__()

    def run(self, cpu):
        zp_address = cpu.fetch_byte()
        address = cpu.read_word(zp_address) + cpu.y        
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1
        byte_r = cpu.read_byte(address)
        print("ADC indirect Y byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        adc(cpu, byte_r)