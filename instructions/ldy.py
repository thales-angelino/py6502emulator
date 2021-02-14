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
        byte_r = cpu.immediate()
        print("LDY immediate byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)


class LDYZeroPage(object):
    """LDY Zero Page instruction"""
    def __init__(self):
        super(LDYZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("LDY zero page byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)

class LDYZeroPageX(object):
    """LDY Zero Page X instruction"""
    def __init__(self):
        super(LDYZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("LDY zero page byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)


class LDYAbsolute(object):
    """LDY Absolute instruction"""
    def __init__(self):
        super(LDYAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("LDY absolute byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)


class LDYAbsoluteX(object):
    """LDY Absolute X instruction"""
    def __init__(self):
        super(LDYAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("LDY absolute X byte read: %s" % hex(byte_r))
        cpu.load_register_y(byte_r)