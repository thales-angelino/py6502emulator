from checks import check_processor_flags_routine

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
        byte_r = cpu.fetch_byte()
        print("LDA immediate byte read: %s" % hex(byte_r))
        # TODO set the flags
        cpu.a = byte_r

        check_processor_flags_routine(cpu)


class LDAZeroPage(object):
    """LDA Zero Page instruction"""
    def __init__(self):
        super(LDAZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        print("LDA absolute Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDA zero page byte read: %s" % hex(byte_r))
        cpu.a = byte_r
        check_processor_flags_routine(cpu)


class LDAZeroPageX(object):
    """LDA Zero Page X instruction"""
    def __init__(self):
        super(LDAZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        # Truncate if the address is exceeded
        if address > 0xff:
            address = address & 0xff

        print("LDA absolute Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDA zero page byte read: %s" % hex(byte_r))
        cpu.a = byte_r

        check_processor_flags_routine(cpu)


class LDAAbsolute(object):
    """LDA Absolute instruction"""
    def __init__(self):
        super(LDAAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        print("LDA absolute Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDA absolute byte read: %s" % hex(byte_r))
        cpu.a = byte_r

        check_processor_flags_routine(cpu)


class LDAAbsoluteX(object):
    """LDA Absolute X instruction"""
    def __init__(self):
        super(LDAAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1
        print("LDA absolute X Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDA absolute X byte read: %s" % hex(byte_r))
        cpu.a = byte_r

        check_processor_flags_routine(cpu)


class LDAAbsoluteY(object):
    """LDA Absolute Y instruction"""
    def __init__(self):
        super(LDAAbsoluteY, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.y
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1
        print("LDA absolute Y Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDA absolute Y byte read: %s" % hex(byte_r))
        cpu.a = byte_r

        check_processor_flags_routine(cpu)


class LDAIndirectX(object):
    """LDA Indirect X instruction"""
    def __init__(self):
        super(LDAIndirectX, self).__init__()

    def run(self, cpu):
        zp_address = cpu.fetch_byte() + cpu.x
        zp_address = zp_address & 0xff
        cpu.cycles += 1
        address = cpu.read_word(zp_address)
        print("LDA indirect X Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDA indirect X byte read: %s" % hex(byte_r))
        cpu.a = byte_r

        check_processor_flags_routine(cpu)


class LDAIndirectY(object):
    """LDA Indirect Y instruction"""
    def __init__(self):
        super(LDAIndirectY, self).__init__()

    def run(self, cpu):
        zp_address = cpu.fetch_byte()
        address = cpu.read_word(zp_address) + cpu.y
        
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1

        print("LDA indirect y Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDA indirect y byte read: %s" % hex(byte_r))
        cpu.a = byte_r

        check_processor_flags_routine(cpu)