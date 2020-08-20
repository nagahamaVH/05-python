print ("Considere a função f(x) = ax^2 + bx + c, entre com os coeficientes: ")
a = int (input("a: "))
b = int (input("b: "))
c = int (input("c: "))

delta = (b*b) - 4*a*c

if delta < 0:
    print ("Não há raizes reais.")
elif delta == 0:
    print ("As duas raízes são iguais")
else:
    print ("Possui duas raízes reais distintas.")