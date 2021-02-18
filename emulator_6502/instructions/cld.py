CLD_IMPLIED_OPCODE = 0xd8


class CLDImplied(object):
    """CLD implied instruction"""
    def __init__(self):
        super(CLDImplied, self).__init__()

    def run(self, cpu):
        cpu.cld()