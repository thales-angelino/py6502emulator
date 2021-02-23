JMP_ABSOLUTE_OPCODE = 0x4c
JMP_INDIRECT_OPCODE = 0x6c


class JMPAbsolute(object):
    """JMP absolute instruction"""
    def __init__(self):
        super(JMPAbsolute, self).__init__()

    def run(self, cpu):
        address = cpu.fetch_word()
        cpu.jmp(address)


class JMPIndirect(object):
    """JMP absolute X instruction"""
    def __init__(self):
        super(JMPIndirect, self).__init__()

    def run(self, cpu):
        value = cpu.indirect()
        cpu.jmp(value)