from Euler import *

def double_append(somestr, somechr):
    return somechr + somestr + somechr
        
digits = map(str,range(1,10))

def gendecimalpalendromes(length):
    if length == 2:
        for i in range(0,10):
            yield 2*str(i)
    if length == 1:
        for i in range(10):
           yield str(i)
    if length not in [1,2]:
        for palendrome in gendecimalpalendromes(length-2):
            for digit in digits:
                yield double_append(palendrome,digit)

def genpalendromes(maxlength):
    for i in range(1,maxlength):
        for palendrome in gendecimalpalendromes(i):
            yield palendrome
    
        


def dec2bin(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

def ispalendrome(somestr):
    return all([somestr[i] == somestr[-(i+1)] for i in range(int(len(somestr))/2)])


print dec2bin(585)
print ispalendrome('585')
print ispalendrome(dec2bin(585))

palendromes = set([])

def solve():

    for i in genpalendromes(7):
        if ispalendrome(dec2bin(int(i))):
            print i, dec2bin(int(i))
            palendromes.add( i)
            

    print sum(int(i) for i in palendromes)
    
solve()
