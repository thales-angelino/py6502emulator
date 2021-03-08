MEM_SIZE = 65536
PAGE_SIZE = 256
LINE_SIZE = 16

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
        print ("Address\t0x00\t0x01\t0x02\t0x03\t0x04\t0x05\t0x06\t0x07\t0x08"\
               "\t0x09\t0x0a\t0x0b\t0x0c\t0x0d\t0x0e\t0x0f")
        for i in range(start, end, LINE_SIZE):
            print ("%s:\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"\
                   "\t%s\t%s\t%s" % 
                   (hex(i), hex(self.memory[i]), hex(self.memory[i+1]),
                    hex(self.memory[i+2]), hex(self.memory[i+3]),
                    hex(self.memory[i+4]), hex(self.memory[i+5]),
                    hex(self.memory[i+6]), hex(self.memory[i+7]),
                    hex(self.memory[i+8]), hex(self.memory[i+9]),
                    hex(self.memory[i+10]), hex(self.memory[i+11]),
                    hex(self.memory[i+12]), hex(self.memory[i+13]),
                    hex(self.memory[i+14]), hex(self.memory[i+15])))