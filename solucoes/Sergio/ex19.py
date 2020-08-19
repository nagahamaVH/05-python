continuar = "S"
palavras = []
cont = 0
while(continuar == "S"):
	print("Programa que verifica anagramas: \n\n")
	palavras.insert(cont, input("Digite uma palavra: "))
	cont = cont+1
	continuar = input("Deseja continuar? (S/N)")

cont = 0
while (cont < len(palavras)-1):
	cont2 = cont
	while (cont2 < len(palavras)-1):
		cont2 = cont2+1
		if(sorted(palavras[cont]) == sorted(palavras[cont2])):
			print(palavras[cont] + " e " + palavras[cont2] +" São anagramas." )
	cont = cont+1
