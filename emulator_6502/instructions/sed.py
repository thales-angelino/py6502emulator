SED_IMPLIED_OPCODE = 0xf8


class SEDImplied(object):
    """SED implied instruction"""
    def __init__(self):
        super(SEDImplied, self).__init__()

    def run(self, cpu):
        cpu.sed()