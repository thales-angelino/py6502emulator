SEC_IMPLIED_OPCODE = 0x38


class SECImplied(object):
    """SEC implied instruction"""
    def __init__(self):
        super(SECImplied, self).__init__()

    def run(self, cpu):
        cpu.sec()