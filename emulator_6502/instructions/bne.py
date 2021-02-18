BNE_RELATIVE_OPCODE = 0xd0


class BNERelative(object):
    """BMI relative instruction"""
    def __init__(self):
        super(BNERelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.bne(offset)