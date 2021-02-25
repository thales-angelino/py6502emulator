TXS_IMPLIED_OPCODE = 0x9a


class TXSImplied(object):
    """TXS implied instruction"""
    def __init__(self):
        super(TXSImplied, self).__init__()

    def run(self, cpu):
        cpu.txs()