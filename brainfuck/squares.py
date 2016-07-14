
# coding=utf-8
# Автоматически скомпилировано из Brainfuck.
from sys import stdout
tape = [0]*32000
xc = 0

tape[xc]+=1
tape[xc]+=1
tape[xc]+=1
tape[xc]+=1
while tape[xc]:
	xc+=1
	tape[xc]+=1
	tape[xc]+=1
	tape[xc]+=1
	tape[xc]+=1
	tape[xc]+=1
	xc-=1
	tape[xc]-=1
xc+=1
while tape[xc]:
	xc-=1
	tape[xc]+=1
	tape[xc]+=1
	tape[xc]+=1
	tape[xc]+=1
	tape[xc]+=1
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
		xc-=1
		xc-=1
		tape[xc]-=1
	tape[xc]+=1
	tape[xc]+=1
	xc+=1
	xc+=1
	while tape[xc]:
		xc-=1
		xc-=1
		tape[xc]+=1
		xc+=1
		xc+=1
		tape[xc]-=1
	xc+=1
	xc+=1
	xc+=1
	while tape[xc]:
		tape[xc]-=1
	tape[xc]+=1
	tape[xc]+=1
	xc+=1
	while tape[xc]:
		tape[xc]-=1
	tape[xc]+=1
	xc+=1
	xc+=1
	xc+=1
	tape[xc]+=1
	while tape[xc]:
		while tape[xc]:
			tape[xc]-=1
		tape[xc]+=1
		tape[xc]+=1
		tape[xc]+=1
		tape[xc]+=1
		tape[xc]+=1
		tape[xc]+=1
		xc+=1
		xc+=1
		xc+=1
	xc-=1
	xc-=1
	xc-=1
	while tape[xc]:
		while tape[xc]:
			xc-=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			xc-=1
			tape[xc]+=1
			tape[xc]+=1
			xc+=1
			xc+=1
			tape[xc]-=1
		tape[xc]+=1
		xc-=1
		stdout.write(chr(tape[xc])); stdout.flush()
		xc-=1
		while tape[xc]:
			xc+=1
			tape[xc]-=1
			tape[xc]-=1
			tape[xc]-=1
			tape[xc]-=1
			xc-=1
			tape[xc]-=1
		xc-=1
	xc-=1
	xc-=1
	while tape[xc]:
		xc+=1
		xc+=1
		xc+=1
		xc+=1
		xc+=1
		while tape[xc]:
			xc+=1
			xc+=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			xc-=1
			while tape[xc]:
				xc+=1
				tape[xc]-=1
				xc-=1
				tape[xc]-=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
			tape[xc]+=1
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
					xc-=1
					xc-=1
					xc-=1
			xc-=1
			while tape[xc]:
				xc+=1
				tape[xc]+=1
				xc-=1
				tape[xc]-=1
			xc+=1
		xc-=1
		xc-=1
		tape[xc]-=1
	xc-=1
	xc-=1
	tape[xc]-=1