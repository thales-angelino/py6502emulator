from memory import Memory
from cpu import CPU

def main():
    memory = Memory()
    cpu = CPU(memory)
    cpu.reset()

    while True:
        cpu.print_cpu_stats()
        command = raw_input("Press (R) to reset, (N) to execute next "\
                            "instruction, (M_[NUMBER]) to print a memory"\
                            " page or (Q) to quit: ")

        if command.upper() == 'R':
            cpu.reset()

        elif command.upper() == 'N':
            cpu.execute(1)

        elif command.upper() == 'Q':
            print('Good bye...')
            exit(0)

        elif command.upper().startswith('M_'):
            page_number = int(command.split('_')[1])
            memory.dump_page(page_number)

        else:
            print('Command [%s] not recognized' % command)


if __name__ == '__main__':
    main()