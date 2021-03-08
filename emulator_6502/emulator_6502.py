from memory import Memory
from cpu import CPU
import argparse

START_ADDRESS = 0x600
INTERRUPT_VECTOR = 0xfffe

def main():
    parser = argparse.ArgumentParser(description='Emulates the 6502 chip.')
    parser.add_argument('--hex_file', required=True, help='Path to the hex file to be loaded in memory')
    parser.add_argument('--verbose', '-v', action='count', default=0)

    args = parser.parse_args()

    memory = Memory()
    cpu = CPU(memory)
    cpu.reset()
    memory.load_file(args.hex_file)

    while True:
        cpu.print_cpu_stats()
        command = raw_input("\nPress (R) to reset, (N) to execute next "\
                            "instruction, (M_[NUMBER]) to print a memory"\
                            " page or (Q) to quit: ")

        if command.upper() == 'R':
            cpu.reset()
            memory.load_file(args.hex_file)

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