CLI_IMPLIED_OPCODE = 0x58


class CLIImplied(object):
    """CLI implied instruction"""
    def __init__(self):
        super(CLIImplied, self).__init__()

    def run(self, cpu):
        cpu.cli()