#!/usr/bin/env python
# coding=utf-8

import sys

class Brainfuck(object):
    def __init__(self, brainfuck=None, optimize=True):
        if brainfuck:
            self.load(brainfuck, optimize)

    def load(self, brainfuck, optimize=True):
        chars = ['begin']
        args = [1]
        brackets = []
        for char in brainfuck:
            if char in '[]<>.,+-':
                if optimize and char in '<>+-' and char==chars[-1]:
                    args[-1]+=1
                else:
                    chars.append(char); args.append(1)
                    if char=='[':
                        brackets.append(len(chars)-1)
                    elif char==']':
                        left = brackets.pop()
                        args[left] = len(chars)-1
                        args[-1] = left
        chars.append('end'); args.append(1)
        self.code = zip(chars, args)

    def run(self):
        code = self.code
        tape = [0]*30000
        pc = xc = 0
        prog_len = len(code)
        while pc<prog_len:
            char, arg = code[pc]
            if char=='+':
                tape[xc]+=arg
            elif char=='-':
                tape[xc]-=arg
            elif char=='>':
                xc+=arg
            elif char=='<':
                xc-=arg
            elif char=='.':
                sys.stdout.write(chr(tape[xc]))
                sys.stdout.flush()
            elif char==']' and tape[xc]:
                pc = arg
            elif char=='[' and tape[xc]==0:
                pc = arg
            pc+=1


class Compiler(Brainfuck):
    # Определение команды commands[char] = (src, src_arg, indent)
    # src - исходник команды Brainfuck на другом языке.
    # src_arg - исходник команды с аргументом. требует %d
    # tabs - сдвиг.
    commands = {}

    def __init__(self, brainfuck=None, optimize=True):
        super(Compiler, self).__init__(brainfuck, optimize)
        for char, (src, src_arg, tabs) in self.commands.iteritems():
            src_has_arg = src.find('%d')>0 if src else 0
            self.commands[char] = (
                src%1 if src_has_arg else src,
                src_arg if src_arg else src,
                tabs
            )

    def write(self, f, src, indent):
        if src:
            f.write((u'\n'+src).replace(u'\n', u'\n'+u'\t'*indent))

    def compile(self, f):
        indent = 0
        for char, arg in self.code:
            try:
                src, src_arg, tabs = self.commands[char]
                if tabs:
                    self.write(f, src, indent)
                    indent+=tabs
                elif arg>1:
                    self.write(f, src_arg%arg, indent)
                else:
                    self.write(f, src, indent)
            except KeyError:
                pass
        f.write('\n')


class PythonCompiler(Compiler):
    commands = {
        'begin': (u'''# coding=utf-8
# Автоматически скомпилировано из Brainfuck.
from sys import stdout
tape = [0]*32000
xc = 0''', None, 0),
        '+': (u'tape[xc]+=%d', None, 0),
        '-': (u'tape[xc]-=%d', None, 0),
        '.': (u'stdout.write(chr(tape[xc])); stdout.flush()', None, 0),
        '>': (u'xc+=%d', None, 0),
        '<': (u'xc-=%d', None, 0),
        '[': (u'while tape[xc]:', None, 1),
        ']': (None, None, -1)
    }


class EmojicodeCompiler(Compiler):
    commands = {
        'begin': (u'''👴 Автоматически скомпилировано из Brainfuck.
📦 files 🔴

🐋 🚂 🍇
    🐖 🎩 ➡ 🔣 🍇
        🍎 🍺 🔬 🔤?????????❌t❌n??❌r?????????????????? !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~🔤 🐕
    🍉
🍉

🏁 🍇
    🍦 stdout 🍩📤📄
    🍦 tape 🔷 🍨🐚🚂 🐧 32000
    🍮 xc 0

    🔂 i ⏩ 1 32000 🍇
        🐻 tape 0
    🍉
''', None, 1),
        '+': (u'🐷 tape xc ➕ 🍺 🐽 tape xc %d', None, 0),
        '-': (u'🐷 tape xc ➖ 🍺 🐽 tape xc %d', None, 0),
        '.': (u'✏ stdout 📇 🔡 🎩 🍺 🐽 tape xc', None, 0),
        '>': (u'🍫 xc', u'🍮 xc ➕ xc %d', 0),
        '<': (u'🍳 xc', u'🍮 xc ➖ xc %d', 0),
        '[': (u'🔁 ❎ 😛 🍺 🐽 tape xc 0 🍇', None, 1),
        ']': (u'🍉', None, -1),
        'end': (u'🍉', None, -1)
    }


class CCompiler(Compiler):
    commands = {
        'begin': (u'''/* Автоматически скомпилировано из Brainfuck. */
#include <stdio.h>
int main(int argc, char **argv) {
    int tape[32768];
    int xc = 0;
''', None, 1),
        '+': (u'tape[xc]++;', u'tape[xc]+=%d;', 0),
        '-': (u'tape[xc]--;', u'tape[xc]-=%d;', 0),
        '.': (u'putchar(tape[xc]);', None, 0),
        '>': (u'xc++;', u'xc+=%d;', 0),
        '<': (u'xc--;', u'xc-=%d;', 0),
        '[': (u'while (tape[xc]) {', None, 1),
        ']': (u'}', None, -1),
        'end': (u'putchar(10); return 0; }', None, -1)
    }



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
