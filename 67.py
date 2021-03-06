from helper import memoized
import time

tri = open('triangle.txt','r').read()
tri = [map(int,line.split()) for line in tri.splitlines()]

@memoized
def value(row,pos):
    if row == len(tri)-1:
        return tri[row][pos]
    else:
        return tri[row][pos] + max(value(row+1,pos),value(row+1,pos+1))

start = time.time()
print value(0,0)
end = time.time()

print "took ", end-start
