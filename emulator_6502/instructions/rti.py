RTI_IMPLIED_OPCODE = 0x40


class RTIImplied(object):
    """RTI implied instruction"""
    def __init__(self):
        super(RTIImplied, self).__init__()

    def run(self, cpu):
        cpu.rti()