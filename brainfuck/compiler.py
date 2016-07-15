# coding=utf-8

import codecs
import subprocess
import os

from brainfuck import Brainfuck

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
        self.output = []

    # переводит на другой язык и сохраняет в файл f
    def write(self, f):
        indent = 0
        def w(f, src, indent):
            if src:
                f.write((u'\n'+src).replace(u'\n', u'\n'+u'\t'*indent))

        for char, arg in self.code:
            try:
                src, src_arg, tabs = self.commands[char]
                if tabs:
                    w(f, src, indent)
                    indent+=tabs
                elif arg>1:
                    w(f, src_arg%arg, indent)
                else:
                    w(f, src, indent)
            except KeyError:
                pass
        f.write('\n')

    # загружает, переводить в другой язык, запускает внешние компиляторы
    def compile(self, name, optimize=True):
        # загружает из файла
        with codecs.open(name, 'r', 'utf-8') as f:
            self.load(f.read(), optimize)
        # переводим брейнфак в другой язык
        self.output = [(name[:-2] if name.endswith('.b') else name)+self.ext]
        with codecs.open(self.output[-1], 'w', 'utf-8') as f:
            self.write(f)
        # запускаем внешние компиляторы
        self.prepare()

    def prepare(self): pass

    def run(self):
        if self.output: # работает только после compile
            subprocess.call(self.run_cmd%self.output[-1], shell=True)

    # Удаление сгенерированных файлов
    def clean(self):
        for name in self.output:
            if os.path.exists(name):
                subprocess.call(u'rm %s'%name, shell=True)


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
    ext = '.py'
    run_cmd = 'python %s'


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
    ext = '.emojic'
    run_cmd = 'emojicode %s'

    def prepare(self):
        subprocess.call('emojicodec %s'%self.output[-1], shell=True)
        self.output.append(self.output[-1].replace('.emojic', '.emojib'))


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
        'end': (u'return 0;\n}', None, -1)
    }
    ext = '.c'
    run_cmd = './%s'

    def prepare(self):
        self.output.append(self.output[-1].replace('.c', '.out'))
        subprocess.call('cc %s -o %s'%(self.output[-2], self.output[-1]), shell=True)


class JavascriptCompiler(Compiler):
    commands = {
        'begin': (u'''// Автоматически скомпилировано из Brainfuck.
stdout = process.stdout
tape = Array.apply(null, Array(32000)).map(Number.prototype.valueOf,0);
xc = 0''', None, 0),
        '+': (u'tape[xc]++;', u'tape[xc]+=%d;', 0),
        '-': (u'tape[xc]--;', u'tape[xc]-=%d;', 0),
        '.': (u'stdout.write(String.fromCharCode(tape[xc]));', None, 0),
        '>': (u'xc++;', u'xc+=%d;', 0),
        '<': (u'xc--;', u'xc-=%d;', 0),
        '[': (u'while (tape[xc]) {', None, 1),
        ']': (u'}', None, -1),
        'end': (u'stdout.write("\\r");', None, -1)
    }
    ext = '.js'
    run_cmd = 'node %s'


class RubyCompiler(Compiler):
    commands = {
        'begin': (u'''# Автоматически скомпилировано из Brainfuck.
tape = Array.new(32000, 0)
xc = 0''', None, 0),
        '+': (u'tape[xc]+=%d', None, 0),
        '-': (u'tape[xc]-=%d', None, 0),
        '.': (u'STDOUT.write(tape[xc].chr)', None, 0),
        '>': (u'xc+=%d', None, 0),
        '<': (u'xc-=%d', None, 0),
        '[': (u'while tape[xc]!=0 do', None, 1),
        ']': (u'end', None, -1)
    }
    ext = '.rb'
    run_cmd = 'ruby %s'


class JavaCompiler(Compiler):
    commands = {
        'begin': (u'''
public class Brainfuck {
   public static void main(String[] args) {
      int[] tape = new int[32000];
      int xc = 0;
      java.util.Arrays.fill(tape, 0);
''', None, 2),
        '+': (u'tape[xc]++;', u'tape[xc]+=%d;', 0),
        '-': (u'tape[xc]--;', u'tape[xc]-=%d;', 0),
        '.': (u'System.out.print((char)tape[xc]);', None, 0),
        '>': (u'xc++;', u'xc+=%d;', 0),
        '<': (u'xc--;', u'xc-=%d;', 0),
        '[': (u'while (tape[xc]!=0) {', None, 1),
        ']': (u'}', None, -1),
        'end': (u'\n}\n}', None, -2)
    }
    ext = '.java'
    run_cmd = 'java %s'

    def prepare(self):
        subprocess.call('mv %s Brainfuck.java'%self.output.pop(), shell=True)
        subprocess.call('javac Brainfuck.java', shell=True)
        self.output = ['Brainfuck.java', 'Brainfuck.class', 'Brainfuck']
