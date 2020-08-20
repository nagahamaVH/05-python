l1 = int(input("Digite um número: "))
l2 = int(input("Digite um número: "))
l3 = int(input("Digite um número: "))

if (l1 == l2) and (l2 == l3):
    print ("Equilatero")
elif (l1 == l2) or (l2 == l3) or (l1 == l3):
    print ("Isóceles")
else:
    print ("Escaleno")