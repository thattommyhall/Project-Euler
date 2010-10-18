from itertools import count
from heapq import heappush,heappop

def gen_primes():
    yield 2
    
    def update_composites(number,increment):
        heappush(composites,(number,increment))
    composites = [(4,2)]

    c = count(3)
    
    while 1:
        #print composites
        smallest,increment = heappop(composites)
        update_composites(smallest+increment,increment)
        if composites[0][0] == smallest:
            continue
        next = c.next()
        if next < smallest:
            yield next
            c.next()
            update_composites(2*next,next)
        
            

                        
g=gen_primes()
    
for i in range(100):
    print g.next()
