#!/usr/bin/python3

import math

num1 = float(input("Digite um número:"))

if (num1 >= 0):
    raiz = math.sqrt(num1)
    print("\n",raiz)
elif (num1 < 0):
    potencia = num1 ** 2
    print("\n",potencia)
else:
    print("\nErro")
