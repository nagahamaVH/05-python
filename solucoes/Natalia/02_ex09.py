limit=int(input("Digite um número limite: "))
def showNumbers(limit):
	for i in range(limit + 1):
		if ((i % 2) == 0):
			print (i, "PAR")
		else:
			print (i, "IMPAR")
showNumbers(limit)
