#!/usr/bin/python3

import math    

a = float(input("Digite o valor de a\n"))
b = float(input("Digite o valor de b?\n"))
c = float(input("Digite o valor de c?\n"))

delta = (b**2)-(4*a*c)

if (delta > 0):
    x1 = (-b+(math.sqrt(delta)))/2*a
    x2 = (-b-(math.sqrt(delta)))/2*a
    print ("\nEsta equação possui duas raízes reais, sendo elas", x1, "e", x2)

elif (delta < 0):
    print ("\nEsta equação não possui raízes reais!")

elif (delta == 0):
    x1 = (-b+(math.sqrt(delta)))/2*a
    x2 = (-b-(math.sqrt(delta)))/2*a
    print ("\nEsta equação só possui uma raiz, sendo ela", x1)
else:
    print ("\nVariável incorreta")
