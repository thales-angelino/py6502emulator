BVS_RELATIVE_OPCODE = 0x70


class BVSRelative(object):
    """BVS relative instruction"""
    def __init__(self):
        super(BVSRelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.bvs(offset)