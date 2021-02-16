STA_ZEROPAGE_OPCODE = 0x85
STA_ZEROPAGEX_OPCODE = 0x95
STA_ABSOLUTE_OPCODE = 0x8d
STA_ABSOLUTEX_OPCODE = 0x9d
STA_ABSOLUTEY_OPCODE = 0x99
STA_INDIRECTX_OPCODE = 0x81
STA_INDIRECTY_OPCODE = 0x91


class STAZeroPage(object):
    """STA Zero Page instruction"""
    def __init__(self):
        super(STAZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        cpu.sta(address)


class STAZeroPageX(object):
    """STA Zero Page X instruction"""
    def __init__(self):
        super(STAZeroPageX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.x
        cpu.cycles += 1
        cpu.sta(address)


class STAAbsolute(object):
    """STA absolute instruction"""
    def __init__(self):
        super(STAAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.sta(address)
        print "Cycles"
        print cpu.cycles


class STAAbsoluteX(object):
    """STA absolute X instruction"""
    def __init__(self):
        super(STAAbsoluteX, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.x
        cpu.cycles += 1
        if address > 0xffff:
            address = address & 0xffff
        cpu.sta(address)


class STAAbsoluteY(object):
    """STA absolute X instruction"""
    def __init__(self):
        super(STAAbsoluteY, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.y
        if address > 0xffff:
            address = address & 0xffff
        cpu.cycles += 1
        print("Reading Absolute Y Address: %s" % hex(address))
        cpu.sta(address)


class STAIndirectX(object):
    """STA indirect X instruction"""
    def __init__(self):
        super(STAIndirectX, self).__init__()

    def run(self, cpu):
        zp_address = cpu.fetch_byte() + cpu.x
        zp_address = zp_address & 0xff
        cpu.cycles += 1
        address = cpu.read_word(zp_address)
        print("Reading Indirect X Address: %s" % hex(address))
        cpu.sta(address)


class STAIndirectY(object):
    """STA indirect Y instruction"""
    def __init__(self):
        super(STAIndirectY, self).__init__()

    def run(self, cpu):
        zp_address = cpu.fetch_byte()
        address = cpu.read_word(zp_address) + cpu.y
        if address > 0xffff:
            address = address & 0xffff
        cpu.cycles += 1
        print("Reading Indirect Y Address: %s" % hex(address))
        cpu.sta(address)