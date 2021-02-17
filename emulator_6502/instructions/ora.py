ORA_IMMEDIATE_OPCODE = 0x09
ORA_ZEROPAGE_OPCODE = 0x05
ORA_ZEROPAGEX_OPCODE = 0x15
ORA_ABSOLUTE_OPCODE = 0x0d
ORA_ABSOLUTEX_OPCODE = 0x1d
ORA_ABSOLUTEY_OPCODE = 0x19
ORA_INDIRECTX_OPCODE = 0x01
ORA_INDIRECTY_OPCODE = 0x11


class ORAImmediate(object):
    def __init__(self):
        super(ORAImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("ORA memory byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)


class ORAZeroPage(object):
    """ORA Zero Page instruction"""
    def __init__(self):
        super(ORAZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("ORA zero page byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)


class ORAZeroPageX(object):
    """ORA Zero Page X instruction"""
    def __init__(self):
        super(ORAZeroPageX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page_x()
        print("ORA zero page X byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)


class ORAAbsolute(object):
    """ORA absolute instruction"""
    def __init__(self):
        super(ORAAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("ORA absolute byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)


class ORAAbsoluteX(object):
    """ORA absolute X instruction"""
    def __init__(self):
        super(ORAAbsoluteX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_x()
        print("ORA absolute x byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)


class ORAAbsoluteY(object):
    """ORA absolute Y instruction"""
    def __init__(self):
        super(ORAAbsoluteY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute_y()
        print("ORA absolute Y byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)


class ORAIndirectX(object):
    """ORA indirect X instruction"""
    def __init__(self):
        super(ORAIndirectX, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_x()
        print("ORA indirect X byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)


class ORAIndirectY(object):
    """ORA Indirect Y instruction"""
    def __init__(self):
        super(ORAIndirectY, self).__init__()

    def run(self, cpu):
        byte_r = cpu.indirect_y()
        print("ORA indirect Y byte read: %s" % hex(byte_r))
        print("ORA register A read: %s" % hex(cpu.a))
        cpu.ora(byte_r)