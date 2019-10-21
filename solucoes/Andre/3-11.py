def duplicado(vetor):
    d = []
    for x in vetor:
        contador = 0
        for i in range(len(vetor)):
            if vetor[i] == x:
                contador += 1
        if contador > 1 and x not in d:
            d.append(x)
    return d

print(duplicado([1, 2, 1, 3, 2, 5]))

