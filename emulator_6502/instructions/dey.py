DEY_IMPLIED_OPCODE = 0x88


class DEYImplied(object):
    def __init__(self):
        super(DEYImplied, self).__init__()

    def run(self, cpu):
        cpu.dey()