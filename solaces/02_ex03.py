a, b, c = input("Digite as parâmetros a, b e c da equação de segundo grau f(x) = a*x^2 + b*x + c: ").split()
a=int(a)
b=int(b)
c=int(c)
delta = (b**2) - (4*a*c)
if (a == 0):
    print ("Essa equação é de primeiro grau. Escolha um valor de a diferente de 0.")
elif (delta < 0):
    print ("A equação não possui raízes reais.")
elif (delta == 0):
    print ("A equação possui uma raíz real.")
else:
    print ("A equação possui duas raízes reais.")
