S = open('S.txt','r').read()

def f(n):
    count = 0
    pos = 0
    strn = str(n)
    while 1:
        pos = S.find(strn, pos+1)
        if pos == -1:
            print 'failed'
            return 0
        print 'found at', pos
        count += 1
        if count == n:
            return pos

print f(1)
print f(5)
print f(12)
print f(7780)

