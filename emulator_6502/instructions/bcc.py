BCC_RELATIVE_OPCODE = 0x90


class BCCRelative(object):
    """BCC relative instruction"""
    def __init__(self):
        super(BCCRelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.bcc(offset)