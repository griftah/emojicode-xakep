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
        f.write('\n')


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


class EmojicodeCompiler(Compiler):
    def define_lang(self):
        self.define('begin',
u'''👴 Автоматически скомпилировано из Brainfuck.
📦 files 🔴

🐋 🚂 🍇
    🐖 🎩 ➡ 🔣 🍇
        🍎 🍺 🔬 🔤?????????❌t❌n??❌r?????????????????? !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~🔤 🐕
    🍉
🍉

🏁 🍇
    🍦 stdout 🍩📤📄
    👴 🍦 tape 🍨 0 🍆
    🍦 tape 🔷 🍨🐚🚂 🐸
    🍮 xc 0

    🔂 i ⏩ 1 32000 🍇
        🐻 tape 0
    🍉
''', indent=1)
        self.define('+', u'🐷 tape xc ➕ 🍺 🐽 tape xc %d')
        self.define('-', u'🐷 tape xc ➖ 🍺 🐽 tape xc %d')
        self.define('.', u'✏ stdout 📇 🔡 🎩 🍺 🐽 tape xc')
        self.define('>', u'🍫 xc', u'🍮 xc ➕ xc %d')
        self.define('<', u'🍳 xc', u'🍮 xc ➖ xc %d')
        self.define('[', u'🔁 ❎ 😛 🍺 🐽 tape xc 0 🍇', indent=1)
        self.define(']', u'🍉', indent=-1)
        self.define('end', u'🍉', indent=-1)


class CCompiler(Compiler):
    def define_lang(self):
        self.define('begin',
u'''/* Автоматически скомпилировано из Brainfuck. */
#include <stdio.h>
int main(int argc, char **argv) {
    int tape[32768];
    int xc = 0;
''', indent=1)
        self.define('+', u'tape[xc]++;', u'tape[xc]+=%d;')
        self.define('-', u'tape[xc]--;', u'tape[xc]-=%d;')
        self.define('.', u'putchar(tape[xc]);')
        self.define('>', u'xc++;', u'xc+=%d;')
        self.define('<', u'xc--;', u'xc-=%d;')
        self.define('[', u'while (tape[xc]) {', indent=1)
        self.define(']', u'}', indent=-1)
        self.define('end', u'putchar(10); return 0; }', indent=-1)


if __name__=='__main__':
    import codecs
    import subprocess
    from timeit import default_timer as timer

    source_filename = None
    optimize = False
    lang = None
    run = True          # исполнять
    t = 0

    compilers = {
        'python':    ( PythonCompiler, '.py', 'python %s'),
        'emojicode': ( EmojicodeCompiler, '.emojic', 'emojicode %s'),
        'c':         ( CCompiler, '.c', './%s')
    }

    for arg in sys.argv[1:]:
        if arg=='-o':
            optimize = True
        elif arg=='.':
            run = False
        elif arg.endswith('.b'):
            source_filename = arg
        elif compilers.has_key(arg):
            lang = arg

    if source_filename:
        with codecs.open(source_filename, 'r', 'utf-8') as f:
            source = f.read()
        if lang:
            compiler, ext, run_cmd = compilers[lang]

            # компиляция
            output = [source_filename.replace('.b', ext)]
            with codecs.open(output[-1], 'w', 'utf-8') as f:
                compiler(source, optimize).compile(f)

            # создание исполняемых файлов
            if lang=='emojicode':
                subprocess.call('emojicodec %s'%output[-1], shell=True)
                output.append(source_filename.replace('.b', '.emojib'))
            elif lang=='c':
                output.append(source_filename.replace('.b', '.out'))
                subprocess.call(
                    'cc %s -o %s'%(output[0], output[1]), shell=True)

            # запуск
            if run:
                t0 = timer()
                subprocess.call(run_cmd%output[-1], shell=True)
                t = timer()-t0
                # Удаление сгенерированных файлов
                for name in output:
                    subprocess.call(u'rm %s'%name, shell=True)
            else:
                print source_filename, '->', ' -> '.join(output)
        else:
            t0 = timer()
            Brainfuck(source, optimize).run()
            t = timer()-t0

        # время работы
        if t:
            print '\nt = %.3f s'%t
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
