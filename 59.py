import itertools
import string
import operator

letters = string.ascii_lowercase[::-1]
code = map (int,open('cipher1.txt','r').read().split(','))
words = open('/usr/share/dict/words','r').readlines()
words = [string.strip(i) for i in words]


def decode(somecode,key):
    key = [ord(k) for k in key]
    #somecode = [ord(k) for k in somecode]
    output = ""
    for i,j in itertools.izip(somecode,itertools.cycle(key)):
        letter = chr(operator.xor(i,j))
        output += letter
    return output

for i in letters:
    print i
    for j in letters:
        for k in letters:
            key = i+j+k
            dec = decode(code,key)
            totwords = 0
            for word in dec.split():
                if word in words:
                    totwords += 1
            if totwords > 10:
                print dec
                print i,j,k
