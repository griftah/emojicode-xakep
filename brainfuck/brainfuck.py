# coding=utf-8

import sys
import timeit

class Brainfuck(object):
    def __init__(self, brainfuck=None, optimize=True):
        if brainfuck:
            self.load(brainfuck, optimize)

    # загружает код из строки
    def load(self, brainfuck, optimize=True):
        chars = ['begin']
        args = [1]
        brackets = []
        for char in brainfuck:
            if char in '[]<>.,+-':
                if optimize and char in '<>+-' and char==chars[-1]:
                    args[-1]+=1
                else:
                    chars.append(char); args.append(1)
                    if char=='[':
                        brackets.append(len(chars)-1)
                    elif char==']':
                        left = brackets.pop()
                        args[left] = len(chars)-1
                        args[-1] = left
        chars.append('end'); args.append(1)
        self.code = zip(chars, args)

    # исполняет загруженное
    def run(self):
        code = self.code
        tape = [0]*30000
        pc = xc = 0
        prog_len = len(code)
        while pc<prog_len:
            char, arg = code[pc]
            if char=='+':
                tape[xc]+=arg
            elif char=='-':
                tape[xc]-=arg
            elif char=='>':
                xc+=arg
            elif char=='<':
                xc-=arg
            elif char=='.':
                sys.stdout.write(chr(tape[xc]))
                sys.stdout.flush()
            elif char==']' and tape[xc]:
                pc = arg
            elif char=='[' and tape[xc]==0:
                pc = arg
            pc+=1

    # Запустить и вернуть время работы
    def time(self):
        t0 = timeit.default_timer()
        self.run()
        return timeit.default_timer()-t0
