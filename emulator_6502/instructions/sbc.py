SBC_IMMEDIATE_OPCODE = 0xe9
SBC_ZEROPAGE_OPCODE = 0xe5
SBC_ZEROPAGEX_OPCODE = 0xf5
SBC_ABSOLUTE_OPCODE = 0xed
SBC_ABSOLUTEX_OPCODE = 0xfd
SBC_ABSOLUTEY_OPCODE = 0xf9
SBC_INDIRECTX_OPCODE = 0xe1
SBC_INDIRECTY_OPCODE = 0xf1


class SBCImmediate(object):
    def __init__(self):
        super(SBCImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("SBC memory byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)


class SBCZeroPage(object):
    """SBC Zero Page instruction"""
    def __init__(self):
        super(SBCZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("SBC zero page byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)


class SBCZeroPageX(object):
    """SBC Zero Page X instruction"""
    def __init__(self):
        super(SBCZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("SBC zero page X byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)


class SBCAbsolute(object):
    """SBC absolute instruction"""
    def __init__(self):
        super(SBCAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("SBC absolute byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)


class SBCAbsoluteX(object):
    """SBC absolute X instruction"""
    def __init__(self):
        super(SBCAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("SBC absolute x byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)


class SBCAbsoluteY(object):
    """SBC absolute Y instruction"""
    def __init__(self):
        super(SBCAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("SBC absolute Y byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)


class SBCIndirectX(object):
    """SBC indirect X instruction"""
    def __init__(self):
        super(SBCIndirectX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_x()
        print("SBC indirect X byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)


class SBCIndirectY(object):
    """SBC Indirect Y instruction"""
    def __init__(self):
        super(SBCIndirectY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_y()
        print("SBC indirect Y byte read: %s" % hex(byte_r))
        print("SBC register A read: %s" % hex(cpu.a))
        print("SBC processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.sbc(byte_r)