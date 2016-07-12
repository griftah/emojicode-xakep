abc = [ chr(i) if i>31 else '?' for i in range(128) ]
abc[ord('\n')]=':x:n'
abc[ord('\t')]=':x:t'
abc[ord('\r')]=':x:r'
print ':abc:%s:abc:'%''.join(abc)
