limit=int(input("Digite um número limite: "))
def multiplo(limit):
	sum = 0
	for i in range(1, limit + 1):
		if ((i % 3) == 0 or (i % 5) == 0):
			sum += i
	return (f"Soma dos números divisiveis por 3 ou 5: {sum}")
print(multiplo(limit))
