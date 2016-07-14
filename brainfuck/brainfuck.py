#!/usr/bin/env python
# coding=utf-8

import sys

class Command(object):
    def __init__(self, char):
        self.char = char
        self.arg = 1

    def __repr__(self):
        return '%s:%d'%(self.char, self.arg)


class Brainfuck(object):
    def __init__(self, brainfuck=None, optimize=True):
        self.code = []
        if brainfuck:
            self.load(brainfuck, optimize)

    def load(self, brainfuck, optimize=True):
        braces = []
        self.code = code = [Command('begin')]
        for char in brainfuck:
            if char in '[]<>.,+-':
                if optimize and char in '<>+-' and char==code[-1].char:
                    code[-1].arg+=1
                else:
                    code.append(Command(char))
                    if char=='[':
                        braces.append(len(code)-1)
                    elif char==']':
                        left = braces.pop()
                        code[left].arg = len(code)-1
                        code[-1].arg = left
        self.code.append(Command('end'))

    def run(self):
        tape = [0]*30000
        xc = 0
        pc = 0
        code = self.code
        prog_len = len(code)
        while pc<prog_len:
            cmd = code[pc]
            if cmd.char=='+':
                tape[xc]+=cmd.arg
            elif cmd.char=='-':
                tape[xc]-=cmd.arg
            elif cmd.char=='>':
                xc+=cmd.arg
            elif cmd.char=='<':
                xc-=cmd.arg
            elif cmd.char=='.':
                sys.stdout.write(chr(tape[xc]))
                sys.stdout.flush()
            elif cmd.char==']' and tape[xc]!=0:
                pc = cmd.arg
            elif cmd.char=='[' and tape[xc]==0:
                pc = cmd.arg
            pc+=1


class Compiler(Brainfuck):
    def __init__(self, brainfuck=None, optimize=True):
        super(Compiler, self).__init__(brainfuck, optimize)
        self.commands = {}
        self.define_lang()

    # Определение команды на другом языке
    class Definition(object):
        # src - исходник команды Brainfuck на другом языке.
        # src_opt - исходник команды с аргументом. требует %d
        # indent - сдвиг.
        def __init__(self, src, src_arg, indent):
            src_has_arg = src.count('%d') if src else 0
            self.src = src%1 if src_has_arg else src
            self.src_arg = src_arg if src_arg else src
            self.indent = indent

    def define(self, char, src, src_arg=None, indent=0):
        self.commands[char] = Compiler.Definition(src, src_arg, indent)

    # Определение соответствий команд Brainfuck конкретному языку
    def define_lang(self):
        pass

    def write(self, f, src, indent):
        if src:
            f.write((u'\n'+src).replace(u'\n', u'\n'+u'\t'*indent))

    def compile(self, f):
        indent = 0
        for cmd in self.code:
            try:
                d = self.commands[cmd.char]
                if d.indent:
                    self.write(f, d.src, indent)
                    indent+=d.indent
                elif cmd.arg>1:
                    self.write(f, d.src_arg%cmd.arg, indent)
                else:
                    self.write(f, d.src, indent)
            except KeyError:
                pass


class PythonCompiler(Compiler):
    def define_lang(self):
        self.define('begin',
u'''# coding=utf-8
# Автоматически скомпилировано из Brainfuck.
from sys import stdout
tape = [0]*32000
xc = 0
''')
        self.define('+', u'tape[xc]+=%d')
        self.define('-', u'tape[xc]-=%d')
        self.define('.', u'stdout.write(chr(tape[xc])); stdout.flush()')
        self.define('>', u'xc+=%d')
        self.define('<', u'xc-=%d')
        self.define('[', u'while tape[xc]:', indent=1)
        self.define(']', None, indent=-1)


if __name__=='__main__':
    import codecs
    import subprocess
    import time

    source_filename = None
    optimize = False
    compiler = None
    ext = ''            # расширение нового файла
    run = True          # исполнять
    run_command = None  # команда для запуска скомпилированого файла
    t = 0

    for arg in sys.argv[1:]:
        if arg=='-o':
            optimize = True
        elif arg=='.':
            run = False
        elif arg=='python':
            compiler = PythonCompiler
            ext = '.py'
            run_command = u'python %s'
        elif arg.endswith('.b'):
            source_filename = arg

    if source_filename:
        with codecs.open(source_filename, 'r', 'utf-8') as f:
            source = f.read()

        import os

        if compiler:
            output_filename = source_filename.replace('.b', ext)
            with codecs.open(output_filename, 'w', 'utf-8') as f:
                compiler(source, optimize).compile(f)
                if run_command and run:
                    t0 = time.clock()
                    subprocess.call(run_command%output_filename, shell=True)
                    t = time.clock()-t0
                    subprocess.call(u'rm %s'%output_filename, shell=True)
                else:
                    print source_filename, '->', output_filename
        else:
            t0 = time.clock()
            Brainfuck(source, optimize).run()
            t = time.clock()-t0

        if t:
            print '\nt =', t, 's'
    else:
        for example, comment in (
            ('%s source.b', 'исполнить source.b интерпретатором'),
            ('%s -o source.b', '-o включает оптимизацию'),
            ('%s python source.b', 'перевести на Python и запустить'),
            ('%s emojicode source.b', 'перевести на Emojicode и запустить'),
            ('%s c source.b', 'перевести на C и запустить'),
            ('%s python source.b .', 'сохранить исходник и не запускать'),
        ):
            print example.ljust(25)%__file__, comment
