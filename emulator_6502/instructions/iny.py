INY_IMPLIED_OPCODE = 0xc8


class INYImplied(object):
    """INY implied instruction"""
    def __init__(self):
        super(INYImplied, self).__init__()
    def run(self, cpu):
        cpu.iny()