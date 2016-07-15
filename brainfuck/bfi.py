# coding=utf-8

# Порт brainfuck.c

import sys

def run(code):
    prog_len = len(code)
    tape = [0]

    xc = 0
    pc = 0
    l = 0
    while pc < prog_len:
        if code[pc]=='+':
            tape[xc]+=1
        elif code[pc]=='-':
            tape[xc]-=1
        elif code[pc]=='.':
            sys.stdout.write(chr(tape[xc]))
            sys.stdout.flush()
        elif code[pc]=='>':
            xc+=1
            if len(tape)<=xc:
                tape.append(0)
        elif code[pc]=='<':
            if xc>0:
                xc-=1
        elif code[pc]=='[':
            if tape[xc]==0:
                pc+=1
                while l>0 or code[pc]!=']':
                    if code[pc]=='[':
                        l+=1
                    elif code[pc]==']':
                        l-=1
                    pc+=1
        elif code[pc]==']':
            pc-=1
            while l>0 or code[pc]!='[':
                if code[pc]==']':
                    l+=1
                elif code[pc]=='[':
                    l-=1
                pc-=1
            pc-=1
        pc+=1

if __name__=='__main__':
    if len(sys.argv)>1:
        run(open(sys.argv[1]).read())
    else:
        run("""++++++++[>+++++++++<-]>.<+++++[>++++++<-]>-.+++++++..+++.<
++++++++[>>++++<<-]>>.<<++++[>------<-]>.<++++[>++++++<-]>
.+++.------.--------.>+.""")
