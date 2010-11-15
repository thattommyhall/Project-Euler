from __future__ import division 
from collections import defaultdict
from time import time
import math

import psyco
psyco.full()

start = time()


def triples(maxperimeter=100):
    root = math.sqrt(maxperimeter)
    for q in range(1, root):
        for p in range(q+1, root):
            a = p**2 - q**2
            b = 2 * p * q
            c = p**2 + q**2
            for m in range(1,int(maxperimeter/c)):
                yield (m*min(a,b),m*max(a,b), m*c)
        

count = 0
for a,b,c in triples(100000000):
    if c % (b-a) == 0:
        count =+ 1
    


