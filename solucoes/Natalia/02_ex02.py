idade = int(input ("Por favor, digite sua idade: "))
peso = int(input ("Por favor, digite seu peso (em kg): "))
sono = int(input ("Digite quanto tempo (em horas) você dormiu nas últimas 24hrs: "))
if ((idade <= 69 and idade >= 16) and (peso >= 50) and (sono >= 6)):
    print ("Você pode doar sangue :) ")
else : 
    print ("Você não pode doar sangue :( ")
