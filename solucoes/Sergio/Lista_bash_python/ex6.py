lado_1 = input("Digite um lado do triangulo:")
lado_2 = input("Digite outro lado do triangulo:")
lado_3 = input("Digite o ultimo lado do triangulo:")

if(lado_1 == lado_2 == lado_3):
    print("Equilátero")
elif(lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3):
    print("Isósceles")
else:
    print("Escaleno")
