def wrap(txt="",pos=0):
	arquivo_texto = open(txt)
	linhas = arquivo_texto.readlines()
	for linha in linhas:
		print(linha[:pos])
		print(linha[pos:])


txt = input("Digite o nome do arquivo:")
pos = int(input("Digite a posição de corte para a linha:"))
wrap(txt,pos)
