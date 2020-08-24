arquivo = open(input("Digite o nome do arquivo: "), 'r')
linhas = arquivo.readlines()

count = 0
soma = 0
for linha in linhas:
    count = count+1
    soma += float(linha)

print("A média é: "+ str(soma/count))
linhas_sorted = sorted(linhas)
print("A mediana é: "+ str(linhas_sorted[int(len(linhas)/2)]) )

dividendo = 0
for linha in linhas:
    dividendo += float(linha)-(soma/count)
desvio_padrao = ((dividendo**2)/count)**(1/2)
print("O desvio padrão é: " + str(desvio_padrao))
