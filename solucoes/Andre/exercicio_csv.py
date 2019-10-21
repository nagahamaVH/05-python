def parse_csv(caminho_arq):
    a = open(caminho_arq).readlines()
    matriz = []
    for l in a:
        l_split = l.split(',')
        for i in range(len(l_split)):
            if l_split[i][-1] == '\n':
                l_split[i] = l_split[i][:-1]
        matriz.append(l_split)

    for l in matriz:
        print(l)
    return matriz


print(parse_csv('a1.csv'))
print(parse_csv('iris.csv'))