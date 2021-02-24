PLA_IMPLIED_OPCODE = 0x68


class PLAImplied(object):
    """PLA implied instruction"""
    def __init__(self):
        super(PLAImplied, self).__init__()

    def run(self, cpu):
        cpu.pla()