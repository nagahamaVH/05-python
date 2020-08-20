def showNumbers(limit):
    for i in range(limit+1):
        print ("*\t {} {}".format(i, "IMPAR" if i%2 else "PAR"))


showNumbers(6)