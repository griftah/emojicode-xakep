# coding=utf-8

import sys

class Command(object):
    def __init__(self, char):
        self.char = char
        self.arg = 1

    def __repr__(self):
        return '%s:%d'%(self.char, self.arg)

class Program(object):
    def __init__(self, code=None):
        if code:
            self.load(code)

    def append(self, char):
        self.code.append(Command(char))
        if char=='[':
            self.braces.append(len(self.code)-1)
        elif char==']':
            left = self.braces.pop()
            self.code[left].arg = len(self.code)-1
            self.code[-1].arg = left

    def load(self, code):
        self.braces = []
        self.code = [Command('')]
        for char in code:
            if char in '[]<>.,+-':
                self.append(char)
        # print self.code

    def run(self):
        tape = [0]*30000
        xc = 0
        pc = 0
        prog_len = len(self.code)
        while pc<prog_len:
            cmd = self.code[pc]
            if cmd.char=='+':
                tape[xc]+=cmd.arg
            elif cmd.char=='-':
                tape[xc]-=cmd.arg
            elif cmd.char=='>':
                xc+=cmd.arg
            elif cmd.char=='<':
                xc-=cmd.arg
            elif cmd.char=='.':
                sys.stdout.write(chr(tape[xc]))
                # sys.stdout.flush()
            elif cmd.char==']' and tape[xc]!=0:
                pc = cmd.arg
            elif cmd.char=='[' and tape[xc]==0:
                pc = cmd.arg
            pc+=1

class Optimizer(Program):
    def append(self, char):
        if self.code[-1].char==char and char in '<>+-':
            self.code[-1].arg+=1
        else:
            super(self.__class__, self).append(char)

if __name__=='__main__':
    from timeit import timeit

    # program = Program(open(sys.argv[1]).read())
    program = Optimizer(open(sys.argv[1]).read())
    # print timeit(program.run, number=1)
    program.run()
