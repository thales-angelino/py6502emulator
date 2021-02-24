TXA_IMPLIED_OPCODE = 0x8a


class TXAImplied(object):
    """TXA implied instruction"""
    def __init__(self):
        super(TXAImplied, self).__init__()

    def run(self, cpu):
        cpu.txa()