INC_ZEROPAGE_OPCODE = 0xe6
INC_ZEROPAGEX_OPCODE = 0xf6
INC_ABSOLUTE_OPCODE = 0xee
INC_ABSOLUTEX_OPCODE = 0xfe


class INCZeroPage(object):
    """INC Zero Page instruction"""
    def __init__(self):
        super(INCZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.inc(address)


class INCZeroPageX(object):
    """INC Zero Page X instruction"""
    def __init__(self):
        super(INCZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.inc(address)


class INCAbsolute(object):
    """INC absolute instruction"""
    def __init__(self):
        super(INCAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.inc(address)


class INCAbsoluteX(object):
    """INC absolute X instruction"""
    def __init__(self):
        super(INCAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        cpu.cycles += 1
        if address > 0xffff:
            address = address & 0xffff
        cpu.inc(address)