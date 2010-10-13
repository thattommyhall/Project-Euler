from __future__ import division 
from collections import defaultdict
from time import time
import psyco
psyco.full()

start = time()
counter = defaultdict(list)

def triples():
    for q in range(1, 35):
        for p in range(q+1, 35):
            a = p**2 - q**2
            b = 2 * p * q
            c = p**2 + q**2
            for m in range(1,int(1000/c)):
                yield (m*min(a,b),m*max(a,b), m*c)
                
for triple in triples():
    perimeter = sum(triple)
    if perimeter < 1001:
        counter[perimeter] += [triple]
        
print set((counter[120]))

maxlen = 1
for i in counter:
    if len(set(counter[i])) > maxlen:
        maxlen = len(set(counter[i]))
        print i
end = time()

print "took ", end-start

