#!/usr/bin/env python
# coding=utf-8

# Удаляет всё, что нагенерировали компиляторы.

from glob import glob
import os

def clean():
    path = os.path.dirname(__file__)

    for bf in glob('%s/*.b'%path):
        for filename in glob(bf.replace('.b', '.*')):
            if not filename.endswith('.b'):
                print filename
                os.remove(filename)

    for filename in ('a.out', 'Brainfuck.java', 'Brainfuck.class'):
        if os.path.exists(filename):
            print filename
            os.remove(filename)

if __name__=='__main__':
    clean()
