from __future__ import division
from Euler import *

pents = set([])

def abs(x):
    return max([x,-x])

for i in range(1,10000):
    pents.add(i * (3*i - 1) / 2)
#print pents

@timed
def solve():
    for i in pents:
        for j in pents:
            if (i+j in pents and abs(j-i) in pents):
                print i,j, abs(j-i)

solve()
