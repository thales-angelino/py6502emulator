PHA_IMPLIED_OPCODE = 0x48


class PHAImplied(object):
    """PHA implied instruction"""
    def __init__(self):
        super(PHAImplied, self).__init__()

    def run(self, cpu):
        cpu.pha()