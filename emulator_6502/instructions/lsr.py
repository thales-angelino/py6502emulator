LSR_ACCUMULATOR_OPCODE = 0x4a
LSR_ZEROPAGE_OPCODE = 0x46
LSR_ZEROPAGEX_OPCODE = 0x56
LSR_ABSOLUTE_OPCODE = 0x4e
LSR_ABSOLUTEX_OPCODE = 0x5e


class LSRAccumulator(object):
    def __init__(self):
        super(LSRAccumulator, self).__init__()

    def run(self, cpu):
        cpu.lsr()


class LSRZeroPage(object):
    """LSR Zero Page instruction"""
    def __init__(self):
        super(LSRZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.lsr(address)


class LSRZeroPageX(object):
    """LSR Zero Page X instruction"""
    def __init__(self):
        super(LSRZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.lsr(address)


class LSRAbsolute(object):
    """LSR absolute instruction"""
    def __init__(self):
        super(LSRAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.lsr(address)


class LSRAbsoluteX(object):
    """LSR absolute X instruction"""
    def __init__(self):
        super(LSRAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        cpu.cycles += 1
        if address > 0xffff:
            address = address & 0xffff
        cpu.lsr(address)