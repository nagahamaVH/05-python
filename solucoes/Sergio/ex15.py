def fatorial(num):
	cont = 1
	soma = 1
	while(cont <= num):
		soma = soma*cont
		cont = cont+1
	print(str(soma))

num = int(input("Digite um número: "))
fatorial(num)
