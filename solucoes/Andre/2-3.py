print("Considere uma equação de segundo grau f(x) = a*x**2 + b*x + c")
a = int(input("Insira o número 'a':"))
b = int(input("Insira o número 'b':"))
c = int(input("Insira o número 'c':"))

delta = b**2 - (4*a*c)

if delta > 0:
    print("A equação possui duas raízes reais")
elif delta == 0:
    print("A equação possui uma raíz real")
else:
    print("A equação não possui nenhuma raíz real")


