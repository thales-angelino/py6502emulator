LDA_IMMEDIATE_OPCODE = 0xa9
LDA_ZEROPAGE_OPCODE = 0xa5
LDA_ZEROPAGEX_OPCODE = 0xb5
LDA_ABSOLUTE_OPCODE = 0xad
LDA_ABSOLUTEX_OPCODE = 0xbd
LDA_ABSOLUTEY_OPCODE = 0xb9
LDA_INDIRECTX_OPCODE = 0xa1
LDA_INDIRECTY_OPCODE = 0xb1


class LDAImmediate(object):
    """LDA immediate instruction"""
    def __init__(self):
        super(LDAImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("LDA immediate byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)


class LDAZeroPage(object):
    """LDA Zero Page instruction"""
    def __init__(self):
        super(LDAZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("LDA zero page byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)


class LDAZeroPageX(object):
    """LDA Zero Page X instruction"""
    def __init__(self):
        super(LDAZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("LDA zero page byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)


class LDAAbsolute(object):
    """LDA Absolute instruction"""
    def __init__(self):
        super(LDAAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("LDA absolute byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)


class LDAAbsoluteX(object):
    """LDA Absolute X instruction"""
    def __init__(self):
        super(LDAAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("LDA absolute X byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)


class LDAAbsoluteY(object):
    """LDA Absolute Y instruction"""
    def __init__(self):
        super(LDAAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("LDA absolute Y byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)


class LDAIndirectX(object):
    """LDA Indirect X instruction"""
    def __init__(self):
        super(LDAIndirectX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_x()
        print("LDA indirect X byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)


class LDAIndirectY(object):
    """LDA Indirect Y instruction"""
    def __init__(self):
        super(LDAIndirectY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_y()
        print("LDA indirect y byte read: %s" % hex(byte_r))
        cpu.load_register_a(byte_r)