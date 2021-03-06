LDX_IMMEDIATE_OPCODE = 0xa2
LDX_ZEROPAGE_OPCODE = 0xa6
LDX_ZEROPAGEY_OPCODE = 0xb6
LDX_ABSOLUTE_OPCODE = 0xae
LDX_ABSOLUTEY_OPCODE = 0xbe


class LDXImmediate(object):
    """LDX immediate instruction"""
    def __init__(self):
        super(LDXImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("LDX immediate byte read: %s" % hex(byte_r))
        cpu.load_register_x(byte_r)


class LDXZeroPage(object):
    """LDX Zero Page instruction"""
    def __init__(self):
        super(LDXZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("LDX zero page byte read: %s" % hex(byte_r))
        cpu.load_register_x(byte_r)


class LDXZeroPageY(object):
    """LDX Zero Page Y instruction"""
    def __init__(self):
        super(LDXZeroPageY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_y()
        print("LDX zero page Y byte read: %s" % hex(byte_r))
        cpu.load_register_x(byte_r)


class LDXAbsolute(object):
    """LDX Absolute instruction"""
    def __init__(self):
        super(LDXAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("LDX absolute byte read: %s" % hex(byte_r))
        cpu.load_register_x(byte_r)


class LDXAbsoluteY(object):
    """LDX Absolute Y instruction"""
    def __init__(self):
        super(LDXAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("LDX absolute Y byte read: %s" % hex(byte_r))
        cpu.load_register_x(byte_r)