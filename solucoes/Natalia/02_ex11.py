limit=int(input("Digite um número limite: "))
def numerosPrimos(limit):
	for num in range(1, limit + 1):
   		if num > 1:
       			for i in range(2,num):
           			if (num % i) == 0:
               				break
       			else:
           			print(num)
print (f"Números primos até {limit}: ")
numerosPrimos(limit)
