def parse_csv(caminho_arq,d,c):
    a = open(caminho_arq).readlines()
    return [[y for y in x if (y != "\n" and y != "," and y != d)] for x in a if x[0] != c]

print(parse_csv('a2.csv','!','#'))

