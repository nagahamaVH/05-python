#!/usr/bin/python3

idade=int(input("Qual a sua idade?"))
peso=int(input("Qual o seu peso?"))
dormiu=int(input("Quantas horas você dormiu nas últimas 24 horas?"))

if (16 < idade < 69):
    if (peso > 50):
        if (dormiu >= 6):
            print ("\nParabéns, você está apto para doar sangue!")
        else:
            print ("\nVocê não está apto para doar sangue!")
    else:
        print ("\nVocê não está apto para doar sangue!")
else:
    print ("\nVocê não está apto para doar sangue!")
