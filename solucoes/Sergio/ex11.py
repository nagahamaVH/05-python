def primos(num):
	cont = 0
	while (cont <= num):
		cont2 = 2
		primo = True

		while (cont2 < cont):
			if(cont % cont2 == 0):
				primo=False
			cont2 = cont2+1

		if(primo):
			print(str(cont))
		cont = cont+1

primos(int(input("Digite um número: ")))
