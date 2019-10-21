import sys

a = open(sys.argv[1])
compr = int(sys.argv[2])

a_wrap = []
for x in a:
    if len(x) <= compr:
        a_wrap.append(x)
    else:
        while len(x) > compr:
            #procura o ' ' mais próximo de compr
            i_espaco = compr - 1
            while i_espaco > 0:
                if x[i_espaco] == ' ':
                    break
                i_espaco -= 1

            #caso nao encontre, quebra a palavra no indice indicado
            if i_espaco == 0:
                i_espaco = compr - 1

            a_wrap.append(x[:i_espaco])
            x = x[i_espaco + 1:]
        a_wrap.append(x)

for x in a_wrap:
    print(x)
