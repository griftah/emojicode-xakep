
# coding=utf-8
# Создано bf-compiler.py из исходника на Brainfuck.
import sys
tape = [0]*32000
xc = 0

tape[xc]+=4
while tape[xc]:
    xc+=1
    tape[xc]+=5
    xc-=1
    tape[xc]-=1
xc+=1
while tape[xc]:
    xc-=1
    tape[xc]+=5
    xc+=1
    tape[xc]-=1
tape[xc]+=1
xc-=1
tape[xc]+=1
while tape[xc]:
    xc+=1
    while tape[xc]:
        xc+=1
        tape[xc]+=1
        xc+=1
        tape[xc]+=1
        xc-=2
        tape[xc]-=1
    tape[xc]+=2
    xc+=2
    while tape[xc]:
        xc-=2
        tape[xc]+=1
        xc+=2
        tape[xc]-=1
    xc+=3
    while tape[xc]:
        tape[xc]-=1
    tape[xc]+=2
    xc+=1
    while tape[xc]:
        tape[xc]-=1
    tape[xc]+=1
    xc+=3
    tape[xc]+=1
    while tape[xc]:
        while tape[xc]:
            tape[xc]-=1
        tape[xc]+=6
        xc+=3
    xc-=3
    while tape[xc]:
        while tape[xc]:
            xc-=1
            tape[xc]+=8
            xc-=1
            tape[xc]+=2
            xc+=2
            tape[xc]-=1
        tape[xc]+=1
        xc-=1
        sys.stdout.write(chr(tape[xc]))
        xc-=1
        while tape[xc]:
            xc+=1
            tape[xc]-=4
            xc-=1
            tape[xc]-=1
        xc-=1
    xc-=2
    while tape[xc]:
        xc+=5
        while tape[xc]:
            xc+=3
            while tape[xc]:
                tape[xc]-=1
            tape[xc]+=9
            xc-=1
            while tape[xc]:
                xc+=1
                tape[xc]-=1
                xc-=1
                tape[xc]-=1
            tape[xc]+=9
            xc+=1
            while tape[xc]:
                tape[xc]-=1
                while tape[xc]:
                    xc-=1
                    tape[xc]-=1
                    xc+=1
                    tape[xc]-=1
                tape[xc]+=1
                while tape[xc]:
                    xc-=3
            xc-=1
            while tape[xc]:
                xc+=1
                tape[xc]+=1
                xc-=1
                tape[xc]-=1
            xc+=1
        xc-=2
        tape[xc]-=1
    xc-=2
    tape[xc]-=1
