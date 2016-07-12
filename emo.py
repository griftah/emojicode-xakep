# coding=utf-8

# emo.py файл - сгенерирует аналогичный файл с расширением emojic и эмодзи.
# emo.py файл . - сгенерирует и запустит его.
# emo.py > текст - скомпилирует текст

import sys
import codecs
import os
import emoji

if __name__=='__main__':
    filename = sys.argv[1]
    if filename == '-':
        print emoji.emojize(u' '.join((c.decode('utf-8') for c in sys.argv[2:])))
        sys.exit(0)

    basename = filename.rsplit('.', 1)[0]
    src = codecs.open(filename, 'r', 'utf-8').read()
    src = emoji.emojize(src.replace('#', ':older_man:').replace(':abc::older_man::abc:', ':abc:#:abc:'), True)

    for n, line in enumerate(src.split('\n')):
        print n, '\t', line

    srcname = basename+'.emojic'
    with codecs.open(srcname, 'w', 'utf-8') as f:
        f.write(src)

    os.system('emojicodec %s'%srcname)

    if len(sys.argv)>2:
        os.system('emojicode %s'%basename+'.emojib')
