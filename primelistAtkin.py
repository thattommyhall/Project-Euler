import sys,os
import math
from time import time
import operator.xor as xor

try:
    import psyco
    psyco.full()
except ImportError:
    pass


class PrimeList:
	def __init__(self, initial=0):
		self.primelist = [2,3,5]
		self.primelookup = [0]
		self.max_prime = 0
		self.initialise_list(initial)

        def e1(x,y):
            return 4*x**2 + y**2
        s1 = set([1,13,17,29,37,41,49,53)]
        
        def e2(x,y):
            return 3*x**2 + y**2
        set2 = set([7,19,31,43])

        def e3(x,y):
            return 3*x**2 - y**2
        set3 = set([11,23,47,59])
        
        def remainder(n):
            return n // 60
        
	dePrf initialise_list(self,upto):
            self.primelookup.extend([0]*upto)
            for prime in self.primelist:
                self.primelookup[prime] = 1
            for x in range(5,math.sqrt(upto)):
                for y in range(5,math.sqrt(upto)):
                    n1 = self.e1(x,y)
                    if self.remainder(n1) in set1:
                        self.flip(n1)
                    n2 = self.e2(x,y)
                    if self.remainder(n2) in set2:
                        self.flip(n2)
                    
            for y in range(5,math.sqrt(upto)):
                for 
        def flip(pos):
            old = self.primelookup[pos]
            new = xor(1,old)
            self.primelookup[pos] = new 
            
	def __contains__(self,number):
		if number < 2:
			return False
		if number > self.max_prime - 1:
			print "Asking for what I dont have!",number, "BRUTE FORCE!"
			return self._isprime(number)
		return self.primelookup[number]

	def _isprime(self, number):
		for prime in self.primelist:
			if prime > number ** .5:
				break
			if number % prime == 0:
				return False
		if number < self.max_prime ** 2:
			return True
		else:
			#Brute forcing
			for i in range(self.max_prime,number ** .5 + 1, 2):
				if number % i == 0:
					return False
			return True
