def divisors(number):
    return [i for i in range(1,number) if (number % i == 0)]


def d(number):
    return sum(divisors(number))

print d(220)

def is_amicable(a):
    b = d(a)
    return (a != b and d(b) ==a)

print sum(i for i in range(1,10001) if is_amicable(i))

