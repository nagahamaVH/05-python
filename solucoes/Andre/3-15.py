def unico(vetor,key = lambda l : l):
    u = []
    for x in vetor:
        contador = 0
        for i in range(len(u)):
            if key(vetor[i]) == key(x):
                contador += 1
        if contador == 0:
            u.append(x)
    return u

print(unico(["python", "java", "Python", "Java"], key=lambda s: s.lower()))


