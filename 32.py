from Euler import *

import psyco
psyco.full()

def run():
    solns = set([])
    for perm in perms("123456789"):
        #print perm
        for i in range(1,7):
            for j in range(i+1,8):
                calc = perm[:i] + "*" + perm[i:j] + "==" + perm[j:]
                #print calc
                if eval(calc):
                    print calc
                    solns.add(perm[j:])
    print sum(int(sol) for sol in solns)
    
run()
