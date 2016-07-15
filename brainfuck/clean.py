#!/usr/bin/env python
# coding=utf-8

# Удаляет всё, что нагенерировали компиляторы.

from glob import glob
import os

path = os.path.dirname(__file__)

for bf in glob('%s/*.b'%path):
    for filename in glob(bf.replace('.b', '.*')):
        if not filename.endswith('.b'):
            print filename
            os.system('rm %s'%filename)

for name in ('a.out', 'Brainfuck.java', 'Brainfuck.class'):
    if os.path.exists(name):
        print name
        os.system('rm %s'%name)
