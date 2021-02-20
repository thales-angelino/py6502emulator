DEC_ZEROPAGE_OPCODE = 0xc6
DEC_ZEROPAGEX_OPCODE = 0xd6
DEC_ABSOLUTE_OPCODE = 0xce
DEC_ABSOLUTEX_OPCODE = 0xde


class DECZeroPage(object):
    """DEC Zero Page instruction"""
    def __init__(self):
        super(DECZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.dec(address)


class DECZeroPageX(object):
    """DEC Zero Page X instruction"""
    def __init__(self):
        super(DECZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.dec(address)


class DECAbsolute(object):
    """DEC absolute instruction"""
    def __init__(self):
        super(DECAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.dec(address)


class DECAbsoluteX(object):
    """DEC absolute X instruction"""
    def __init__(self):
        super(DECAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        cpu.cycles += 1
        if address > 0xffff:
            address = address & 0xffff
        cpu.dec(address)