CPY_IMMEDIATE_OPCODE = 0xc0
CPY_ZEROPAGE_OPCODE = 0xc4
CPY_ABSOLUTE_OPCODE = 0xcc


class CPYImmediate(object):
    def __init__(self):
        super(CPYImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("CPY memory byte read: %s" % hex(byte_r))
        print("CPY register Y read: %s" % hex(cpu.y))
        print("CPY processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cpy(byte_r)


class CPYZeroPage(object):
    """CPY Zero Page instruction"""
    def __init__(self):
        super(CPYZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("CPY zero page byte read: %s" % hex(byte_r))
        print("CPY register Y read: %s" % hex(cpu.y))
        print("CPY processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cpy(byte_r)


class CPYAbsolute(object):
    """CPY absolute instruction"""
    def __init__(self):
        super(CPYAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("CPY absolute byte read: %s" % hex(byte_r))
        print("CPY register Y read: %s" % hex(cpu.y))
        print("CPY processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cpy(byte_r)