def showNumbers(limit):
    for i in range(limit + 1):
        j = ""
        if i % 2 == 0:
            j = "EVEN"
        else:
            j = "ODD"
        print(i,j)

showNumbers(99)