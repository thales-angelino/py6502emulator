CMP_IMMEDIATE_OPCODE = 0xc9
CMP_ZEROPAGE_OPCODE = 0xc5
CMP_ZEROPAGEX_OPCODE = 0xd5
CMP_ABSOLUTE_OPCODE = 0xcd
CMP_ABSOLUTEX_OPCODE = 0xdd
CMP_ABSOLUTEY_OPCODE = 0xd9
CMP_INDIRECTX_OPCODE = 0xc1
CMP_INDIRECTY_OPCODE = 0xd1


class CMPImmediate(object):
    def __init__(self):
        super(CMPImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("CMP memory byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)


class CMPZeroPage(object):
    """CMP Zero Page instruction"""
    def __init__(self):
        super(CMPZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("CMP zero page byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)


class CMPZeroPageX(object):
    """CMP Zero Page X instruction"""
    def __init__(self):
        super(CMPZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("CMP zero page X byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)


class CMPAbsolute(object):
    """CMP absolute instruction"""
    def __init__(self):
        super(CMPAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("CMP absolute byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)


class CMPAbsoluteX(object):
    """CMP absolute X instruction"""
    def __init__(self):
        super(CMPAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("CMP absolute x byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)


class CMPAbsoluteY(object):
    """CMP absolute Y instruction"""
    def __init__(self):
        super(CMPAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("CMP absolute Y byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)


class CMPIndirectX(object):
    """CMP indirect X instruction"""
    def __init__(self):
        super(CMPIndirectX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_x()
        print("CMP indirect X byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)


class CMPIndirectY(object):
    """CMP Indirect Y instruction"""
    def __init__(self):
        super(CMPIndirectY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_y()
        print("CMP indirect Y byte read: %s" % hex(byte_r))
        print("CMP register A read: %s" % hex(cpu.a))
        print("CMP processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cmp(byte_r)