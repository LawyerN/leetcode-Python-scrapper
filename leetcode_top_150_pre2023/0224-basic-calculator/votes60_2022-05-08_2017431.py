class Tokenizer:
    def __init__(self, s):
        self.s = s
        self.pc = 0
        self.skip_whitespaces()
        
    def has_next(self):
        return self.pc < len(self.s)
        
    def next(self):
        self.pc += 1
        self.skip_whitespaces()
            
    def skip_whitespaces(self):
        while self.has_next() and self.current() == \' \':
            self.pc += 1
        
    def is_digit(self):
        return self.current().isdigit()
        
    def current(self):
        return self.s[self.pc]