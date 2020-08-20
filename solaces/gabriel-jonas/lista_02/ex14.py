def product(lista):
    cummulative = lista.pop(0) 
    for i in lista:
        cummulative *= i
    return cummulative

print(product([1,2,3]))