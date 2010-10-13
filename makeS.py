def makeS():
    f = open('S.txt','w')
    S = ''
    for i in range(100000000):
        S += str(i)
    f.write(S)
    f.close()

makeS()
