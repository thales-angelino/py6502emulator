EOR_IMMEDIATE_OPCODE = 0x49
EOR_ZEROPAGE_OPCODE = 0x45
EOR_ZEROPAGEX_OPCODE = 0x55
EOR_ABSOLUTE_OPCODE = 0x4d
EOR_ABSOLUTEX_OPCODE = 0x5d
EOR_ABSOLUTEY_OPCODE = 0x59
EOR_INDIRECTX_OPCODE = 0x41
EOR_INDIRECTY_OPCODE = 0x51


class EORImmediate(object):
    def __init__(self):
        super(EORImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("EOR memory byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)


class EORZeroPage(object):
    """EOR Zero Page instruction"""
    def __init__(self):
        super(EORZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("EOR zero page byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)


class EORZeroPageX(object):
    """EOR Zero Page X instruction"""
    def __init__(self):
        super(EORZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("EOR zero page X byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)


class EORAbsolute(object):
    """EOR absolute instruction"""
    def __init__(self):
        super(EORAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("EOR absolute byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)


class EORAbsoluteX(object):
    """EOR absolute X instruction"""
    def __init__(self):
        super(EORAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("EOR absolute x byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)


class EORAbsoluteY(object):
    """EOR absolute Y instruction"""
    def __init__(self):
        super(EORAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("EOR absolute Y byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)


class EORIndirectX(object):
    """EOR indirect X instruction"""
    def __init__(self):
        super(EORIndirectX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_x()
        print("EOR indirect X byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)


class EORIndirectY(object):
    """EOR Indirect Y instruction"""
    def __init__(self):
        super(EORIndirectY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_y()
        print("EOR indirect Y byte read: %s" % hex(byte_r))
        print("EOR register A read: %s" % hex(cpu.a))
        cpu.eor(byte_r)