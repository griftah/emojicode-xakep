# coding=utf-8

# emo.py файл - сгенерирует аналогичный файл с расширением emojic и эмодзи.
# emo.py файл . - сгенерирует и запустит его.
# emo.py > текст - скомпилирует текст

import sys
import codecs
# import os
import subprocess
import emoji

if __name__=='__main__':
    filename = sys.argv[1]
    if filename == '-':
        print emoji.emojize(u' '.join((c.decode('utf-8') for c in sys.argv[2:])))
        sys.exit(0)

    basename = filename.rsplit('.', 2)[0]
    with codecs.open(filename, 'r', 'utf-8') as f:
        src = emoji.emojize(f.read().replace('#', ':older_man:').replace(':abc::older_man::abc:', ':abc:#:abc:'), True)

    with codecs.open(basename+'.emojic', 'w', 'utf-8') as f:
        f.write(src)

    if src.count(u'🏁'):
        try:
            subprocess.check_output('emojicodec %s.emojic'%basename, stderr=subprocess.STDOUT, shell=True)
            if len(sys.argv)<3:
                subprocess.call('emojicode %s.emojib'%basename, shell=True)
        except subprocess.CalledProcessError as err:
            for n, line in enumerate(src.strip().split('\n')):
                print n, '\t', line
            print err.output

