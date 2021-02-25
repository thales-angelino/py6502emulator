NOP_IMPLIED_OPCODE = 0x00


class NOPImplied(object):
    """NOP implied instruction"""
    def __init__(self):
        super(NOPImplied, self).__init__()

    def run(self, cpu):
        cpu.nop()