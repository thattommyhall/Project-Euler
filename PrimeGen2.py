from itertools import count
from heapq import heappush,heappop

def gen_primes():
    yield 2
    
    def update_composites(number,increment):
        heappush(composites,(number,increment))

    composites = [(4,2)]

    c = count(3)
    
    while 1:
        print composites
        next = c.next()
        smallest,inc = heappop(composites)
        while 1:
            try:
                nextsmallest,newinc = composites[0]
            except IndexError:
                break
            if nextsmallest != smallest:
                break
            update_composites(nextsmallest+newinc,newinc)
            smallest,inc = heappop(composites)
            
        if next < smallest:
            yield next
            c.next()
            update_composites(2*next,next)

                        
g=gen_primes()
    
for i in range(100):
    print g.next()
    raw_input()
