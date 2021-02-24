TAY_IMPLIED_OPCODE = 0xa8


class TAYImplied(object):
    """TAY implied instruction"""
    def __init__(self):
        super(TAYImplied, self).__init__()

    def run(self, cpu):
        cpu.tay()