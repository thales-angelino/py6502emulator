SEI_IMPLIED_OPCODE = 0x78


class SEIImplied(object):
    """SEI implied instruction"""
    def __init__(self):
        super(SEIImplied, self).__init__()

    def run(self, cpu):
        cpu.sei()