#!/usr/bin/python3

num1=int(input("Digite o primeiro número:"))
num2=int(input("Digite o segundo número:"))

soma = num1+num2

if (soma > 20):
    soma = soma + 8
    print ("\n",soma)
elif (soma < 20):
    soma = soma - 5
    print ("\n",soma)
else:
    print("\nErro!")
