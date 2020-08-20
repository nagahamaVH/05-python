mes_por_extenso = ("","Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
mes_numero = int(input("Digite o número do mês: "))

if(mes_numero >= 1 and mes_numero <=12):
	print(mes_por_extenso[mes_numero])
else:
	print("Não existe mês com este número")
