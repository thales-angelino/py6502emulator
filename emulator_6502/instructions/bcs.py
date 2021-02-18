BCS_RELATIVE_OPCODE = 0xb0


class BCSRelative(object):
    """BCS relative instruction"""
    def __init__(self):
        super(BCSRelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.bcs(offset)