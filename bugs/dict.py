import subprocess

def pretty(dict):
    return ' '.join(['%d:%d'%(key, value) for key, value in dict.iteritems()])

def diff(a, b):
    return dict(set(b.items()) - set(a.items()) | set(a.items()) - set(b.items()))

d = old = {}
for line in subprocess.Popen('emojicode dict.emojib', shell=True, stdout=subprocess.PIPE).stdout.readlines():
    line = line.strip()
    if line:
        numbers = [int(x) for x in reversed(line.split(' '))]

        old = d.copy()

        key, value = numbers.pop(), numbers.pop()
        print 'dict[%d] = %d'%(key, value)

        while len(numbers):
            key, value = numbers.pop(), numbers.pop()
            d[key] = value

        print 'dict =', pretty(d)
        print 'diff =', pretty(diff(d, old))
        print
