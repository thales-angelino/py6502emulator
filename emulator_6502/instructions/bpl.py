BPL_RELATIVE_OPCODE = 0x10


class BPLRelative(object):
    """BPL relative instruction"""
    def __init__(self):
        super(BPLRelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.bpl(offset)