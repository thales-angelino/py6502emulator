TSX_IMPLIED_OPCODE = 0xba


class TSXImplied(object):
    """TSX implied instruction"""
    def __init__(self):
        super(TSXImplied, self).__init__()

    def run(self, cpu):
        cpu.tsx()