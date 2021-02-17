STY_ZEROPAGE_OPCODE = 0x84
STY_ZEROPAGEX_OPCODE = 0x94
STY_ABSOLUTE_OPCODE = 0x8c


class STYZeroPage(object):
    """STY Zero Page instruction"""
    def __init__(self):
        super(STYZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.sty(address)


class STYZeroPageX(object):
    """STY Zero Page X instruction"""
    def __init__(self):
        super(STYZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.sty(address)


class STYAbsolute(object):
    """STY absolute instruction"""
    def __init__(self):
        super(STYAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.sty(address)