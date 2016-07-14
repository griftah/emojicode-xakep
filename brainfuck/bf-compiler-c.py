# coding=utf-8

# Компилятор Brainfuck в Си

import sys, os

def compile(code, f=sys.stdout):
    indent = 1

    def w(line):
        f.write('\t'*indent)
        f.write(line)
        f.write('\n')

    w('''
#include <stdio.h>
int main(int argc, char **argv) {
    int tape[32768];
    int xc = 0;
''')

    for cmd in code:
        lines = []
        if cmd=='+':
            w('tape[xc]++;')
        elif cmd=='-':
            w('tape[xc]--;')
        elif cmd=='.':
            w('putchar(tape[xc]);')
        elif cmd=='>':
            w('xc++;')
        elif cmd=='<':
            w('xc--;')
        elif cmd=='[':
            w('while (tape[xc]) {')
            indent+=1
        elif cmd==']':
            indent-=1
            w('}')
    w('putchar(10); return 0; }')


if __name__=='__main__':
    if len(sys.argv)>1:
        filename = sys.argv[1]
        base_filename = filename.rsplit('.', 1)[0]
        new_filename = base_filename+'.c'
        f = open(new_filename, 'w')
        compile(open(sys.argv[1]).read(), f)
    else:
        compile("""++++++++[>+++++++++<-]>.<+++++[>++++++<-]>-.+++++++..+++.<
++++++++[>>++++<<-]>>.<<++++[>------<-]>.<++++[>++++++<-]>
.+++.------.--------.>+.""")
