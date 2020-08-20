def multiplos(num):
	cont = 0
	soma = 0
	while(cont <= num):
		if(cont % 3 == 0 or cont % 5 == 0):
			soma = soma+cont
		cont = cont+1
	print(str(soma))

multiplos(int(input("Digite um número: ")))
