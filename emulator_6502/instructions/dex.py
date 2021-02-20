DEX_IMPLIED_OPCODE = 0xca


class DEXImplied(object):
    def __init__(self):
        super(DEXImplied, self).__init__()

    def run(self, cpu):
        cpu.dex()