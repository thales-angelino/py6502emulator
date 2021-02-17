ASL_ACCUMULATOR_OPCODE = 0x0a
ASL_ZEROPAGE_OPCODE = 0x06
ASL_ZEROPAGEX_OPCODE = 0x16
ASL_ABSOLUTE_OPCODE = 0x0e
ASL_ABSOLUTEX_OPCODE = 0x1e


class ASLAccumulator(object):
    def __init__(self):
        super(ASLAccumulator, self).__init__()

    def run(self, cpu):
        cpu.asl()


class ASLZeroPage(object):
    """ASL Zero Page instruction"""
    def __init__(self):
        super(ASLZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.asl(address)


class ASLZeroPageX(object):
    """ASL Zero Page X instruction"""
    def __init__(self):
        super(ASLZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.asl(address)


class ASLAbsolute(object):
    """ASL absolute instruction"""
    def __init__(self):
        super(ASLAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.asl(address)


class ASLAbsoluteX(object):
    """ASL absolute X instruction"""
    def __init__(self):
        super(ASLAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        cpu.cycles += 1
        if address > 0xffff:
            address = address & 0xffff
        cpu.asl(address)