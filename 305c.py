import time

def timed(fn):
    def wrapper(*arg):
        start = time.time()
        print 'running ', fn.__name__, str(*arg)
        result = fn(*arg)
        stop = time.time()
        print 'took', stop-start
        return result
    return wrapper

def bmsearch(pattern, text, pos):
    m = len(pattern)
    n = len(text)
    if m > n: return -1
    skip = []
    for k in range(256): skip.append(m)
    for k in range(m - 1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1

def S():
    offset = 0
    count = 1
    old_s = ''
    while 1:
        s = ''
        for i in range((count-1)*1000000,count*1000000):
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
            pos = bmsearch(strn, nextstr, pos+1)
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
