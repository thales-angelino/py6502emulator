BEQ_RELATIVE_OPCODE = 0xf0


class BEQRelative(object):
    """BEQ relative instruction"""
    def __init__(self):
        super(BEQRelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.beq(offset)