from Euler import *
from primelist import PrimeList

max_prime = 1000000

primes = PrimeList(max_prime)
squares = [i**2 for i in range(int(math.sqrt(max_prime)))]

@timed
def main():
    i = 3
    while i < max_prime:
        if i in primes:
            i += 2
            continue
        if all([(i-prime)/2 not in squares for prime in primes.primelist if prime < i]):
                print "found ",i
                break
        i += 2
main()
