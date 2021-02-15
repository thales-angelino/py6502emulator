from instructions import lda, ldx, ldy, adc, _and, asl, lsr, rol

PAGE_SIZE = 256
MEM_SIZE = 65536
START_ADDRESS = 0xfffc

LSB_7BITS_ENABLED_MASK = 0x7f 
OVERFLOW_MASK = 0x80


OPCODES_TABLE = {
    lda.LDA_IMMEDIATE_OPCODE: lda.LDAImmediate(),
    lda.LDA_ZEROPAGE_OPCODE: lda.LDAZeroPage(),
    lda.LDA_ZEROPAGEX_OPCODE: lda.LDAZeroPageX(),
    lda.LDA_ABSOLUTE_OPCODE: lda.LDAAbsolute(),
    lda.LDA_ABSOLUTEX_OPCODE: lda.LDAAbsoluteX(),
    lda.LDA_ABSOLUTEY_OPCODE: lda.LDAAbsoluteY(),
    lda.LDA_INDIRECTX_OPCODE: lda.LDAIndirectX(),
    lda.LDA_INDIRECTY_OPCODE: lda.LDAIndirectY(),
    ldx.LDX_IMMEDIATE_OPCODE: ldx.LDXImmediate(),
    ldx.LDX_ZEROPAGE_OPCODE: ldx.LDXZeroPage(),
    ldx.LDX_ZEROPAGEY_OPCODE: ldx.LDXZeroPageY(),
    ldx.LDX_ABSOLUTE_OPCODE: ldx.LDXAbsolute(),
    ldx.LDX_ABSOLUTEY_OPCODE: ldx.LDXAbsoluteY(),
    ldy.LDY_IMMEDIATE_OPCODE: ldy.LDYImmediate(),
    ldy.LDY_ZEROPAGE_OPCODE: ldy.LDYZeroPage(),
    ldy.LDY_ZEROPAGEX_OPCODE: ldy.LDYZeroPageX(),
    ldy.LDY_ABSOLUTE_OPCODE: ldy.LDYAbsolute(),
    ldy.LDY_ABSOLUTEX_OPCODE: ldy.LDYAbsoluteX(),
    adc.ADC_IMMEDIATE_OPCODE: adc.ADCImmediate(),
    adc.ADC_ZEROPAGE_OPCODE: adc.ADCZeroPage(),
    adc.ADC_ZEROPAGEX_OPCODE: adc.ADCZeroPageX(),
    adc.ADC_ABSOLUTE_OPCODE: adc.ADCAbsolute(),
    adc.ADC_ABSOLUTEX_OPCODE: adc.ADCAbsoluteX(),
    adc.ADC_ABSOLUTEY_OPCODE: adc.ADCAbsoluteY(),
    adc.ADC_INDIRECTX_OPCODE: adc.ADCIndirectX(),
    adc.ADC_INDIRECTY_OPCODE: adc.ADCIndirectY(),
    _and.AND_IMMEDIATE_OPCODE: _and.ANDImmediate(),
    _and.AND_ZEROPAGE_OPCODE: _and.ANDZeroPage(),
    _and.AND_ZEROPAGEX_OPCODE: _and.ANDZeroPageX(),
    _and.AND_ABSOLUTE_OPCODE: _and.ANDAbsolute(),
    _and.AND_ABSOLUTEX_OPCODE: _and.ANDAbsoluteX(),
    _and.AND_ABSOLUTEY_OPCODE: _and.ANDAbsoluteY(),
    _and.AND_INDIRECTX_OPCODE: _and.ANDIndirectX(),
    _and.AND_INDIRECTY_OPCODE: _and.ANDIndirectY(),
    asl.ASL_ACCUMULATOR_OPCODE: asl.ASLAccumulator(),
    asl.ASL_ZEROPAGE_OPCODE: asl.ASLZeroPage(),
    asl.ASL_ZEROPAGEX_OPCODE: asl.ASLZeroPageX(),
    asl.ASL_ABSOLUTE_OPCODE: asl.ASLAbsolute(),
    asl.ASL_ABSOLUTEX_OPCODE: asl.ASLAbsoluteX(),
    lsr.LSR_ACCUMULATOR_OPCODE: lsr.LSRAccumulator(),
    lsr.LSR_ZEROPAGE_OPCODE: lsr.LSRZeroPage(),
    lsr.LSR_ZEROPAGEX_OPCODE: lsr.LSRZeroPageX(),
    lsr.LSR_ABSOLUTE_OPCODE: lsr.LSRAbsolute(),
    lsr.LSR_ABSOLUTEX_OPCODE: lsr.LSRAbsoluteX(),
    rol.ROL_ACCUMULATOR_OPCODE: rol.ROLAccumulator(),
    rol.ROL_ZEROPAGE_OPCODE: rol.ROLZeroPage(),
    rol.ROL_ZEROPAGEX_OPCODE: rol.ROLZeroPageX(),
    rol.ROL_ABSOLUTE_OPCODE: rol.ROLAbsolute(),
    rol.ROL_ABSOLUTEX_OPCODE: rol.ROLAbsoluteX(),
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
    """6502 CPU"""
    def __init__(self, memory):
        super(CPU, self).__init__()
        self.memory = memory
        """
        The program counter is a 16 bit register which points to the next
        instruction to be executed.
        The value of program counter is modified automatically as instructions
        are executed.

        The value of the program counter can be modified by executing a jump, 
        a relative branch or a subroutine call to another memory address or by
        returning from a subroutine or interrupt.
        """
        self.program_counter = 0x00
        """
        The processor supports a 256 byte stack located between $0100 and $01FF. 
        The stack pointer is an 8 bit register and holds the low 8 bits of the
        next free location on the stack.
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

    def write_byte(self, address, value):
        self.memory.memory[address] = value
        self.cycles += 1
        return value

    def check_processor_flags_routine(self, register):
        if (register == 0):
            self.processor_status['zero'] = 1
        if (register & 0b10000000) > 0:
            self.processor_status['negative'] = 1

    def load_register_a(self, value):
        self.a = value
        self.check_processor_flags_routine(self.a)

    def load_register_x(self, value):
        self.x = value
        self.check_processor_flags_routine(self.x)

    def load_register_y(self, value):
        self.y = value
        self.check_processor_flags_routine(self.y)

    def adc(self, value):
        """
        http://www.righto.com/2012/12/the-6502-overflow-flag-explained.html

        It should also check the processor status decimal flag.
        """
        result = self.a + value + self.processor_status['carry']
        c6 = ((self.a & LSB_7BITS_ENABLED_MASK) +
              (value & LSB_7BITS_ENABLED_MASK) + 
              self.processor_status['carry']) & OVERFLOW_MASK
        if c6:
            c6 = 1
        self.a = (result & 0xff)

        self.processor_status['carry'] = 0
        if result > 0xff:
            self.processor_status['carry'] = 1
        
        if c6 ^ self.processor_status['carry']:
            self.processor_status['overflow'] = 1

        self.check_processor_flags_routine(self.a)

    def _and(self, value):
        result = (self.a & value)
        self.a = result
        self.check_processor_flags_routine(self.a)

    def asl(self, address=None):
        if address is None:
            self.cycles += 1
            # Perform the operation on the A register
            if (self.a & 0b10000000) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = ((self.a << 1) & 0xff)
            self.a = result
            self.check_processor_flags_routine(self.a)
        else:
            value = self.read_byte(address)
            self.cycles += 1
            if (value & 0b10000000) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = ((value << 1) & 0xff)
            self.write_byte(address, result)
            self.check_processor_flags_routine(result)

    def lsr(self, address=None):
        if address is None:
            self.cycles += 1
            # Perform the operation on the A register
            if (self.a & 0b00000001) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = ((self.a >> 1) & 0xff)
            self.a = result
            self.check_processor_flags_routine(self.a)
        else:
            value = self.read_byte(address)
            self.cycles += 1
            if (value & 0b00000001) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = ((value >> 1) & 0xff)
            self.write_byte(address, result)
            self.check_processor_flags_routine(result)

    def rol(self, address=None):
        carry = self.processor_status['carry']
        if address is None:
            self.cycles += 1
            # Perform the operation on the A register
            if (self.a & 0b10000000) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = ((self.a << 1) & 0xff) + carry
            self.a = result
            self.check_processor_flags_routine(self.a)
        else:
            value = self.read_byte(address)
            self.cycles += 1
            if (value & 0b10000000) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = ((value << 1) & 0xff) + carry
            self.write_byte(address, result)
            self.check_processor_flags_routine(result)


    # Memory access methods

    def immediate(self):
        return self.fetch_byte()

    def zero_page(self):
        address = self.fetch_byte()
        print("Reading From Zero Page Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

    def zero_page_x(self):
        address = self.fetch_byte() + self.x
        self.cycles += 1
        # Truncate if the address is exceeded
        if address > 0xff:
            address = address & 0xff
        print("Reading Zero Page X Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

    def zero_page_y(self):
        address = self.fetch_byte() + self.y
        self.cycles += 1
        # Truncate if the address is exceeded
        if address > 0xff:
            address = address & 0xff
        print("Reading Zero Page Y Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

    def absolute(self):
        address = self.fetch_word()
        print("Reading Absolute Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

    def absolute_x(self):
        address = self.fetch_word() + self.x
        if address > 0xffff:
            address = address & 0xffff
            self.cycles += 1
        print("Reading Absolute X Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

    def absolute_y(self):
        address = self.fetch_word() + self.y
        if address > 0xffff:
            address = address & 0xffff
            self.cycles += 1
        print("Reading Absolute Y Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

    def indirect_x(self):
        zp_address = self.fetch_byte() + self.x
        zp_address = zp_address & 0xff
        self.cycles += 1
        address = self.read_word(zp_address)
        print("Reading Indirect X Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

    def indirect_y(self):
        zp_address = self.fetch_byte()
        address = self.read_word(zp_address) + self.y
        if address > 0xffff:
            address = address & 0xffff
            self.cycles += 1
        print("Reading Indirect Y Address: %s" % hex(address))
        value = self.read_byte(address)
        return value

def main():
    memory = Memory()
    cpu = CPU(memory)
    cpu.reset()
    cpu.execute(1)


if __name__ == '__main__':
    main()