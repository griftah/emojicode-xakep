#!/usr/bin/env python
# coding=utf-8

import sys
import codecs
import timeit

from compiler import *
from clean import clean

class PythonInterpreter(Brainfuck):
    def compile(self, name, optimize=True):
        with codecs.open(name, 'r', 'utf-8') as f:
            self.load(f.read(), optimize)

    def clean(self): pass

class EmojicodeInterpreter(Compiler):
    run_cmd = u'emojicode brainfuck.emojib %s'

    def compile(self, name, optimize=True):
        if optimize:
            self.run_cmd = u'emojicode brainfuck.emojib -o %s'
        self.output = [name]

    def clean(self): pass


brainfucks = {
    'pyi':        (PythonInterpreter, 'Python Interpreter'),
    'eci':        (EmojicodeInterpreter, 'Emojicode Interpreter'),
    'emojicode':  (EmojicodeCompiler, 'Emojicode Compiler'),
    'python':     (PythonCompiler, 'Python Compiler'),
    'ruby':       (RubyCompiler, 'Ruby Compiler'),
    'javascript': (JavascriptCompiler, 'Javascript Compiler'),
    'c':          (CCompiler, 'C Compiler'),
    'java':       (JavaCompiler, 'Java Compiler'),
    'profiler':   (Profiler, 'Profiler'),
}

# Запустить один интерпретатор
def run(filename, optimize, lang, justsave=False):
    bf_cls, bf_name = brainfucks[lang]
    bf = bf_cls()
    bf.compile(filename, optimize)
    if justsave:
        print filename, '->', ' -> '.join(bf.output)
        return (0, '', False)
    else:
        t = bf.time()
        bf.clean()
        print 't = %.3f s\t'%t,
        print 'Brainfuck %s'%bf_name,
        print 'with optimization' if optimize else ''
        return t, bf_name, optimize

def runall(filename):
    results = []
    try:
        for lang in brainfucks.iterkeys():
            t, bf_name, optimize = run(filename, False, lang)
            t_opt = run(filename, True, lang)[0]
            results.append((t, t_opt, bf_name))
    except KeyboardInterrupt:
        print
        clean()
    print '-'*40
    print 't\tt opt\ttitle'
    for result in sorted(results, key=lambda a: a[0]):
        if t:
            print '%.3f\t%.3f\t%s'%result

if __name__=='__main__':
    filename = None
    optimize = False
    lang = 'pyi'
    justsave = False # только сохранить, не запускать
    for arg in sys.argv[1:]:
        if arg=='-o':
            optimize = True
        elif arg=='.':
            justsave = True
        elif arg=='all':
            lang = arg
        elif arg.endswith('.b'):
            filename = arg
        elif brainfucks.has_key(arg):
            lang = arg

    if filename:
        if lang=='all':
            runall(filename)
        else:
            run(filename, optimize, lang, justsave)
    else:
        for example, comment in (
            ('%s source.b', 'исполнить интерпретатором на Python'),
            ('%s -o source.b', '-o включает оптимизацию'),
            ('%s python source.b .', 'сохранить исходник и не запускать'),
        ):
            print (example%__file__).ljust(35), comment
        for arg in sorted(brainfucks.iterkeys()):
            bf, bf_name = brainfucks[arg]
            print ('%s %s source.b'%(__file__, arg)).ljust(35), bf_name
