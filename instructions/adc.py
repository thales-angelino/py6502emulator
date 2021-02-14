ADC_IMMEDIATE_OPCODE = 0x69
ADC_ZEROPAGE_OPCODE = 0x65
ADC_ZEROPAGEX_OPCODE = 0x75
ADC_ABSOLUTE_OPCODE = 0x6d
ADC_ABSOLUTEX_OPCODE = 0x7d
ADC_ABSOLUTEY_OPCODE = 0x79
ADC_INDIRECTX_OPCODE = 0x61
ADC_INDIRECTY_OPCODE = 0x71


class ADCImmediate(object):
    def __init__(self):
        super(ADCImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("ADC memory byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)


class ADCZeroPage(object):
    """ADC Zero Page instruction"""
    def __init__(self):
        super(ADCZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("ADC zero page byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)


class ADCZeroPageX(object):
    """ADC Zero Page X instruction"""
    def __init__(self):
        super(ADCZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("ADC zero page X byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)


class ADCAbsolute(object):
    """ADC absolute instruction"""
    def __init__(self):
        super(ADCAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("ADC absolute byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)


class ADCAbsoluteX(object):
    """ADC absolute X instruction"""
    def __init__(self):
        super(ADCAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("ADC absolute x byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)


class ADCAbsoluteY(object):
    """ADC absolute Y instruction"""
    def __init__(self):
        super(ADCAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("ADC absolute Y byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)


class ADCIndirectX(object):
    """ADC indirect X instruction"""
    def __init__(self):
        super(ADCIndirectX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_x()
        print("ADC indirect X byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)


class ADCIndirectY(object):
    """ADC Indirect Y instruction"""
    def __init__(self):
        super(ADCIndirectY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_y()
        print("ADC indirect Y byte read: %s" % hex(byte_r))
        print("ADC register A read: %s" % hex(cpu.a))
        print("ADC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.adc(byte_r)