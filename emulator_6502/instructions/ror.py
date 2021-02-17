ROR_ACCUMULATOR_OPCODE = 0x6a
ROR_ZEROPAGE_OPCODE = 0x66
ROR_ZEROPAGEX_OPCODE = 0x76
ROR_ABSOLUTE_OPCODE = 0x6e
ROR_ABSOLUTEX_OPCODE = 0x7e


class RORAccumulator(object):
    def __init__(self):
        super(RORAccumulator, self).__init__()

    def run(self, cpu):
        cpu.ror()


class RORZeroPage(object):
    """ROR Zero Page instruction"""
    def __init__(self):
        super(RORZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.ror(address)


class RORZeroPageX(object):
    """ROR Zero Page X instruction"""
    def __init__(self):
        super(RORZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.ror(address)


class RORAbsolute(object):
    """ROR absolute instruction"""
    def __init__(self):
        super(RORAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.ror(address)


class RORAbsoluteX(object):
    """ROR absolute X instruction"""
    def __init__(self):
        super(RORAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        cpu.cycles += 1
        if address > 0xffff:
            address = address & 0xffff
        cpu.ror(address)