INX_IMPLIED_OPCODE = 0xe8


class INXImplied(object):
    """INX implied instruction"""
    def __init__(self):
        super(INXImplied, self).__init__()
    def run(self, cpu):
        cpu.inx()