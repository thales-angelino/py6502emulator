from instructions import OPCODES_TABLE

PAGE_SIZE = 256
MEM_SIZE = 65536
START_ADDRESS = 0x600
INTERRUPT_VECTOR = 0xfffe
LSB_7BITS_ENABLED_MASK = 0x7f 
OVERFLOW_MASK = 0x80

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
        self.program_counter = START_ADDRESS
        self.stack_pointer = 0xff
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
        self.program_counter = START_ADDRESS
        self.stack_pointer = 0xff
        self.cycles = 0

    def execute(self, n_opcodes):
        while n_opcodes > 0:
            print "n opcodes: %d" % n_opcodes
            opcode = self.fetch_byte()
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

    def sbc(self, value):
        # TODO implement decimal mode operation
        assert self.processor_status['decimal_mode'] is 0
        value_1comp = value ^ 0xff
        self.adc(value_1comp)

    def bcc(self, offset):
        if self.processor_status['carry'] is 0:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def bcs(self, offset):
        if self.processor_status['carry'] is 1:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def beq(self, offset):
        if self.processor_status['zero'] is 1:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def bmi(self, offset):
        if self.processor_status['negative'] is 1:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def bne(self, offset):
        if self.processor_status['zero'] is 0:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def bpl(self, offset):
        if self.processor_status['negative'] is 0:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def bvc(self, offset):
        if self.processor_status['overflow'] is 0:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def bvs(self, offset):
        if self.processor_status['overflow'] is 1:
            # Branch succeeded
            self.cycles += 1
            self.branch(offset)

    def sec(self):
        self.cycles += 1
        self.processor_status['carry'] = 1

    def sed(self):
        self.cycles += 1
        self.processor_status['decimal_mode'] = 1

    def sei(self):
        self.cycles += 1
        self.processor_status['interrupt_disable'] = 1

    def clc(self):
        self.cycles += 1
        self.processor_status['carry'] = 0

    def cld(self):
        self.cycles += 1
        self.processor_status['decimal_mode'] = 0

    def cli(self):
        self.cycles += 1
        self.processor_status['interrupt_disable'] = 0

    def clv(self):
        self.cycles += 1
        self.processor_status['overflow'] = 0
        
    def branch(self, offset):
        old_pc = self.program_counter
        if (offset & 0b10000000) > 0:
            self.program_counter -= (offset ^ 0xff)
        else:
            self.program_counter += offset
        page_changed = (self.program_counter >> 8) != (old_pc >> 8)
        if page_changed:
            # Memory page changed
            self.cycles += 1

    def cmp(self, value):
        result = self.a - value

        if (self.a >= value):
            self.processor_status['carry'] = 1
        if (self.a == value):
            self.processor_status['zero'] = 1
        if (result & 0b10000000) > 0:
            self.processor_status['negative'] = 1

    def cpx(self, value):
        result = self.x - value

        if (self.x >= value):
            self.processor_status['carry'] = 1
        if (self.x == value):
            self.processor_status['zero'] = 1
        if (result & 0b10000000) > 0:
            self.processor_status['negative'] = 1

    def cpy(self, value):
        result = self.y - value

        if (self.y >= value):
            self.processor_status['carry'] = 1
        if (self.y == value):
            self.processor_status['zero'] = 1
        if (result & 0b10000000) > 0:
            self.processor_status['negative'] = 1

    def increment(self, value):
        self.cycles += 1
        result = (value + 1) & 0xff
        return result

    def inx(self):
        self.cycles += 1
        self.x = (self.x + 1) & 0xff
        self.check_processor_flags_routine(self.x)

    def iny(self):
        self.cycles += 1
        self.y = (self.y + 1) & 0xff
        self.check_processor_flags_routine(self.y)
    
    def inc(self, address):    
        value = self.read_byte(address)
        result = self.increment(value)
        self.write_byte(address, result)
        self.check_processor_flags_routine(result)

    def decrement(self, value):
        self.cycles += 1
        result = value
        if value == 0x00:
            result = 0xff
        else:
            result -= 1
        return result

    def dec(self, address):    
        value = self.read_byte(address)
        result = self.decrement(value)
        self.write_byte(address, result)
        self.check_processor_flags_routine(result)

    def dey(self):
        self.y = self.decrement(self.y)
        self.check_processor_flags_routine(self.y)

    def dex(self):
        self.x = self.decrement(self.x)
        self.check_processor_flags_routine(self.x)

    def adc(self, value):
        """
        http://www.righto.com/2012/12/the-6502-overflow-flag-explained.html

        It should also check the processor status decimal_mode flag.
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

    def eor(self, value):
        '''Exclusive OR'''
        result = (self.a ^ value)
        self.a = result
        self.check_processor_flags_routine(self.a)

    def ora(self, value):
        '''Inclusive OR'''
        result = (self.a | value)
        self.a = result
        self.check_processor_flags_routine(self.a)

    def sta(self, address):
        self.write_byte(address, self.a)

    def stx(self, address):
        self.write_byte(address, self.x)

    def sty(self, address):
        self.write_byte(address, self.y)

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

    def ror(self, address=None):
        carry = 0b00000000
        if self.processor_status['carry'] is 1:
            carry = 0b10000000
        if address is None:
            self.cycles += 1
            # Perform the operation on the A register
            if (self.a & 0b00000001) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = (((self.a >> 1) & 0xff) | carry)
            self.a = result
            self.check_processor_flags_routine(self.a)
        else:
            value = self.read_byte(address)
            self.cycles += 1
            if (value & 0b00000001) > 0:
                self.processor_status['carry'] = 1
            else:
                self.processor_status['carry'] = 0
            result = (((value >> 1) & 0xff) | carry)
            self.write_byte(address, result)
            self.check_processor_flags_routine(result)

    def jmp(self, address):
        self.program_counter = address

    def push_byte_stack(self, value):
        self.cycles += 2
        stack_address = 0x100 + self.stack_pointer
        self.memory.memory[stack_address] = value
        self.stack_pointer -= 1

    def pop_byte_stack(self):
        self.cycles += 2
        self.stack_pointer += 1
        stack_address = 0x100 + self.stack_pointer
        value = self.memory.memory[stack_address]
        self.memory.memory[stack_address] = 0x00
        return value

    def push_word_stack(self, word):
        self.cycles += 2
        msb = (word >> 8) & 0xff
        lsb = word & 0xff
        stack_address = 0x100 + self.stack_pointer
        self.memory.memory[stack_address] = msb
        self.stack_pointer -= 1
        stack_address = 0x100 + self.stack_pointer
        self.memory.memory[stack_address] = lsb
        self.stack_pointer -= 1

    def pop_word_stack(self):
        self.cycles += 2
        self.stack_pointer += 1
        stack_address = 0x100 + self.stack_pointer
        lsb = self.memory.memory[stack_address]
        self.memory.memory[stack_address] = 0x00
        self.stack_pointer += 1
        stack_address = 0x100 + self.stack_pointer
        msb = self.memory.memory[stack_address]
        self.memory.memory[stack_address] = 0x00
        word = (msb << 8) | lsb
        return word

    def jsr(self):
        self.cycles += 1
        address = self.fetch_word()
        old_pc = self.program_counter - 1
        self.push_word_stack(old_pc)
        self.program_counter = address

    def rts(self):
        stacked_pc = self.pop_word_stack()
        self.cycles += 3
        self.program_counter = stacked_pc + 1

    def brk(self):
        self.push_word_stack(self.program_counter)
        self.php()
        self.program_counter = self.read_word(INTERRUPT_VECTOR)
        self.processor_status['break_command'] = 1

    def rti(self):
        self.plp()
        self.program_counter = self.pop_word_stack()

    def pha(self):
        self.push_byte_stack(self.a)

    def pla(self):
        self.a = self.pop_byte_stack()
        self.cycles += 1
        self.check_processor_flags_routine(self.a)

    def php(self):
        value = 0x00
        if self.processor_status['carry'] > 0:
            value += 0b00000001

        if self.processor_status['zero'] > 0:
            value += 0b00000010

        if self.processor_status['interrupt_disable'] > 0:
            value += 0b00000100

        if self.processor_status['decimal_mode'] > 0:
            value += 0b00001000

        if self.processor_status['break_command'] > 0:
            value += 0b00010000

        if self.processor_status['overflow'] > 0:
            value += 0b01000000

        if self.processor_status['negative'] > 0:
            value += 0b10000000

        self.push_byte_stack(value)

    def plp(self):
        value = self.pop_byte_stack()

        if (value & 0b00000001) > 0:
            self.processor_status['carry'] = 1
        else:
            self.processor_status['carry'] = 0

        if (value & 0b00000010) > 0:
            self.processor_status['zero'] = 1
        else:
            self.processor_status['zero'] = 0

        if (value & 0b00000100) > 0:
            self.processor_status['interrupt_disable'] = 1
        else:
            self.processor_status['interrupt_disable'] = 0

        if (value & 0b00001000) > 0:
            self.processor_status['decimal_mode'] = 1
        else:
            self.processor_status['decimal_mode'] = 0

        if (value & 0b00010000) > 0:
            self.processor_status['break_command'] = 1
        else:
            self.processor_status['break_command'] = 0

        if (value & 0b01000000) > 0:
            self.processor_status['overflow'] = 1
        else:
            self.processor_status['overflow'] = 0

        if (value & 0b10000000) > 0:
            self.processor_status['negative'] = 1
        else:
            self.processor_status['negative'] = 0

        self.cycles += 1

    def tax(self):
        self.x = self.a
        self.cycles += 1
        self.check_processor_flags_routine(self.x)

    def tay(self):
        self.y = self.a
        self.cycles += 1
        self.check_processor_flags_routine(self.y)

    def txa(self):
        self.a = self.x
        self.cycles += 1
        self.check_processor_flags_routine(self.a)

    def tya(self):
        self.a = self.y
        self.cycles += 1
        self.check_processor_flags_routine(self.a)

    def tsx(self):
        self.x = self.stack_pointer
        self.cycles += 1
        self.check_processor_flags_routine(self.x)

    def txs(self):
        self.stack_pointer = self.x
        self.cycles += 1

    def nop(self):
        self.cycles += 1

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

    def indirect(self):
        address = self.fetch_word()
        print("Reading Indirect Address: %s" % hex(address))
        value = self.read_word(address)
        print("Value: %s" % hex(value))
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