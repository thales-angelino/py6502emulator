AND_IMMEDIATE_OPCODE = 0x29
AND_ZEROPAGE_OPCODE = 0x25
AND_ZEROPAGEX_OPCODE = 0x35
AND_ABSOLUTE_OPCODE = 0x2d
AND_ABSOLUTEX_OPCODE = 0x3d
AND_ABSOLUTEY_OPCODE = 0x39
AND_INDIRECTX_OPCODE = 0x21
AND_INDIRECTY_OPCODE = 0x31


class ANDImmediate(object):
    def __init__(self):
        super(ANDImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("AND memory byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)


class ANDZeroPage(object):
    """AND Zero Page instruction"""
    def __init__(self):
        super(ANDZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("AND zero page byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)


class ANDZeroPageX(object):
    """AND Zero Page X instruction"""
    def __init__(self):
        super(ANDZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("AND zero page X byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)


class ANDAbsolute(object):
    """AND absolute instruction"""
    def __init__(self):
        super(ANDAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("AND absolute byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)


class ANDAbsoluteX(object):
    """AND absolute X instruction"""
    def __init__(self):
        super(ANDAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("AND absolute x byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)


class ANDAbsoluteY(object):
    """AND absolute Y instruction"""
    def __init__(self):
        super(ANDAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("AND absolute Y byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)


class ANDIndirectX(object):
    """AND indirect X instruction"""
    def __init__(self):
        super(ANDIndirectX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_x()
        print("AND indirect X byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)


class ANDIndirectY(object):
    """AND Indirect Y instruction"""
    def __init__(self):
        super(ANDIndirectY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_y()
        print("AND indirect Y byte read: %s" % hex(byte_r))
        print("AND register A read: %s" % hex(cpu.a))
        cpu._and(byte_r)