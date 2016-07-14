# coding=utf-8

# делаем список эмодзи в виде CSV

import codecs
import emoji

emoji.EMOJI_UNICODE.update(emoji.EMOJI_ALIAS_UNICODE)

with codecs.open('emoji.txt', 'w', 'utf-8') as f:
    for name in sorted(emoji.EMOJI_UNICODE.keys()):
        c = emoji.EMOJI_UNICODE[name]
        name = name.replace(':', '').replace('_', ' ')
        print >> f, '%s\t%s'%(c, name)
