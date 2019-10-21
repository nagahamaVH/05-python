def parse_csv(caminho_arq):
    a = open(caminho_arq).readlines()
    return [[y for y in x if (y != "\n" and y != ",")] for x in a]

print(parse_csv('a1.csv'))
print(parse_csv('iris.csv'))