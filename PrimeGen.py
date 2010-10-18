from itertools import count

def gen_primes():
    yield 2
    def update_composites(number,increment):
        try:
            composites[number] += [increment]
        except:
            composites[number] = [increment]

    composites = {4:[2]}

    c = count(3)
    while 1:
        #print composites
        next = c.next()
        smallest = min(composites.keys())
        incs = composites[smallest]
        del composites[smallest]
        for inc in incs:
            update_composites(smallest+inc,inc)
        if next < smallest:
            yield next
            c.next()
            update_composites(next**2,next)
                        
g=gen_primes()
    
for i in range(100):
    print g.next()
