
# coding=utf-8
# Автоматически скомпилировано из Brainfuck.
from sys import stdout
tape = [0]*32000
xc = 0
tape[xc]+=13
while tape[xc]:
	tape[xc]-=1
	xc+=1
	tape[xc]+=2
	xc+=3
	tape[xc]+=5
	xc+=1
	tape[xc]+=2
	xc+=1
	tape[xc]+=1
	xc-=6
xc+=5
tape[xc]+=6
xc+=1
tape[xc]-=3
xc+=10
tape[xc]+=15
while tape[xc]:
	while tape[xc]:
		xc+=9
	tape[xc]+=1
	while tape[xc]:
		xc-=9
	xc+=9
	tape[xc]-=1
tape[xc]+=1
while tape[xc]:
	xc+=8
	while tape[xc]:
		tape[xc]-=1
	xc+=1
xc-=9
while tape[xc]:
	xc-=9
xc+=8
while tape[xc]:
	tape[xc]-=1
tape[xc]+=1
xc-=7
tape[xc]+=5
while tape[xc]:
	tape[xc]-=1
	while tape[xc]:
		tape[xc]-=1
		xc+=9
		tape[xc]+=1
		xc-=9
	xc+=9
xc+=7
tape[xc]+=1
xc+=27
tape[xc]+=1
xc-=17
while tape[xc]:
	xc-=9
xc+=3
while tape[xc]:
	tape[xc]-=1
tape[xc]+=1
while tape[xc]:
	xc+=6
	while tape[xc]:
		xc+=7
		while tape[xc]:
			tape[xc]-=1
		xc+=2
	xc-=9
	while tape[xc]:
		xc-=9
	xc+=7
	while tape[xc]:
		tape[xc]-=1
	tape[xc]+=1
	xc-=6
	tape[xc]+=4
	while tape[xc]:
		tape[xc]-=1
		while tape[xc]:
			tape[xc]-=1
			xc+=9
			tape[xc]+=1
			xc-=9
		xc+=9
	xc+=6
	tape[xc]+=1
	xc-=6
	tape[xc]+=7
	while tape[xc]:
		tape[xc]-=1
		while tape[xc]:
			tape[xc]-=1
			xc+=9
			tape[xc]+=1
			xc-=9
		xc+=9
	xc+=6
	tape[xc]+=1
	xc-=16
	while tape[xc]:
		xc-=9
	xc+=3
	while tape[xc]:
		while tape[xc]:
			tape[xc]-=1
		xc+=6
		while tape[xc]:
			xc+=7
			while tape[xc]:
				tape[xc]-=1
				xc-=6
				tape[xc]+=1
				xc+=6
			xc-=6
			while tape[xc]:
				tape[xc]-=1
				xc+=6
				tape[xc]+=1
				xc-=2
				tape[xc]+=1
				xc-=3
				tape[xc]+=1
				xc-=1
			xc+=8
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=8
			while tape[xc]:
				tape[xc]-=1
				xc-=7
				tape[xc]+=1
				xc+=7
			xc-=7
			while tape[xc]:
				tape[xc]-=1
				xc+=7
				tape[xc]+=1
				xc-=2
				tape[xc]+=1
				xc-=3
				tape[xc]+=1
				xc-=2
			xc+=8
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=7
		while tape[xc]:
			tape[xc]-=1
			xc-=7
			tape[xc]+=1
			xc+=7
		xc-=7
		while tape[xc]:
			tape[xc]-=1
			xc+=7
			tape[xc]+=1
			xc-=2
			tape[xc]+=1
			xc-=5
		xc+=9
		tape[xc]+=15
		while tape[xc]:
			while tape[xc]:
				xc+=9
			tape[xc]+=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			tape[xc]-=1
		tape[xc]+=1
		while tape[xc]:
			xc+=1
			tape[xc]+=1
			xc+=8
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=1
			tape[xc]-=1
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=4
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]+=1
				xc-=5
				while tape[xc]:
					tape[xc]-=1
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc-=2
						tape[xc]+=1
						xc+=2
					xc-=2
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						tape[xc]+=1
						xc+=2
						tape[xc]+=1
						xc-=4
					tape[xc]+=1
					xc+=9
				xc-=8
				while tape[xc]:
					xc-=9
			xc+=9
			while tape[xc]:
				xc+=9
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc-=10
			xc+=1
			while tape[xc]:
				tape[xc]-=1
				xc+=9
				tape[xc]+=1
				xc-=9
			xc-=1
			tape[xc]+=1
			xc+=8
		xc-=9
		while tape[xc]:
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc-=1
			tape[xc]-=1
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					xc-=1
					tape[xc]-=1
					xc+=1
					tape[xc]-=1
					xc-=6
					tape[xc]+=1
					xc+=6
				xc-=1
				while tape[xc]:
					tape[xc]-=1
					xc+=1
					tape[xc]+=1
					xc-=1
				xc+=4
			xc-=3
			while tape[xc]:
				tape[xc]-=1
				xc+=3
				tape[xc]+=1
				xc-=3
			xc-=1
			tape[xc]+=1
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=1
			tape[xc]+=1
			xc+=8
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=1
			tape[xc]-=1
			xc+=5
			while tape[xc]:
				tape[xc]-=1
				xc-=5
				tape[xc]+=1
				xc+=5
			xc-=5
			while tape[xc]:
				tape[xc]-=1
				xc+=5
				tape[xc]+=1
				xc-=6
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					while tape[xc]:
						tape[xc]-=1
						xc-=3
						tape[xc]+=1
						xc+=3
					xc-=3
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]+=1
						xc+=1
						tape[xc]+=1
						xc-=4
					tape[xc]+=1
					xc+=9
				xc-=8
				while tape[xc]:
					xc-=9
			xc+=9
			while tape[xc]:
				xc+=9
			xc-=9
			while tape[xc]:
				xc+=2
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc-=11
			xc+=2
			while tape[xc]:
				tape[xc]-=1
				xc+=9
				tape[xc]+=1
				xc-=9
			xc-=2
			tape[xc]+=1
			xc+=8
		xc-=9
		while tape[xc]:
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc-=1
			tape[xc]-=1
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					xc-=1
					tape[xc]-=1
					xc+=1
					tape[xc]-=1
					xc-=6
					tape[xc]+=1
					xc+=6
				xc-=1
				while tape[xc]:
					tape[xc]-=1
					xc+=1
					tape[xc]+=1
					xc-=1
				xc+=4
			xc-=3
			while tape[xc]:
				tape[xc]-=1
				xc+=3
				tape[xc]+=1
				xc-=3
			xc-=1
			tape[xc]+=1
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=36
				tape[xc]+=1
				xc+=36
			xc+=5
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=9
		tape[xc]+=15
		while tape[xc]:
			while tape[xc]:
				xc+=9
			xc-=9
			tape[xc]-=1
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			tape[xc]-=1
		tape[xc]+=1
		xc+=21
		tape[xc]+=1
		xc-=3
		while tape[xc]:
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=3
			while tape[xc]:
				tape[xc]-=1
				xc-=3
				tape[xc]-=1
				xc+=3
			tape[xc]+=1
			xc-=3
			while tape[xc]:
				tape[xc]-=1
				xc+=3
				tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc-=13
					while tape[xc]:
						xc-=9
					xc+=4
					while tape[xc]:
						tape[xc]-=1
					tape[xc]+=1
					xc+=5
					while tape[xc]:
						xc+=9
					xc+=1
					tape[xc]+=1
					xc-=1
			tape[xc]+=1
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]-=1
				xc+=4
			tape[xc]+=1
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]-=1
				xc-=1
				while tape[xc]:
					tape[xc]-=1
					xc-=3
					tape[xc]+=1
					xc+=3
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]+=1
					xc-=12
					while tape[xc]:
						xc-=9
					xc+=3
					while tape[xc]:
						tape[xc]-=1
					tape[xc]+=1
					xc+=6
					while tape[xc]:
						xc+=9
					xc+=1
					while tape[xc]:
						tape[xc]-=1
					tape[xc]+=1
					xc-=1
			tape[xc]+=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
				xc-=1
				while tape[xc]:
					xc+=9
				xc-=8
			xc+=8
		xc-=9
		while tape[xc]:
			xc-=9
		xc-=7
		while tape[xc]:
			tape[xc]-=1
			xc+=1
			tape[xc]+=1
			xc+=3
			tape[xc]-=1
			xc-=4
		xc+=9
		tape[xc]+=26
		xc+=2
		while tape[xc]:
			tape[xc]-=1
			xc-=4
			tape[xc]+=1
			xc+=4
		xc-=4
		while tape[xc]:
			tape[xc]-=1
			xc+=4
			tape[xc]+=1
			xc-=2
			while tape[xc]:
				tape[xc]-=1
			xc-=2
		xc+=2
		while tape[xc]:
			xc-=7
			tape[xc]+=1
			xc-=1
			while tape[xc]:
				tape[xc]-=1
				xc-=1
				tape[xc]+=1
				xc+=4
				tape[xc]+=1
				xc-=2
				while tape[xc]:
					tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
				xc-=2
				while tape[xc]:
					tape[xc]-=1
					xc+=1
					tape[xc]+=1
					xc+=3
					tape[xc]-=1
					xc-=4
				xc+=3
			xc+=13
			while tape[xc]:
				xc+=2
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=5
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=3
			while tape[xc]:
				tape[xc]-=1
			xc+=6
			while tape[xc]:
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc-=3
					tape[xc]+=1
					xc-=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=2
				while tape[xc]:
					tape[xc]-=1
					xc-=9
					tape[xc]+=1
					xc+=9
				xc+=7
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			tape[xc]+=15
			while tape[xc]:
				while tape[xc]:
					xc+=9
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=9
				tape[xc]-=1
			tape[xc]+=1
			while tape[xc]:
				xc+=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=1
				tape[xc]-=1
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]+=1
					xc+=5
				xc-=5
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]+=1
					xc-=6
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]+=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc+=1
							tape[xc]+=1
							xc-=3
						tape[xc]+=1
						xc+=9
					xc-=8
					while tape[xc]:
						xc-=9
				xc+=9
				while tape[xc]:
					xc+=9
				xc-=9
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=9
						tape[xc]+=1
						xc-=9
					xc-=10
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc-=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=3
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						xc-=1
						tape[xc]-=1
						xc+=1
						tape[xc]-=1
						xc-=7
						tape[xc]+=1
						xc+=7
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc-=1
					xc+=3
				xc-=2
				while tape[xc]:
					tape[xc]-=1
					xc+=2
					tape[xc]+=1
					xc-=2
				xc-=1
				tape[xc]+=1
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=6
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]+=1
					xc+=5
				xc-=5
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]+=1
					xc-=4
					tape[xc]+=1
					xc-=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=1
				tape[xc]-=1
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]+=1
					xc+=5
				xc-=5
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]+=1
					xc-=6
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]+=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc+=2
							tape[xc]+=1
							xc-=4
						tape[xc]+=1
						xc+=9
					xc-=8
					while tape[xc]:
						xc-=9
				xc+=9
				while tape[xc]:
					xc+=9
				xc-=9
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=9
						tape[xc]+=1
						xc-=9
					xc-=10
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc-=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						xc-=1
						tape[xc]-=1
						xc+=1
						tape[xc]-=1
						xc-=6
						tape[xc]+=1
						xc+=6
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc-=1
					xc+=4
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]+=1
					xc-=3
				xc-=1
				tape[xc]+=1
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=36
					tape[xc]+=1
					xc+=36
				xc+=5
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=36
					tape[xc]+=1
					xc+=36
				xc+=6
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			tape[xc]+=15
			while tape[xc]:
				while tape[xc]:
					xc+=9
				xc-=9
				tape[xc]-=1
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=9
				tape[xc]-=1
			tape[xc]+=1
			while tape[xc]:
				xc+=8
				while tape[xc]:
					tape[xc]-=1
					xc-=7
					tape[xc]+=1
					xc+=7
				xc-=7
				while tape[xc]:
					tape[xc]-=1
					xc+=7
					tape[xc]+=1
					xc-=6
					tape[xc]+=1
					xc-=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=6
				while tape[xc]:
					tape[xc]-=1
				xc+=3
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=4
			tape[xc]+=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=5
			xc+=1
			while tape[xc]:
				tape[xc]-=1
				xc-=6
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]+=1
					xc-=1
					tape[xc]+=2
					xc-=4
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]+=1
					xc+=5
				xc-=1
				tape[xc]-=1
				xc+=1
				tape[xc]+=1
				xc+=1
			xc-=1
			while tape[xc]:
				tape[xc]-=1
				xc+=1
				tape[xc]+=1
				xc-=1
			xc-=5
			while tape[xc]:
				tape[xc]-=1
				xc+=5
				tape[xc]+=1
				xc-=5
			xc+=6
			while tape[xc]:
				tape[xc]-=1
			xc-=6
			tape[xc]+=1
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]-=1
				xc+=4
			tape[xc]+=1
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]-=1
				xc+=5
				while tape[xc]:
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc-=2
						tape[xc]-=1
						xc+=2
					tape[xc]+=1
					xc-=2
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						tape[xc]-=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc-=3
							tape[xc]+=1
							xc+=3
						xc-=3
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]+=1
							xc-=12
							while tape[xc]:
								xc-=9
							xc+=3
							while tape[xc]:
								tape[xc]-=1
							tape[xc]+=1
							xc+=6
							while tape[xc]:
								xc+=9
							xc+=1
							tape[xc]+=1
							xc-=1
					tape[xc]+=1
					xc+=3
					while tape[xc]:
						tape[xc]-=1
						xc-=3
						tape[xc]-=1
						xc+=3
					tape[xc]+=1
					xc-=3
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]-=1
						xc-=1
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]+=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc-=11
							while tape[xc]:
								xc-=9
							xc+=4
							while tape[xc]:
								tape[xc]-=1
							tape[xc]+=1
							xc+=5
							while tape[xc]:
								xc+=9
							xc+=1
							while tape[xc]:
								tape[xc]-=1
							tape[xc]+=1
							xc-=1
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc-=1
						while tape[xc]:
							xc+=9
						xc-=8
					xc+=8
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc+=5
					while tape[xc]:
						xc+=1
						tape[xc]+=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]-=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc-=2
						xc+=8
					xc-=8
					tape[xc]+=1
					xc-=1
					while tape[xc]:
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=5
							tape[xc]+=1
							xc-=4
							while tape[xc]:
								tape[xc]-=1
								xc+=4
								tape[xc]-=1
								xc-=14
								tape[xc]+=1
								xc+=11
								while tape[xc]:
									tape[xc]-=1
									xc+=3
									tape[xc]+=1
									xc-=3
								xc-=1
							xc+=1
							while tape[xc]:
								tape[xc]-=1
								xc+=3
								tape[xc]-=1
								xc-=14
								tape[xc]+=1
								xc+=11
							xc-=2
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=4
							tape[xc]+=1
							xc-=3
							while tape[xc]:
								tape[xc]-=1
								xc+=3
								tape[xc]-=1
								xc-=14
								tape[xc]+=1
								xc+=11
							xc-=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]+=1
							xc-=3
						xc-=12
					xc+=4
					while tape[xc]:
						tape[xc]-=1
					xc-=4
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=3
					tape[xc]+=1
					xc+=3
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]+=1
					xc+=6
					while tape[xc]:
						xc+=1
						tape[xc]+=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc-=1
							tape[xc]-=1
							xc+=1
						xc-=1
						while tape[xc]:
							tape[xc]-=1
							xc+=1
							tape[xc]+=1
							xc-=1
						xc+=8
					xc-=8
					tape[xc]+=1
					xc-=1
					while tape[xc]:
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=5
							tape[xc]+=1
							xc-=3
							while tape[xc]:
								tape[xc]-=1
								xc+=3
								tape[xc]-=1
								xc-=14
								tape[xc]+=1
								xc+=10
								while tape[xc]:
									tape[xc]-=1
									xc+=4
									tape[xc]+=1
									xc-=4
								xc+=1
							xc-=1
							while tape[xc]:
								tape[xc]-=1
								xc+=4
								tape[xc]-=1
								xc-=14
								tape[xc]+=1
								xc+=10
							xc-=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]+=1
							xc-=4
							while tape[xc]:
								tape[xc]-=1
								xc+=4
								tape[xc]-=1
								xc-=14
								tape[xc]+=1
								xc+=10
							xc+=1
						xc-=1
						while tape[xc]:
							tape[xc]-=1
							xc+=4
							tape[xc]+=1
							xc-=4
						xc-=11
					xc+=6
					tape[xc]+=1
					xc-=6
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=4
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]+=1
				xc+=5
				while tape[xc]:
					xc+=9
				xc-=9
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=5
						tape[xc]+=1
						xc-=4
						while tape[xc]:
							tape[xc]-=1
							xc+=4
							tape[xc]-=1
							xc-=14
							tape[xc]+=1
							xc+=11
							while tape[xc]:
								tape[xc]-=1
								xc+=3
								tape[xc]+=1
								xc-=3
							xc-=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]-=1
							xc-=14
							tape[xc]+=1
							xc+=11
						xc-=2
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=4
						tape[xc]+=1
						xc-=3
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]-=1
							xc-=14
							tape[xc]+=1
							xc+=11
						xc-=1
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]+=1
						xc-=3
					xc-=12
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=2
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=5
			while tape[xc]:
				xc+=2
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=6
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc-=3
					tape[xc]+=1
					xc-=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			tape[xc]+=15
			while tape[xc]:
				while tape[xc]:
					xc+=9
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=9
				tape[xc]-=1
			tape[xc]+=1
			while tape[xc]:
				xc+=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=1
				tape[xc]-=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc-=5
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]+=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc+=1
							tape[xc]+=1
							xc-=3
						tape[xc]+=1
						xc+=9
					xc-=8
					while tape[xc]:
						xc-=9
				xc+=9
				while tape[xc]:
					xc+=9
				xc-=9
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=9
						tape[xc]+=1
						xc-=9
					xc-=10
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc-=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=3
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						xc-=1
						tape[xc]-=1
						xc+=1
						tape[xc]-=1
						xc-=7
						tape[xc]+=1
						xc+=7
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc-=1
					xc+=3
				xc-=2
				while tape[xc]:
					tape[xc]-=1
					xc+=2
					tape[xc]+=1
					xc-=2
				xc-=1
				tape[xc]+=1
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=36
					tape[xc]+=1
					xc+=36
				xc+=6
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=5
			while tape[xc]:
				tape[xc]-=1
			xc+=4
			tape[xc]+=15
			while tape[xc]:
				while tape[xc]:
					xc+=9
				xc-=9
				tape[xc]-=1
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=9
				tape[xc]-=1
			tape[xc]+=1
			while tape[xc]:
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=3
					tape[xc]-=1
					xc+=3
				tape[xc]+=1
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]-=1
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc-=4
						tape[xc]+=1
						xc+=4
					xc-=4
					while tape[xc]:
						tape[xc]-=1
						xc+=4
						tape[xc]+=1
						xc-=13
						while tape[xc]:
							xc-=9
						xc+=4
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc+=5
						while tape[xc]:
							xc+=9
						xc+=1
						tape[xc]+=1
						xc-=1
				tape[xc]+=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]-=1
					xc+=4
				tape[xc]+=1
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]-=1
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc-=3
						tape[xc]+=1
						xc+=3
					xc-=3
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]+=1
						xc-=12
						while tape[xc]:
							xc-=9
						xc+=3
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc+=6
						while tape[xc]:
							xc+=9
						xc+=1
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc-=1
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc-=1
					while tape[xc]:
						xc+=9
					xc-=8
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=3
			while tape[xc]:
				tape[xc]-=1
				xc-=3
				tape[xc]+=1
				xc+=3
			xc-=3
			while tape[xc]:
				tape[xc]-=1
				xc+=3
				tape[xc]+=1
				xc+=6
				while tape[xc]:
					xc+=1
					tape[xc]+=1
					xc+=3
					while tape[xc]:
						tape[xc]-=1
						xc-=3
						tape[xc]-=1
						xc+=3
					xc-=3
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]+=1
						xc-=3
					xc+=8
				xc-=8
				tape[xc]+=1
				xc-=1
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc-=1
							tape[xc]-=1
							xc-=10
							tape[xc]+=1
							xc+=12
							while tape[xc]:
								tape[xc]-=1
								xc-=2
								tape[xc]+=1
								xc+=2
							xc-=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]-=1
							xc-=10
							tape[xc]+=1
							xc+=12
						xc-=3
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc-=1
						tape[xc]+=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]-=1
							xc-=10
							tape[xc]+=1
							xc+=12
						xc-=1
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc-=2
						tape[xc]+=1
						xc+=2
					xc-=13
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=4
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]+=1
				xc+=5
				while tape[xc]:
					xc+=1
					tape[xc]+=1
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc-=2
						tape[xc]-=1
						xc+=2
					xc-=2
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						tape[xc]+=1
						xc-=2
					xc+=8
				xc-=8
				tape[xc]+=1
				xc-=1
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]-=1
							xc-=10
							tape[xc]+=1
							xc+=11
							while tape[xc]:
								tape[xc]-=1
								xc-=1
								tape[xc]+=1
								xc+=1
							xc+=1
						xc-=1
						while tape[xc]:
							tape[xc]-=1
							xc-=1
							tape[xc]-=1
							xc-=10
							tape[xc]+=1
							xc+=11
						xc-=2
					xc+=3
					while tape[xc]:
						tape[xc]-=1
						xc-=2
						tape[xc]+=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc-=1
							tape[xc]-=1
							xc-=10
							tape[xc]+=1
							xc+=11
						xc+=1
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc-=1
						tape[xc]+=1
						xc+=1
					xc-=12
				xc+=5
				tape[xc]+=1
				xc-=5
			xc+=9
			while tape[xc]:
				xc+=3
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=4
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=3
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=5
			while tape[xc]:
				xc+=7
				while tape[xc]:
					tape[xc]-=1
					xc-=6
					tape[xc]+=1
					xc+=6
				xc-=6
				while tape[xc]:
					tape[xc]-=1
					xc+=6
					tape[xc]+=1
					xc-=4
					tape[xc]+=1
					xc-=2
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=4
			tape[xc]+=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=5
			xc+=2
			while tape[xc]:
				tape[xc]-=1
				xc-=7
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]+=1
					xc-=1
					tape[xc]+=2
					xc-=4
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]+=1
					xc+=5
				xc-=1
				tape[xc]-=1
				xc+=1
				tape[xc]+=1
				xc+=2
			xc-=2
			while tape[xc]:
				tape[xc]-=1
				xc+=2
				tape[xc]+=1
				xc-=2
			xc-=5
			while tape[xc]:
				tape[xc]-=1
				xc+=5
				tape[xc]+=1
				xc-=5
			tape[xc]+=1
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]-=1
				xc+=4
			tape[xc]+=1
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]-=1
				xc+=5
				while tape[xc]:
					xc+=3
					while tape[xc]:
						tape[xc]-=1
						xc-=3
						tape[xc]-=1
						xc+=3
					tape[xc]+=1
					xc-=3
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]-=1
						xc-=1
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]+=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc-=11
							while tape[xc]:
								xc-=9
							xc+=4
							while tape[xc]:
								tape[xc]-=1
							tape[xc]+=1
							xc+=5
							while tape[xc]:
								xc+=9
							xc+=1
							tape[xc]+=1
							xc-=1
					tape[xc]+=1
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc-=2
						tape[xc]-=1
						xc+=2
					tape[xc]+=1
					xc-=2
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						tape[xc]-=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc-=3
							tape[xc]+=1
							xc+=3
						xc-=3
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]+=1
							xc-=12
							while tape[xc]:
								xc-=9
							xc+=3
							while tape[xc]:
								tape[xc]-=1
							tape[xc]+=1
							xc+=6
							while tape[xc]:
								xc+=9
							xc+=1
							while tape[xc]:
								tape[xc]-=1
							tape[xc]+=1
							xc-=1
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc-=1
						while tape[xc]:
							xc+=9
						xc-=8
					xc+=8
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=3
					tape[xc]+=1
					xc+=3
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]+=1
					xc+=6
					while tape[xc]:
						xc+=1
						tape[xc]+=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc-=1
							tape[xc]-=1
							xc+=1
						xc-=1
						while tape[xc]:
							tape[xc]-=1
							xc+=1
							tape[xc]+=1
							xc-=1
						xc+=8
					xc-=8
					tape[xc]+=1
					xc-=1
					while tape[xc]:
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=4
							tape[xc]+=1
							xc-=2
							while tape[xc]:
								tape[xc]-=1
								xc+=2
								tape[xc]-=1
								xc-=13
								tape[xc]+=1
								xc+=10
								while tape[xc]:
									tape[xc]-=1
									xc+=3
									tape[xc]+=1
									xc-=3
								xc+=1
							xc-=1
							while tape[xc]:
								tape[xc]-=1
								xc+=3
								tape[xc]-=1
								xc-=13
								tape[xc]+=1
								xc+=10
							xc-=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc-=3
							while tape[xc]:
								tape[xc]-=1
								xc+=3
								tape[xc]-=1
								xc-=13
								tape[xc]+=1
								xc+=10
							xc+=1
						xc-=1
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]+=1
							xc-=3
						xc-=11
					xc+=5
					while tape[xc]:
						tape[xc]-=1
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc-=7
						tape[xc]+=1
						xc+=7
					xc-=7
					while tape[xc]:
						tape[xc]-=1
						xc+=7
						tape[xc]+=1
						xc-=2
						tape[xc]+=1
						xc-=5
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc+=5
					while tape[xc]:
						xc+=1
						tape[xc]+=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]-=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc-=2
						xc+=8
					xc-=8
					tape[xc]+=1
					xc-=1
					while tape[xc]:
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=4
							tape[xc]+=1
							xc-=3
							while tape[xc]:
								tape[xc]-=1
								xc+=3
								tape[xc]-=1
								xc-=13
								tape[xc]+=1
								xc+=11
								while tape[xc]:
									tape[xc]-=1
									xc+=2
									tape[xc]+=1
									xc-=2
								xc-=1
							xc+=1
							while tape[xc]:
								tape[xc]-=1
								xc+=2
								tape[xc]-=1
								xc-=13
								tape[xc]+=1
								xc+=11
							xc-=2
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]+=1
							xc-=2
							while tape[xc]:
								tape[xc]-=1
								xc+=2
								tape[xc]-=1
								xc-=13
								tape[xc]+=1
								xc+=11
							xc-=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc-=2
						xc-=12
				xc+=4
				while tape[xc]:
					tape[xc]-=1
				xc-=4
			xc+=4
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=4
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=2
				while tape[xc]:
					tape[xc]-=1
					xc-=7
					tape[xc]+=1
					xc+=7
				xc-=7
				while tape[xc]:
					tape[xc]-=1
					xc+=7
					tape[xc]+=1
					xc-=2
					tape[xc]+=1
					xc-=5
				xc+=9
				while tape[xc]:
					xc+=9
				xc-=9
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=4
						tape[xc]+=1
						xc-=3
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]-=1
							xc-=13
							tape[xc]+=1
							xc+=11
							while tape[xc]:
								tape[xc]-=1
								xc+=2
								tape[xc]+=1
								xc-=2
							xc-=1
						xc+=1
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]-=1
							xc-=13
							tape[xc]+=1
							xc+=11
						xc-=2
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]+=1
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]-=1
							xc-=13
							tape[xc]+=1
							xc+=11
						xc-=1
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						tape[xc]+=1
						xc-=2
					xc-=12
			xc+=9
			while tape[xc]:
				xc+=2
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=6
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=3
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=5
			while tape[xc]:
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc-=3
					tape[xc]+=1
					xc-=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=6
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]+=1
					xc+=5
				xc-=5
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]+=1
					xc-=3
					tape[xc]+=1
					xc-=2
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			tape[xc]+=15
			while tape[xc]:
				while tape[xc]:
					xc+=9
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=9
				tape[xc]-=1
			tape[xc]+=1
			while tape[xc]:
				xc+=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=1
				tape[xc]-=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc-=5
					while tape[xc]:
						tape[xc]-=1
						xc+=2
						while tape[xc]:
							tape[xc]-=1
							xc-=2
							tape[xc]+=1
							xc+=2
						xc-=2
						while tape[xc]:
							tape[xc]-=1
							xc+=2
							tape[xc]+=1
							xc+=2
							tape[xc]+=1
							xc-=4
						tape[xc]+=1
						xc+=9
					xc-=8
					while tape[xc]:
						xc-=9
				xc+=9
				while tape[xc]:
					xc+=9
				xc-=9
				while tape[xc]:
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc+=9
						tape[xc]+=1
						xc-=9
					xc-=10
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc-=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						xc-=1
						tape[xc]-=1
						xc+=1
						tape[xc]-=1
						xc-=6
						tape[xc]+=1
						xc+=6
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc-=1
					xc+=4
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]+=1
					xc-=3
				xc-=1
				tape[xc]+=1
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=1
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=1
				tape[xc]-=1
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]+=1
					xc+=5
				xc-=5
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]+=1
					xc-=6
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						while tape[xc]:
							tape[xc]-=1
							xc-=3
							tape[xc]+=1
							xc+=3
						xc-=3
						while tape[xc]:
							tape[xc]-=1
							xc+=3
							tape[xc]+=1
							xc+=1
							tape[xc]+=1
							xc-=4
						tape[xc]+=1
						xc+=9
					xc-=8
					while tape[xc]:
						xc-=9
				xc+=9
				while tape[xc]:
					xc+=9
				xc-=9
				while tape[xc]:
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc+=9
						tape[xc]+=1
						xc-=9
					xc-=11
				xc+=2
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc-=2
				tape[xc]+=1
				xc+=8
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						xc-=1
						tape[xc]-=1
						xc+=1
						tape[xc]-=1
						xc-=6
						tape[xc]+=1
						xc+=6
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc-=1
					xc+=4
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]+=1
					xc-=3
				xc-=1
				tape[xc]+=1
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=36
					tape[xc]+=1
					xc+=36
				xc+=5
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=9
			tape[xc]+=15
			while tape[xc]:
				while tape[xc]:
					xc+=9
				xc-=9
				tape[xc]-=1
				xc-=9
				while tape[xc]:
					xc-=9
				xc+=9
				tape[xc]-=1
			tape[xc]+=1
			xc+=21
			tape[xc]+=1
			xc-=3
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=3
				while tape[xc]:
					tape[xc]-=1
					xc-=3
					tape[xc]-=1
					xc+=3
				tape[xc]+=1
				xc-=3
				while tape[xc]:
					tape[xc]-=1
					xc+=3
					tape[xc]-=1
					xc+=1
					while tape[xc]:
						tape[xc]-=1
						xc-=4
						tape[xc]+=1
						xc+=4
					xc-=4
					while tape[xc]:
						tape[xc]-=1
						xc+=4
						tape[xc]+=1
						xc-=13
						while tape[xc]:
							xc-=9
						xc+=4
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc+=5
						while tape[xc]:
							xc+=9
						xc+=1
						tape[xc]+=1
						xc-=1
				tape[xc]+=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]-=1
					xc+=4
				tape[xc]+=1
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]-=1
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc-=3
						tape[xc]+=1
						xc+=3
					xc-=3
					while tape[xc]:
						tape[xc]-=1
						xc+=3
						tape[xc]+=1
						xc-=12
						while tape[xc]:
							xc-=9
						xc+=3
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc+=6
						while tape[xc]:
							xc+=9
						xc+=1
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc-=1
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc-=1
					while tape[xc]:
						xc+=9
					xc-=8
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=2
			tape[xc]-=1
			xc+=2
			while tape[xc]:
				tape[xc]-=1
				xc-=4
				tape[xc]+=1
				xc+=4
			xc-=4
			while tape[xc]:
				tape[xc]-=1
				xc+=4
				tape[xc]+=1
				xc-=2
				while tape[xc]:
					tape[xc]-=1
				xc-=2
			xc+=2
		xc-=2
		tape[xc]+=1
		xc+=4
		while tape[xc]:
			tape[xc]-=1
			xc-=4
			tape[xc]-=1
			xc+=4
		tape[xc]+=1
		xc-=4
		while tape[xc]:
			tape[xc]-=1
			xc+=4
			tape[xc]-=1
			xc-=6
			stdout.write(chr(tape[xc])); stdout.flush()
			xc+=2
		xc+=4
		while tape[xc]:
			tape[xc]-=1
			xc-=7
			stdout.write(chr(tape[xc])); stdout.flush()
			xc+=7
		xc-=3
		while tape[xc]:
			tape[xc]-=1
		xc+=1
		while tape[xc]:
			tape[xc]-=1
		xc+=1
		while tape[xc]:
			tape[xc]-=1
		xc+=1
		while tape[xc]:
			tape[xc]-=1
		xc+=1
		while tape[xc]:
			tape[xc]-=1
		xc+=1
		while tape[xc]:
			tape[xc]-=1
		xc+=3
		while tape[xc]:
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=3
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=5
			while tape[xc]:
				tape[xc]-=1
			xc+=4
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=1
		tape[xc]+=11
		while tape[xc]:
			tape[xc]-=1
			while tape[xc]:
				tape[xc]-=1
				xc+=9
				tape[xc]+=1
				xc-=9
			xc+=9
		xc+=4
		tape[xc]+=1
		xc+=9
		tape[xc]+=1
		xc-=14
		while tape[xc]:
			xc-=9
		xc+=7
		while tape[xc]:
			tape[xc]-=1
			xc-=7
			tape[xc]+=1
			xc+=7
		xc-=7
		while tape[xc]:
			tape[xc]-=1
			xc+=7
			tape[xc]+=1
			while tape[xc]:
				tape[xc]-=1
			xc+=2
			while tape[xc]:
				xc+=9
			xc-=9
			while tape[xc]:
				xc+=7
				while tape[xc]:
					tape[xc]-=1
					xc-=6
					tape[xc]+=1
					xc+=6
				xc-=6
				while tape[xc]:
					tape[xc]-=1
					xc+=6
					tape[xc]+=1
					xc-=7
					while tape[xc]:
						xc-=9
					xc+=7
					while tape[xc]:
						tape[xc]-=1
					tape[xc]+=1
					xc+=3
				xc-=10
		xc+=7
		while tape[xc]:
			tape[xc]-=1
			xc-=7
			tape[xc]+=1
			xc+=7
		xc-=7
		while tape[xc]:
			tape[xc]-=1
			xc+=7
			tape[xc]+=1
			xc+=2
			while tape[xc]:
				xc+=1
				tape[xc]+=1
				xc+=4
				while tape[xc]:
					tape[xc]-=1
					xc-=4
					tape[xc]-=1
					xc+=4
				xc-=4
				while tape[xc]:
					tape[xc]-=1
					xc+=4
					tape[xc]+=1
					xc-=4
				xc+=8
			xc-=2
			tape[xc]+=1
			xc-=7
			while tape[xc]:
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc+=2
					tape[xc]+=1
					xc-=2
				xc-=14
			xc+=9
			while tape[xc]:
				xc+=9
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc+=7
				while tape[xc]:
					tape[xc]-=1
					xc-=7
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						xc-=1
						tape[xc]-=1
						xc+=1
						tape[xc]-=1
						xc-=3
						tape[xc]+=1
						xc+=3
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc-=1
					xc+=7
				xc-=6
				while tape[xc]:
					tape[xc]-=1
					xc+=6
					tape[xc]+=1
					xc-=6
				xc-=1
				tape[xc]+=1
				xc-=9
			xc+=7
			tape[xc]-=1
			xc-=4
			while tape[xc]:
				tape[xc]-=1
			tape[xc]+=1
			xc-=3
		tape[xc]+=1
		xc+=7
		while tape[xc]:
			tape[xc]-=1
			xc-=7
			tape[xc]-=1
			xc+=7
		tape[xc]+=1
		xc-=7
		while tape[xc]:
			tape[xc]-=1
			xc+=7
			tape[xc]-=1
			xc+=2
			while tape[xc]:
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc+=2
					tape[xc]+=1
					xc-=2
				xc+=4
			xc-=9
			while tape[xc]:
				xc+=1
				while tape[xc]:
					tape[xc]-=1
				xc-=1
				tape[xc]-=1
				xc+=7
				while tape[xc]:
					tape[xc]-=1
					xc-=7
					tape[xc]+=1
					xc+=1
					while tape[xc]:
						xc-=1
						tape[xc]-=1
						xc+=1
						tape[xc]-=1
						xc-=3
						tape[xc]+=1
						xc+=3
					xc-=1
					while tape[xc]:
						tape[xc]-=1
						xc+=1
						tape[xc]+=1
						xc-=1
					xc+=7
				xc-=6
				while tape[xc]:
					tape[xc]-=1
					xc+=6
					tape[xc]+=1
					xc-=6
				xc-=1
				tape[xc]+=1
				xc-=9
			xc+=1
			tape[xc]+=5
			while tape[xc]:
				tape[xc]-=1
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc+=9
			xc+=4
			tape[xc]+=1
			xc-=5
			while tape[xc]:
				xc-=9
			xc+=9
			while tape[xc]:
				xc+=5
				while tape[xc]:
					tape[xc]-=1
					xc-=5
					tape[xc]-=1
					xc+=5
				tape[xc]+=1
				xc-=5
				while tape[xc]:
					tape[xc]-=1
					xc+=5
					tape[xc]-=1
					xc+=2
					while tape[xc]:
						tape[xc]-=1
						xc-=7
						tape[xc]+=1
						xc+=7
					xc-=7
					while tape[xc]:
						tape[xc]-=1
						xc+=7
						tape[xc]+=1
						xc-=16
						while tape[xc]:
							xc-=9
						xc+=4
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc+=5
						while tape[xc]:
							xc+=9
						xc+=1
						tape[xc]+=1
						xc-=1
				tape[xc]+=1
				xc+=7
				while tape[xc]:
					tape[xc]-=1
					xc-=7
					tape[xc]-=1
					xc+=7
				tape[xc]+=1
				xc-=7
				while tape[xc]:
					tape[xc]-=1
					xc+=7
					tape[xc]-=1
					xc-=2
					while tape[xc]:
						tape[xc]-=1
						xc-=5
						tape[xc]+=1
						xc+=5
					xc-=5
					while tape[xc]:
						tape[xc]-=1
						xc+=5
						tape[xc]+=1
						xc-=14
						while tape[xc]:
							xc-=9
						xc+=3
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc+=6
						while tape[xc]:
							xc+=9
						xc+=1
						while tape[xc]:
							tape[xc]-=1
						tape[xc]+=1
						xc-=1
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					tape[xc]-=1
					xc-=1
					while tape[xc]:
						xc+=9
					xc-=8
				xc+=8
			xc-=9
			while tape[xc]:
				xc-=9
			xc+=4
			while tape[xc]:
				tape[xc]-=1
			xc-=3
			tape[xc]+=5
			while tape[xc]:
				tape[xc]-=1
				while tape[xc]:
					tape[xc]-=1
					xc+=9
					tape[xc]+=1
					xc-=9
				xc+=9
			xc+=4
			tape[xc]-=1
			xc-=5
			while tape[xc]:
				xc-=9
		xc+=3
	xc-=4
	stdout.write(chr(tape[xc])); stdout.flush()
	xc+=10
	while tape[xc]:
		xc+=6
		while tape[xc]:
			tape[xc]-=1
		xc+=3
	xc-=9
	while tape[xc]:
		xc-=9
	xc+=1
	tape[xc]+=10
	while tape[xc]:
		tape[xc]-=1
		while tape[xc]:
			tape[xc]-=1
			xc+=9
			tape[xc]+=1
			xc-=9
		xc+=9
	xc+=5
	tape[xc]+=1
	xc+=9
	tape[xc]+=1
	xc-=15
	while tape[xc]:
		xc-=9
	xc+=8
	while tape[xc]:
		tape[xc]-=1
		xc-=8
		tape[xc]+=1
		xc+=8
	xc-=8
	while tape[xc]:
		tape[xc]-=1
		xc+=8
		tape[xc]+=1
		while tape[xc]:
			tape[xc]-=1
		xc+=1
		while tape[xc]:
			xc+=9
		xc-=9
		while tape[xc]:
			xc+=8
			while tape[xc]:
				tape[xc]-=1
				xc-=7
				tape[xc]+=1
				xc+=7
			xc-=7
			while tape[xc]:
				tape[xc]-=1
				xc+=7
				tape[xc]+=1
				xc-=8
				while tape[xc]:
					xc-=9
				xc+=8
				while tape[xc]:
					tape[xc]-=1
				tape[xc]+=1
				xc+=2
			xc-=10
	xc+=8
	while tape[xc]:
		tape[xc]-=1
		xc-=8
		tape[xc]+=1
		xc+=8
	xc-=8
	while tape[xc]:
		tape[xc]-=1
		xc+=8
		tape[xc]+=1
		xc+=1
		while tape[xc]:
			xc+=1
			tape[xc]+=1
			xc+=5
			while tape[xc]:
				tape[xc]-=1
				xc-=5
				tape[xc]-=1
				xc+=5
			xc-=5
			while tape[xc]:
				tape[xc]-=1
				xc+=5
				tape[xc]+=1
				xc-=5
			xc+=8
		xc-=1
		tape[xc]+=1
		xc-=8
		while tape[xc]:
			xc+=6
			while tape[xc]:
				tape[xc]-=1
				xc+=2
				tape[xc]+=1
				xc-=2
			xc-=15
		xc+=9
		while tape[xc]:
			xc+=9
		xc-=9
		while tape[xc]:
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc-=1
			tape[xc]-=1
			xc+=8
			while tape[xc]:
				tape[xc]-=1
				xc-=8
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					xc-=1
					tape[xc]-=1
					xc+=1
					tape[xc]-=1
					xc-=2
					tape[xc]+=1
					xc+=2
				xc-=1
				while tape[xc]:
					tape[xc]-=1
					xc+=1
					tape[xc]+=1
					xc-=1
				xc+=8
			xc-=7
			while tape[xc]:
				tape[xc]-=1
				xc+=7
				tape[xc]+=1
				xc-=7
			xc-=1
			tape[xc]+=1
			xc-=9
		xc+=8
		tape[xc]-=1
		xc-=5
		while tape[xc]:
			tape[xc]-=1
		tape[xc]+=1
		xc-=3
	tape[xc]+=1
	xc+=8
	while tape[xc]:
		tape[xc]-=1
		xc-=8
		tape[xc]-=1
		xc+=8
	tape[xc]+=1
	xc-=8
	while tape[xc]:
		tape[xc]-=1
		xc+=8
		tape[xc]-=1
		xc+=1
		while tape[xc]:
			xc+=6
			while tape[xc]:
				tape[xc]-=1
				xc+=2
				tape[xc]+=1
				xc-=2
			xc+=3
		xc-=9
		while tape[xc]:
			xc+=1
			while tape[xc]:
				tape[xc]-=1
			xc-=1
			tape[xc]-=1
			xc+=8
			while tape[xc]:
				tape[xc]-=1
				xc-=8
				tape[xc]+=1
				xc+=1
				while tape[xc]:
					xc-=1
					tape[xc]-=1
					xc+=1
					tape[xc]-=1
					xc-=2
					tape[xc]+=1
					xc+=2
				xc-=1
				while tape[xc]:
					tape[xc]-=1
					xc+=1
					tape[xc]+=1
					xc-=1
				xc+=8
			xc-=7
			while tape[xc]:
				tape[xc]-=1
				xc+=7
				tape[xc]+=1
				xc-=7
			xc-=1
			tape[xc]+=1
			xc-=9
		xc+=1
		tape[xc]+=5
		while tape[xc]:
			tape[xc]-=1
			while tape[xc]:
				tape[xc]-=1
				xc+=9
				tape[xc]+=1
				xc-=9
			xc+=9
		xc+=5
		tape[xc]+=1
		xc+=27
		tape[xc]+=1
		xc-=6
		while tape[xc]:
			xc-=9
		xc+=9
		while tape[xc]:
			xc+=6
			while tape[xc]:
				tape[xc]-=1
				xc-=6
				tape[xc]-=1
				xc+=6
			tape[xc]+=1
			xc-=6
			while tape[xc]:
				tape[xc]-=1
				xc+=6
				tape[xc]-=1
				xc+=2
				while tape[xc]:
					tape[xc]-=1
					xc-=8
					tape[xc]+=1
					xc+=8
				xc-=8
				while tape[xc]:
					tape[xc]-=1
					xc+=8
					tape[xc]+=1
					xc-=17
					while tape[xc]:
						xc-=9
					xc+=4
					while tape[xc]:
						tape[xc]-=1
					tape[xc]+=1
					xc+=5
					while tape[xc]:
						xc+=9
					xc+=1
					tape[xc]+=1
					xc-=1
			tape[xc]+=1
			xc+=8
			while tape[xc]:
				tape[xc]-=1
				xc-=8
				tape[xc]-=1
				xc+=8
			tape[xc]+=1
			xc-=8
			while tape[xc]:
				tape[xc]-=1
				xc+=8
				tape[xc]-=1
				xc-=2
				while tape[xc]:
					tape[xc]-=1
					xc-=6
					tape[xc]+=1
					xc+=6
				xc-=6
				while tape[xc]:
					tape[xc]-=1
					xc+=6
					tape[xc]+=1
					xc-=15
					while tape[xc]:
						xc-=9
					xc+=3
					while tape[xc]:
						tape[xc]-=1
					tape[xc]+=1
					xc+=6
					while tape[xc]:
						xc+=9
					xc+=1
					while tape[xc]:
						tape[xc]-=1
					tape[xc]+=1
					xc-=1
			tape[xc]+=1
			xc+=1
			while tape[xc]:
				tape[xc]-=1
				xc-=1
				while tape[xc]:
					xc+=9
				xc-=8
			xc+=8
		xc-=9
		while tape[xc]:
			xc-=9
		xc+=4
		while tape[xc]:
			tape[xc]-=1
		xc-=3
		tape[xc]+=5
		while tape[xc]:
			tape[xc]-=1
			while tape[xc]:
				tape[xc]-=1
				xc+=9
				tape[xc]+=1
				xc-=9
			xc+=9
		xc+=5
		tape[xc]-=1
		xc+=27
		tape[xc]-=1
		xc-=6
		while tape[xc]:
			xc-=9
	xc+=3
