from collections import defaultdict

from time import time
import math
#import psyco
#psyco.full()

def run():
	start = time()
	counter = [0] * 1000
	maxperimeter = 1000
		#print perimeter
	for a in range(1,maxperimeter/2):
		for b in range(1, maxperimeter/2 - a):
			c = math.sqrt(b**2 + a**2)
			if int(c) == c and a+b+c < maxperimeter:
				counter[a+b+int(c)] += 1
	mosttriples = 0		
	for pos,count in enumerate(counter):
		if count > mosttriples:
			mosttriples = count
			print pos,count
	end = time()
	print "TOOK", end-start

print "without psyco"
run()

print "with"
import psyco
psyco.full()
run()
