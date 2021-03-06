RTS_IMPLIED_OPCODE = 0x60


class RTSImplied(object):
    """RTS implied instruction"""
    def __init__(self):
        super(RTSImplied, self).__init__()

    def run(self, cpu):
        cpu.rts()