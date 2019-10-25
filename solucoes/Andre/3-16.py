def unico(vetor):
    u = set()
    for x in vetor:
        contador = 0
        for i in range(len(u)):
            if vetor[i] == x:
                contador += 1
        if contador == 0:
            u.add(x)
    return u

print(unico([1, 2, 1, 3, 2, 5]))

