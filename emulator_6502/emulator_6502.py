from instructions import lda
from instructions import ldx
from instructions import ldy
from instructions import adc
from instructions import _and
from instructions import asl
from instructions import lsr
from instructions import rol
from instructions import ror
from instructions import eor
from instructions import ora
from instructions import sbc
from instructions import sta
from instructions import stx
from instructions import sty
from instructions import bcc
from instructions import bcs
from instructions import beq
from instructions import bmi
from instructions import bne
from instructions import bpl
from instructions import bvc
from instructions import bvs
from instructions import clc
from instructions import cli
from instructions import cld
from instructions import clv
from instructions import _cmp
from instructions import cpx
from instructions import cpy
from instructions import dey
from instructions import dex
from instructions import dec
from instructions import inc
from instructions import jmp
from instructions import sec
from instructions import sed
from instructions import sei
from instructions import pha
from instructions import pla
from instructions import tax


PAGE_SIZE = 256
MEM_SIZE = 65536
START_ADDRESS = 0x600

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
    ror.ROR_ACCUMULATOR_OPCODE: ror.RORAccumulator(),
    ror.ROR_ZEROPAGE_OPCODE: ror.RORZeroPage(),
    ror.ROR_ZEROPAGEX_OPCODE: ror.RORZeroPageX(),
    ror.ROR_ABSOLUTE_OPCODE: ror.RORAbsolute(),
    ror.ROR_ABSOLUTEX_OPCODE: ror.RORAbsoluteX(),
    eor.EOR_IMMEDIATE_OPCODE: eor.EORImmediate(),
    eor.EOR_ZEROPAGE_OPCODE: eor.EORZeroPage(),
    eor.EOR_ZEROPAGEX_OPCODE: eor.EORZeroPageX(),
    eor.EOR_ABSOLUTE_OPCODE: eor.EORAbsolute(),
    eor.EOR_ABSOLUTEX_OPCODE: eor.EORAbsoluteX(),
    eor.EOR_ABSOLUTEY_OPCODE: eor.EORAbsoluteY(),
    eor.EOR_INDIRECTX_OPCODE: eor.EORIndirectX(),
    eor.EOR_INDIRECTY_OPCODE: eor.EORIndirectY(),
    ora.ORA_IMMEDIATE_OPCODE: ora.ORAImmediate(),
    ora.ORA_ZEROPAGE_OPCODE: ora.ORAZeroPage(),
    ora.ORA_ZEROPAGEX_OPCODE: ora.ORAZeroPageX(),
    ora.ORA_ABSOLUTE_OPCODE: ora.ORAAbsolute(),
    ora.ORA_ABSOLUTEX_OPCODE: ora.ORAAbsoluteX(),
    ora.ORA_ABSOLUTEY_OPCODE: ora.ORAAbsoluteY(),
    ora.ORA_INDIRECTX_OPCODE: ora.ORAIndirectX(),
    ora.ORA_INDIRECTY_OPCODE: ora.ORAIndirectY(),
    sbc.SBC_IMMEDIATE_OPCODE: sbc.SBCImmediate(),
    sbc.SBC_ZEROPAGE_OPCODE: sbc.SBCZeroPage(),
    sbc.SBC_ZEROPAGEX_OPCODE: sbc.SBCZeroPageX(),
    sbc.SBC_ABSOLUTE_OPCODE: sbc.SBCAbsolute(),
    sbc.SBC_ABSOLUTEX_OPCODE: sbc.SBCAbsoluteX(),
    sbc.SBC_ABSOLUTEY_OPCODE: sbc.SBCAbsoluteY(),
    sbc.SBC_INDIRECTX_OPCODE: sbc.SBCIndirectX(),
    sbc.SBC_INDIRECTY_OPCODE: sbc.SBCIndirectY(),
    sta.STA_ZEROPAGE_OPCODE: sta.STAZeroPage(),
    sta.STA_ZEROPAGEX_OPCODE: sta.STAZeroPageX(),
    sta.STA_ABSOLUTE_OPCODE: sta.STAAbsolute(),
    sta.STA_ABSOLUTEX_OPCODE: sta.STAAbsoluteX(),
    sta.STA_ABSOLUTEY_OPCODE: sta.STAAbsoluteY(),
    sta.STA_INDIRECTX_OPCODE: sta.STAIndirectX(),
    sta.STA_INDIRECTY_OPCODE: sta.STAIndirectY(),
    stx.STX_ZEROPAGE_OPCODE: stx.STXZeroPage(),
    stx.STX_ZEROPAGEY_OPCODE: stx.STXZeroPageY(),
    stx.STX_ABSOLUTE_OPCODE: stx.STXAbsolute(),
    sty.STY_ZEROPAGE_OPCODE: sty.STYZeroPage(),
    sty.STY_ZEROPAGEX_OPCODE: sty.STYZeroPageX(),
    sty.STY_ABSOLUTE_OPCODE: sty.STYAbsolute(),
    bcc.BCC_RELATIVE_OPCODE: bcc.BCCRelative(),
    bcs.BCS_RELATIVE_OPCODE: bcs.BCSRelative(),
    beq.BEQ_RELATIVE_OPCODE: beq.BEQRelative(),
    bmi.BMI_RELATIVE_OPCODE: bmi.BMIRelative(),
    bne.BNE_RELATIVE_OPCODE: bne.BNERelative(),
    bpl.BPL_RELATIVE_OPCODE: bpl.BPLRelative(),
    bvc.BVC_RELATIVE_OPCODE: bvc.BVCRelative(),
    bvs.BVS_RELATIVE_OPCODE: bvs.BVSRelative(),
    clc.CLC_IMPLIED_OPCODE: clc.CLCImplied(),
    cld.CLD_IMPLIED_OPCODE: cld.CLDImplied(),
    cli.CLI_IMPLIED_OPCODE: cli.CLIImplied(),
    clv.CLV_IMPLIED_OPCODE: clv.CLVImplied(),
    _cmp.CMP_IMMEDIATE_OPCODE: _cmp.CMPImmediate(),
    _cmp.CMP_ZEROPAGE_OPCODE: _cmp.CMPZeroPage(),
    _cmp.CMP_ZEROPAGEX_OPCODE: _cmp.CMPZeroPageX(),
    _cmp.CMP_ABSOLUTE_OPCODE: _cmp.CMPAbsolute(),
    _cmp.CMP_ABSOLUTEX_OPCODE: _cmp.CMPAbsoluteX(),
    _cmp.CMP_ABSOLUTEY_OPCODE: _cmp.CMPAbsoluteY(),
    _cmp.CMP_INDIRECTX_OPCODE: _cmp.CMPIndirectX(),
    _cmp.CMP_INDIRECTY_OPCODE: _cmp.CMPIndirectY(),
    cpx.CPX_IMMEDIATE_OPCODE: cpx.CPXImmediate(),
    cpx.CPX_ZEROPAGE_OPCODE: cpx.CPXZeroPage(),
    cpx.CPX_ABSOLUTE_OPCODE: cpx.CPXAbsolute(),
    cpy.CPY_IMMEDIATE_OPCODE: cpy.CPYImmediate(),
    cpy.CPY_ZEROPAGE_OPCODE: cpy.CPYZeroPage(),
    cpy.CPY_ABSOLUTE_OPCODE: cpy.CPYAbsolute(),
    dex.DEX_IMPLIED_OPCODE: dex.DEXImplied(),
    dey.DEY_IMPLIED_OPCODE: dey.DEYImplied(),
    dec.DEC_ZEROPAGE_OPCODE: dec.DECZeroPage(),
    dec.DEC_ZEROPAGEX_OPCODE: dec.DECZeroPageX(),
    dec.DEC_ABSOLUTE_OPCODE: dec.DECAbsolute(),
    dec.DEC_ABSOLUTEX_OPCODE: dec.DECAbsoluteX(),
    inc.INC_ZEROPAGE_OPCODE: inc.INCZeroPage(),
    inc.INC_ZEROPAGEX_OPCODE: inc.INCZeroPageX(),
    inc.INC_ABSOLUTE_OPCODE: inc.INCAbsolute(),
    inc.INC_ABSOLUTEX_OPCODE: inc.INCAbsoluteX(),
    jmp.JMP_ABSOLUTE_OPCODE: jmp.JMPAbsolute(),
    jmp.JMP_INDIRECT_OPCODE: jmp.JMPIndirect(),
    sec.SEC_IMPLIED_OPCODE: sec.SECImplied(),
    sed.SED_IMPLIED_OPCODE: sed.SEDImplied(),
    sei.SEI_IMPLIED_OPCODE: sei.SEIImplied(),
    pha.PHA_IMPLIED_OPCODE: pha.PHAImplied(),
    pla.PLA_IMPLIED_OPCODE: pla.PLAImplied(),
    tax.TAX_IMPLIED_OPCODE: tax.TAXImplied(),
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

    def pha(self):
        self.push_byte_stack(self.a)

    def pla(self):
        self.a = self.pop_byte_stack()
        self.cycles += 1
        self.check_processor_flags_routine(self.a)

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

    def txs(self):
        self.x = self.stack_pointer
        self.cycles += 1
        self.check_processor_flags_routine(self.x)

    def txs(self):
        self.stack_pointer = self.x
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