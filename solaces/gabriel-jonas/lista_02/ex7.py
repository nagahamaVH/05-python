meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dec"]

mes = int(input("Digite o mês: "))

if mes <= 12:
    print (meses[mes-1])
else:
    print ("Não existe mes com esse número.")