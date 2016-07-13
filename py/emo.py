#!/usr/bin/env python
# coding=utf-8

import sys
import codecs
import subprocess
import re
import emoji

if __name__=='__main__':
    if len(sys.argv)<2:
        print './emo.py file1.emojic.txt file2.emojic.txt file3.emojic.txt'
        print 'Преобразует в emojic и запускает последний.'
        print 'Если последний - точка, то прекращает без запуска.'
        exit(0)

    for filename in sys.argv[1:]:
        if filename=='.':
            exit(0)

        with codecs.open(filename, 'r', 'utf-8') as f:
            src = emoji.emojize(
                f.read().
                replace('#', ':older_man:').
                replace(':abc::older_man::abc:', ':abc:#:abc:'),
                True)

        basename = filename.rsplit('.', 2)[0]

        with codecs.open(basename+'.emojic', 'w', 'utf-8') as f:
            f.write(src)

        # компилирует только в том случае, если внутри есть флажок.
        if src.count(u'🏁'):
            try:
                subprocess.check_output(
                    'emojicodec %s.emojic'%basename,
                    stderr=subprocess.STDOUT, shell=True)
            except subprocess.CalledProcessError as err:
                # в случае ошибки показываем фрагмент исходника
                try:
                    where = int(re.match(
                        u'\xf0\x9f\x9a\xa8 line (\d+)',
                        err.output).group(1)
                    )
                    l = src.strip().split('\n')
                    for n in xrange(max(where-15, 0), min(where+15, len(l))):
                        print '%d %s\t%s'%(n+1, '>' if n==where-1 else '', l[n])
                except AttributeError:
                   pass
                print err.output
                exit(0)

    # исполняем последний файл в списке
    subprocess.call('emojicode %s.emojib'%basename, shell=True)
