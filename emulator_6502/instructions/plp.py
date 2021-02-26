PLP_IMPLIED_OPCODE = 0x28


class PLPImplied(object):
    """PLP implied instruction"""
    def __init__(self):
        super(PLPImplied, self).__init__()

    def run(self, cpu):
        cpu.plp()