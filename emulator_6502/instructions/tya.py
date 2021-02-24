TYA_IMPLIED_OPCODE = 0x98


class TYAImplied(object):
    """TYA implied instruction"""
    def __init__(self):
        super(TYAImplied, self).__init__()

    def run(self, cpu):
        cpu.tya()