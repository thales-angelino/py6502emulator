CLV_IMPLIED_OPCODE = 0xb8


class CLVImplied(object):
    """CLV implied instruction"""
    def __init__(self):
        super(CLVImplied, self).__init__()

    def run(self, cpu):
        cpu.clv()