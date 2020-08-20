idade = int(input("Qual sua idade: "))
peso = int(input ("Qual seu peso?: "))
sono = int(input ("Quantas horas você dormiu nas últimas 24hrs? "))

if idade >= 16 and idade <= 69 and peso >= 50 and sono >=6:
    print ("Você pode doar sangue.")
else:
    print ("Você nao pode doar sangue")