calendario = {
    1 : "Janeiro",
    2 : "Fevereiro",
    3 : "Março",
    4 : "Abril",
    5 : "Maio",
    6 : "Junho",
    7 : "Julho",
    8 : "Agosto",
    9 : "Setembro",
    10 : "Outubro",
    11 : "Novembro",
    12 : "Dezembro"
}

mes = int(input("Insira um número inteiro de 1 a 12: "))

if mes in calendario:
	print("Mês correspondente: ", calendario[mes])
else:
    	print("Erro! Não existe mês com este número")
