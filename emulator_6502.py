from instructions import lda

PAGE_SIZE = 256
MEM_SIZE = 65536
START_ADDRESS = 0xfffc

OPCODES_TABLE = {
    lda.LDA_IMMEDIATE_OPCODE: lda.LDAImmediate(),
    lda.LDA_ZEROPAGE_OPCODE: lda.LDAZeroPage(),
    lda.LDA_ZEROPAGEX_OPCODE: lda.LDAZeroPageX(),
    lda.LDA_ABSOLUTE_OPCODE: lda.LDAAbsolute(),
    lda.LDA_ABSOLUTEX_OPCODE: lda.LDAAbsoluteX(),
    lda.LDA_ABSOLUTEY_OPCODE: lda.LDAAbsoluteY(),
    lda.LDA_INDIRECTX_OPCODE: lda.LDAIndirectX(),
    lda.LDA_INDIRECTY_OPCODE: lda.LDAIndirectY(),
}

class Memory(object):
    """Memory class is able to hold incredible 64 kb"""
    def __init__(self):
        super(Memory, self).__init__()
        self.memory = [0x00] * MEM_SIZE

    def dump_mem(self):
        for i in range(0, len(self.memory), PAGE_SIZE):
            print ("Page %d: %s" % (int(i/PAGE_SIZE), 
                   self.memory[i:i+PAGE_SIZE]))

    def dump_page(self, page_number=0):
        assert (page_number < PAGE_SIZE)

        start = page_number * PAGE_SIZE
        end = start + PAGE_SIZE
        for i in range(start, end):
            print ("Address %s: %s" % (hex(i), hex(self.memory[i])))

class CPU(object):
    """CPU"""
    def __init__(self, memory):
        super(CPU, self).__init__()
        self.memory = memory
        """
        The program counter is a 16 bit register which points to the next instruction to be executed.
        The value of program counter is modified automatically as instructions are executed.

        The value of the program counter can be modified by executing a jump, a relative branch or
        a subroutine call to another memory address or by returning from a subroutine or interrupt.
        """
        self.program_counter = 0x00
        """
        The processor supports a 256 byte stack located between $0100 and $01FF. 
        The stack pointer is an 8 bit register and holds the low 8 bits of the next free location on the stack.
        The location of the stack is fixed and cannot be moved.

        Pushing bytes to the stack causes the stack pointer to be decremented.
        Conversely pulling bytes causes it to be incremented.

        The CPU does not detect if the stack is overflowed by excessive pushing or 
        pulling operations and will most likely result in the program crashing.
        """
        self.stack_pointer = 0x00

        """
        Registers A, X and Y
        """
        self.a = 0
        self.x = 0
        self.y = 0

        self.processor_status = {
            'carry': 0,
            'zero': 0,
            'interrupt_disable': 0,
            'decimal_mode': 0,
            'break_command': 0,
            'overflow': 0,
            'negative': 0
        }

        self.cycles = 0

    def reset(self):
        self.program_counter = 0xfffc
        self.stack_pointer = 0x0100
        self.cycles = 0

    def execute(self, n_opcodes):
        while n_opcodes > 0:
            print "n opcodes: %d" % n_opcodes
            opcode = self.fetch_byte()
            print (hex(self.program_counter))
            self.run_opcode(opcode)
            n_opcodes -= 1

        print('Execution stopped')

    def run_opcode(self, opcode):
        instruction = OPCODES_TABLE.get(opcode)
        if instruction is not None:
            print(instruction)
            instruction.run(self)
        else:
            print("Instruction not found: %s" % hex(opcode))
            exit(1)

    def fetch_byte(self):
        value = self.memory.memory[self.program_counter]
        self.program_counter += 1
        self.cycles += 1
        return value

    def fetch_word(self):
        lsb = self.fetch_byte()
        msb = self.fetch_byte()
        word = (msb << 8) | lsb
        return word

    def read_byte(self, address):
        value = self.memory.memory[address]
        self.cycles += 1
        return value

    def read_word(self, address):
        lsb = self.read_byte(address)
        msb = self.read_byte(address+1)
        word = (msb << 8) | lsb
        return word

def main():
    memory = Memory()
    cpu = CPU(memory)
    cpu.reset()
    cpu.execute(1)

'''
m6502::Word m6502::CPU::AddrIndirectX( s32& Cycles, const Mem& memory )
{
    Byte ZPAddress = FetchByte( Cycles, memory );
    ZPAddress += X;
    Cycles--;
    Word EffectiveAddr = ReadWord( Cycles, ZPAddress, memory );
    return EffectiveAddr;
}

m6502::Word m6502::CPU::AddrIndirectY( s32& Cycles, const Mem& memory )
{
    Byte ZPAddress = FetchByte( Cycles, memory );
    Word EffectiveAddr = ReadWord( Cycles, ZPAddress, memory );
    Word EffectiveAddrY = EffectiveAddr + Y;
    const bool CrossedPageBoundary = (EffectiveAddr ^ EffectiveAddrY) >> 8;
    if ( CrossedPageBoundary )
    {
        Cycles--;
    }
    return EffectiveAddrY;
}
'''

if __name__ == '__main__':
    main()