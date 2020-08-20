def soma(lista):
    cummulative = lista.pop(0) 
    for i in lista:
        cummulative += i
    return cummulative

print(soma(["hello","world"]))