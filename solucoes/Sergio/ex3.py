print("Cálculo de funções de segundo grau (f(x):ax²+bx+c):")
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b*b)-4*a*c
if (delta < 0):
	print("Nenhuma raíz real.")
elif (delta == 0):
	print("Uma única raíz real.")
else: 
	print("Duas raízes reais")

x1 = (-b+(delta**(1/2)))/(2*a)
x2 = (-b-(delta**(1/2)))/(2*a)

print(x1, x2)

