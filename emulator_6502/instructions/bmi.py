BMI_RELATIVE_OPCODE = 0x30


class BMIRelative(object):
    """BMI relative instruction"""
    def __init__(self):
        super(BMIRelative, self).__init__()

    def run(self, cpu):
        offset = cpu.immediate()
        cpu.bmi(offset)