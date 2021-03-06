JSR_ABSOLUTE_OPCODE = 0x20


class JSRAbsolute(object):
    """JSR absolute instruction"""
    def __init__(self):
        super(JSRAbsolute, self).__init__()

    def run(self, cpu):
        cpu.jsr()