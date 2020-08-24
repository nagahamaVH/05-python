month=int(input("Digite um número de 1 a 12: "))
#l1 = [1 2 3 4 5 6 7 8 9 10 11 12]
l2 = ['J', 'F', 'M', 'A', 'M', 'J', 'J', 'A', 'S', 'O', 'N', 'D']
if (month >=1 and month <=12):
	print (l2[month-1])
else:
	print (" Não existe mês com esse número.")
