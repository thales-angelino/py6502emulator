def check_processor_flags_routine(cpu):
    if (cpu.a == 0):
        cpu.processor_status['zero'] = 1
    if (cpu.a & 0b10000000) > 0:
        cpu.processor_status['negative'] = 1