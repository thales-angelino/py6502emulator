JMP_ABSOLUTE_OPCODE = 0x4c
JMP_INDIRECT_OPCODE = 0x6c


'''
JMP is the only 6502 instruction to support indirection. The instruction contains a 16 bit address which identifies the location of the least significant byte of another 16 bit memory address which is the real target of the instruction.

For example if location $0120 contains $FC and location $0121 contains $BA then the instruction JMP ($0120) will cause the next instruction execution to occur at $BAFC (e.g. the contents of $0120 and $0121).

'''


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