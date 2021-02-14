LDY_IMMEDIATE_OPCODE = 0xa0
LDY_ZEROPAGE_OPCODE = 0xa4
LDY_ZEROPAGEX_OPCODE = 0xb4
LDY_ABSOLUTE_OPCODE = 0xac
LDY_ABSOLUTEX_OPCODE = 0xbc


class LDYImmediate(object):
    """LDY immediate instruction"""
    def __init__(self):
        super(LDYImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.fetch_byte()
        print("LDY immediate byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)


class LDYZeroPage(object):
    """LDY Zero Page instruction"""
    def __init__(self):
        super(LDYZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        print("LDY absolute Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDY zero page byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)

class LDYZeroPageX(object):
    """LDY Zero Page X instruction"""
    def __init__(self):
        super(LDYZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        # Truncate if the address is exceeded
        if address > 0xff:
            address = address & 0xff

        print("LDY zero page + X address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDY zero page byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)


class LDYAbsolute(object):
    """LDY Absolute instruction"""
    def __init__(self):
        super(LDYAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        print("LDY absolute Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDY absolute byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)


class LDYAbsoluteX(object):
    """LDY Absolute X instruction"""
    def __init__(self):
        super(LDYAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1
        print("LDY absolute X Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDY absolute X byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)