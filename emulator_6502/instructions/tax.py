TAX_IMPLIED_OPCODE = 0xaa


class TAXImplied(object):
    """TAX implied instruction"""
    def __init__(self):
        super(TAXImplied, self).__init__()

    def run(self, cpu):
        cpu.tax()