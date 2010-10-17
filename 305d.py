def partitions(somestring):
    for i in range(len(somestring)+1):
        yield somestring[:i], somestring[i:]

for i in partitions('test'):
    print i

def gennumbers(somepartition):
    first,second = somepartition
    
