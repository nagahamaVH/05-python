l1=int(input("Digite um valor para l1: "))
l2=int(input("Digite um valor para l2: "))
l3=int(input("Digite um valor para l3: "))

if (l1 == l2 and l1 ==  l3): 
	print ("O triângulo é equilátero")
elif (l1 == l2 and l1 != l3):
	print ("O triânguo é isósceles")
elif (l1 == l3 and l1 != l2):
	print ("O triânguo é isósceles")
elif (l2 == l3 and l2 != l1):
	print ("O triânguo é isósceles")
else:
	print ("O triângulo é escaleno")
