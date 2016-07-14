# coding=utf-8

# Компилятор Brainfuck

import sys, os, codecs
# import emoji

class Command(object):
    # cmd - команда Brainfuck
    # code - обычный код
    # code_repeat - код команды, повторяющейся несколько раз
    # indent - изменения сдвига в ту или другую сторону.
    def __init__(self, code, code_repeat = None, indent=0):
        n = code.count('%d') if code else 0
        self.code = code%1 if n else code

        self.code_repeat = code_repeat if code_repeat else code
        self.dont_repeat = indent or not self.code_repeat.count('%d')

        self.indent = indent


# Компилирует Brainfuck в заданный язык.
class Compiler(object):
    # Словарь команд.
    # Ключ - команда Brainfuck.
    # Значение - соответствующий код.
    # 'begin' и 'end' - код в начале и конце программы.

    def __init__(self, indent=0):
        self.commands = {}
        self.lines = []
        self.tabs = indent

    # Определить код команды
    def define(self, cmd, code, code_repeat = None, indent=0):
        self.commands[cmd] = Command(code, code_repeat, indent)

    # Записывает строку
    def write(self, line):
        if line:
            tabs = '\t'*self.tabs
            self.lines.append(tabs+line.replace('\n', '\n'+tabs))

    # Добавляет код для команды
    def add(self, c):
        try:
            cmd = self.commands[c]
            self.write(cmd.code)
            self.tabs+=cmd.indent
            return cmd
        except KeyError:
            return None

    # Принимает Brainfuck, отдаёт готовый код на нужном языке.ы
    def compile(self, code):
        self.add('begin')
        for cmd in code:
            self.add(cmd)
        self.add('end')
        self.lines.append('')
        return '\n'.join(self.lines)


# Компилирует и одновременно оптимизирует, складывая повторяющиеся команды.
class Collector(Compiler):
    def __init__(self, indent=0):
        super(self.__class__, self).__init__(indent)
        self.prev_cmd = ''
        self.repeat = 0 # количество повторов прошлой команды

    # Добавляет, сливая повторяющиеся команды
    def add(self, c):
        if c==self.prev_cmd:
            cmd = self.commands[c] # проверка наличия ключа была в прошлый раз
            if cmd.dont_repeat:
                super(self.__class__, self).add(c)
            else:
                del self.lines[-1]
                self.repeat+=1
                self.write(cmd.code_repeat%self.repeat)
            return cmd
        else:
            cmd = super(self.__class__, self).add(c)
            if cmd:
                self.prev_cmd = c
                self.repeat = 1
            return cmd


# Скомпилировать брейнфак в питон.
def py_compile(code, f=sys.stdout,  optimize = False):
    w = Compiler() if optimize else Collector()
    w.define('begin', u'''
# coding=utf-8
# Создано bf-compiler.py из исходника на Brainfuck.
import sys
tape = [0]*32000
xc = 0
''')
    w.define('+', u'tape[xc]+=%d')
    w.define('-', u'tape[xc]-=%d')
    w.define('.', u'sys.stdout.write(chr(tape[xc]))') #; sys.stdout.flush()')
    w.define('>', u'xc+=%d')
    w.define('<', u'xc-=%d')
    w.define('[', u'while tape[xc]:', indent=1)
    w.define(']', None, indent=-1)
    f.write(w.compile(code))


# Скомпилировать брейнфак в эмодзикод.
def emo_compile(code, f=sys.stdout,  optimize = False):
    w = Collector() if optimize else Compiler()
    w.define('begin', u'''
:older_man: Создано bf-compiler.py из исходника на Brainfuck.

:package: files :red_circle:

:older_man: аналог chr в питоне
:whale2: :steam_locomotive: :grapes:
    :pig2: :tophat: :arrow_right: :symbols: :grapes:
        :apple: :beer: :microscope: :abc:?????????:x:t:x:n??:x:r?????????????????? !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~:abc: :dog2:
    :watermelon:
:watermelon:

:checkered_flag: :grapes:
    :icecream: stdout :doughnut::outbox_tray::page_facing_up:
    :older_man: :icecream: tape :ice_cream: 0 :eggplant:
    :icecream: tape :large_blue_diamond: :ice_cream::shell::steam_locomotive: :frog:
    :custard: xc 0

    :repeat_one: i :fast_forward: 1 32000 :grapes:
        :bear: tape 0
    :watermelon:

''', indent=1)
    w.define('+', u':pig: tape xc :heavy_plus_sign: :beer: :pig_nose: tape xc %d')
    w.define('-', u':pig: tape xc :heavy_minus_sign: :beer: :pig_nose: tape xc %d')
    w.define('.', u':pencil2: stdout :card_index: :abcd: :tophat: :beer: :pig_nose: tape xc')
    w.define('>', u':chocolate_bar: xc', u':custard: xc :heavy_plus_sign: xc %d')
    w.define('<', u'\t:cooking: xc', u':custard: xc :heavy_minus_sign: xc %d')
    w.define('[', u':repeat: :negative_squared_cross_mark: :stuck_out_tongue: :beer: :pig_nose: tape xc 0 :grapes:', indent=1)
    w.define(']', u':watermelon:', indent=-1)
    w.define('end', u':watermelon:', indent=-1)
    # f.write(emoji.emojize(w.compile(code), True))

if __name__=='__main__':
    if len(sys.argv)>1:
        filename = sys.argv[1]
        base = filename.rsplit('.', 1)[0]
        brainfuck = open(filename).read()
        with codecs.open(base+'.py', 'w', 'utf-8') as f:
            py_compile(brainfuck, f, True)
        with codecs.open(base+'.emojic', 'w', 'utf-8') as f:
            emo_compile(brainfuck, f, True)
    else:
        py_compile("""
        ++++++++[>+++++++++<-]>.<+++++[>++++++<-]>-.+++++++..+++.<
++++++++[>>++++<<-]>>.<<++++[>------<-]>.<++++[>++++++<-]>
.+++.------.--------.>+.""", optimize=True)
