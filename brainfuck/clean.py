#!/usr/bin/env python
# coding=utf-8

# Удаляет всё, что нагенерировали компиляторы.

from glob import glob
import os

for bf in glob('*.b'):
    for filename in glob(bf.replace('.b', '.*')):
        if not filename.endswith('.b'):
            print filename
            os.system('rm %s'%filename)

if os.path.exists('a.out'):
    print 'a.out'
    os.system('rm a.out')
