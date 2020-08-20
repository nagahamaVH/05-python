def showNumbers(limit):
	cont = 1
	while(cont <= limit):
		if(cont % 2):
			print(str(cont)+ " - IMPAR")
		else:
			print(str(cont)+ " - PAR")
		cont = cont+1


showNumbers(int(input("Digite um número: ")))
