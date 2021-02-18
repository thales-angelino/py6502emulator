BVC_RELATIVE_OPCODE = 0x50


class BVCRelative(object):
    """BVC relative instruction"""
    def __init__(self):
        super(BVCRelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.bvc(offset)