PHP_IMPLIED_OPCODE = 0x08


class PHPImplied(object):
    """PHP implied instruction"""
    def __init__(self):
        super(PHPImplied, self).__init__()

    def run(self, cpu):
        cpu.php()