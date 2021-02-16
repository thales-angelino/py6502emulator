STX_ZEROPAGE_OPCODE = 0x86
STX_ZEROPAGEY_OPCODE = 0x96
STX_ABSOLUTE_OPCODE = 0x8e


class STXZeroPage(object):
    """STX Zero Page instruction"""
    def __init__(self):
        super(STXZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.stx(address)


class STXZeroPageY(object):
    """STX Zero Page Y instruction"""
    def __init__(self):
        super(STXZeroPageY, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.y
        cpu.cycles += 1
        cpu.stx(address)


class STXAbsolute(object):
    """STX absolute instruction"""
    def __init__(self):
        super(STXAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.stx(address)