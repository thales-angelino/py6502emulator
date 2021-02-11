from checks import check_processor_flags_routine


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
        byte_r = cpu.fetch_byte()
        print("LDX immediate byte read: %s" % hex(byte_r))
        # TODO set the flags
        cpu.x = byte_r
        check_processor_flags_routine(cpu)


class LDXZeroPage(object):
    """LDX Zero Page instruction"""
    def __init__(self):
        super(LDXZeroPage, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte()
        print("LDX zero page Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDX zero page byte read: %s" % hex(byte_r))
        cpu.x = byte_r
        check_processor_flags_routine(cpu)


class LDXZeroPageY(object):
    """LDX Zero Page Y instruction"""
    def __init__(self):
        super(LDXZeroPageY, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_byte() + cpu.y
        cpu.cycles += 1
        # Truncate if the address is exceeded
        if address > 0xff:
            address = address & 0xff

        print("LDX zero page Y Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDX zero page Y byte read: %s" % hex(byte_r))
        cpu.x = byte_r
        check_processor_flags_routine(cpu)


class LDXAbsolute(object):
    """LDX Absolute instruction"""
    def __init__(self):
        super(LDXAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        print("LDX absolute Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDX absolute byte read: %s" % hex(byte_r))
        cpu.x = byte_r
        check_processor_flags_routine(cpu)


class LDXAbsoluteY(object):
    """LDX Absolute Y instruction"""
    def __init__(self):
        super(LDXAbsoluteY, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word() + cpu.y
        if address > 0xffff:
            address = address & 0xffff
            cpu.cycles += 1
        print("LDX absolute Y Address: %s" % hex(address))
        byte_r = cpu.read_byte(address)
        print("LDX absolute Y byte read: %s" % hex(byte_r))
        cpu.x = byte_r
        check_processor_flags_routine(cpu)