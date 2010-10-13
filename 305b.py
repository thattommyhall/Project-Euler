import time
from helper import timed


def S():
    offset = 0
    count = 1
    old_s = ''
    while 1:
        s = ''
        for i in range((count-1)*10000000,count*10000000):
            s += str(i)    
        count += 1
        ## trail = old_s[-7:]
        old_s = s
        yield offset, s 
        ## print 'upping offset'
        offset = offset + len(s)
        ## print 'offset is', offset

@timed
def f(n):
    s = S()
    count = 0
    strn = str(n)
    while 1:
        pos = 0
        offset, nextstr = s.next()
        ## print 'got next'
        while 1:
            pos = nextstr.find(strn, pos+1)
            if pos == -1:
                break
            count += 1
            if count == n:
                return offset + pos

print f(1)
print f(5)
print f(12)
print f(7780)

tot = 0
for i in range(1,14):
    res = f(3**i)
    print i, res
    tot += res

print tot
