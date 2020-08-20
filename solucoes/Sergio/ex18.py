txt = input("Digite o nome do arquivo: ")
arquivo_texto = open(txt)
linhas = arquivo_texto.readlines()
frequencia = {}
for linha in linhas:
	for i in linha:
		i = i.lower()
		linha = linha.lower()

		if i in frequencia:
			frequencia[i] += 1
		else:
			frequencia[i] = 1


for chave, valor in frequencia.items():
    print(chave, ' : ', valor)
