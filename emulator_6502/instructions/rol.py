ROL_ACCUMULATOR_OPCODE = 0x2a
ROL_ZEROPAGE_OPCODE = 0x26
ROL_ZEROPAGEX_OPCODE = 0x36
ROL_ABSOLUTE_OPCODE = 0x2e
ROL_ABSOLUTEX_OPCODE = 0x3e


class ROLAccumulator(object):
    def __init__(self):
        super(ROLAccumulator, self).__init__()

    def run(self, cpu):
        cpu.rol()


class ROLZeroPage(object):
    """ROL Zero Page instruction"""
    def __init__(self):
        super(ROLZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.rol(address)


class ROLZeroPageX(object):
    """ROL Zero Page X instruction"""
    def __init__(self):
        super(ROLZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.rol(address)


class ROLAbsolute(object):
    """ROL absolute instruction"""
    def __init__(self):
        super(ROLAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.rol(address)


class ROLAbsoluteX(object):
    """ROL absolute X instruction"""
    def __init__(self):
        super(ROLAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        cpu.cycles += 1
        if address > 0xffff:
            address = address & 0xffff
        cpu.rol(address)