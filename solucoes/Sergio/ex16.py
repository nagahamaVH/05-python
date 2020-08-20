def reverse(txt=""):
	arquivo_texto = open(txt)
	linhas = arquivo_texto.readlines()
	for linha in reversed(linhas):
		print(linha)


reverse(input("Digite o nome do arquivo:"))
