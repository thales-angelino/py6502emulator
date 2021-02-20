CPX_IMMEDIATE_OPCODE = 0xe0
CPX_ZEROPAGE_OPCODE = 0xe4
CPX_ABSOLUTE_OPCODE = 0xec


class CPXImmediate(object):
    def __init__(self):
        super(CPXImmediate, self).__init__()

    def run(self, cpu):
        byte_r = cpu.immediate()
        print("CPX memory byte read: %s" % hex(byte_r))
        print("CPX register X read: %s" % hex(cpu.x))
        print("CPX processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cpx(byte_r)


class CPXZeroPage(object):
    """CPX Zero Page instruction"""
    def __init__(self):
        super(CPXZeroPage, self).__init__()

    def run(self, cpu):
        byte_r = cpu.zero_page()
        print("CPX zero page byte read: %s" % hex(byte_r))
        print("CPX register X read: %s" % hex(cpu.x))
        print("CPX processor status Carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cpx(byte_r)


class CPXAbsolute(object):
    """CPX absolute instruction"""
    def __init__(self):
        super(CPXAbsolute, self).__init__()

    def run(self, cpu):
        byte_r = cpu.absolute()
        print("CPX absolute byte read: %s" % hex(byte_r))
        print("CPX register X read: %s" % hex(cpu.x))
        print("CPX processor status carry read: %s" % hex(cpu.processor_status['carry']))
        cpu.cpx(byte_r)