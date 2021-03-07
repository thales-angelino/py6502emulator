BRK_IMPLIED_OPCODE = 0x00


class BRKImplied(object):
    """BRK implied instruction"""
    def __init__(self):
        super(BRKImplied, self).__init__()

    def run(self, cpu):
        cpu.brk()