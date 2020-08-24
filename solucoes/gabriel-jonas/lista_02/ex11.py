def showPrime(limit):
    for i in range(2,limit+1):
        multiplos = 0
        for j in range(2,i):
            if i%j ==0:
                multiplos += 1
        if multiplos == 0:
            print ("{} é primo".format(i))


showPrime(20)
