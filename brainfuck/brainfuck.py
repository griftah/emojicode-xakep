#!/usr/bin/env python
# coding=utf-8

import sys

class Command(object):
    def __init__(self, char):
        self.char = char
        self.arg = 1

    def __repr__(self):
        return '%s:%d'%(self.char, self.arg)


class Brainfuck(object):
    def __init__(self, brainfuck=None, optimize=True):
        self.code = []
        if brainfuck:
            self.load(brainfuck, optimize)

    def load(self, brainfuck, optimize=True):
        braces = []
        self.code = code = [Command('')]
        for char in brainfuck:
            if char in '[]<>.,+-':
                if optimize and char in '<>+-' and char==code[-1].char:
                    code[-1].arg+=1
                else:
                    code.append(Command(char))
                    if char=='[':
                        braces.append(len(code)-1)
                    elif char==']':
                        left = braces.pop()
                        code[left].arg = len(code)-1
                        code[-1].arg = left

    def run(self):
        tape = [0]*30000
        xc = 0
        pc = 0
        code = self.code
        prog_len = len(code)
        while pc<prog_len:
            cmd = code[pc]
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
                sys.stdout.flush()
            elif cmd.char==']' and tape[xc]!=0:
                pc = cmd.arg
            elif cmd.char=='[' and tape[xc]==0:
                pc = cmd.arg
            pc+=1


if __name__=='__main__':
    import codecs

    optimize = False
    filename = None
    for arg in sys.argv[1:]:
        if arg=='-o' or arg=='-O':
            optimize = True
        else:
            filename = arg

    if filename:
        with codecs.open(filename, 'r', 'utf-8') as f:
            brainfuck = Brainfuck(f.read(), optimize)
        brainfuck.run()
    else:
        print '.\\brainfuck.py source.b'.ljust(40), 'исполнить source.b'
        print '.\\brainfuck.py -o source.b'.ljust(40), '-o включает оптимизацию'
