from __future__ import division 

from helper import count_gen
import itertools

def test(x,y,n):
    return 1/x + 1/y == 1/n
    
print test(5,20,4)

def is_int(x):
    return x == int(x)

def gen_triples(n):
    for x in range(n+1,2*n+1):
        y = (n*x)/(x-n)
        if is_int(y):
            yield (x,y)

def howmany(n):
    return count_gen(gen_triples(n))        

print howmany(4)

max = 0
for i in itertools.count(1):
    result = howmany(i)
    if result > max:
        print result
        max = result
    if result > 1000:
        print i
        break
    
