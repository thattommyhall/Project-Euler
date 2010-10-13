def S(width):
    s = '1'
    n = 2
    while 1:
        if len(s) < width:
            s += str(n)
            n += 1
            continue
        output = s[:width]
        s = s[1:]
        yield output


def when_n_times(generator, predicate, n):
    count = 0
    pos = 1
    while 1:
        next = generator.next()
        if predicate(next):
            count += 1
        if count == n:
            return pos
        pos += 1

def f(n):
    s = S(len(str(n)))
    return when_n_times(s, (lambda x: x == str(n)), n)

## print f(1)
## print f(5)
## print f(12)
## print f(7780)

tot = 0
for i in range(1,14):
    print i
    result = f(3**i)
    print result
    tot += result

print tot
        
    


