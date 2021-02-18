CLC_IMPLIED_OPCODE = 0x18


class CLCImplied(object):
    """CLC implied instruction"""
    def __init__(self):
        super(CLCImplied, self).__init__()

    def run(self, cpu):
        cpu.clc()