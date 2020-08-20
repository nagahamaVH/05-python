d = int(input("Digite um número de dias:"))
arquivo = open(input("Digite o nome do arquivo: "), 'r')
linhas = arquivo.readlines()
gastos = []
cont = 0
while (cont < len(linhas)-d):
    for linha in linhas[cont:cont+d]:
        gastos.append(float(linha))

    gasto_dia = float(linhas[cont+d])
    gasto_medio = float(linhas[int((cont+d)/2)])
    if (gasto_dia > (2*gasto_medio)):
        print("Alerta")
    cont += 1
    gastos[:] = []
