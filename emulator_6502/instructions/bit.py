BIT_ZEROPAGE_OPCODE = 0x24
BIT_ABSOLUTE_OPCODE = 0x2c


class BITZeroPage(object):
    """BIT Zero Page instruction"""
    def __init__(self):
        super(BITZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("BIT zero page byte read: %s" % hex(byte_r))
        print("BIT register A read: %s" % hex(cpu.a))
        cpu.bit(byte_r)


class BITAbsolute(object):
    """BIT absolute instruction"""
    def __init__(self):
        super(BITAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("BIT absolute byte read: %s" % hex(byte_r))
        print("BIT register A read: %s" % hex(cpu.a))
        cpu.bit(byte_r)