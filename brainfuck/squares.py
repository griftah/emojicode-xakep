
# coding=utf-8
# Создано bf-compiler.py из исходника на Brainfuck.
import sys
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
		sys.stdout.write(chr(tape[xc]))
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
