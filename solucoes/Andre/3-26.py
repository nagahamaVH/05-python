def quadrado(x): return x * x

def mapa(func, lista):
    return [func(x) for x in lista]

print(mapa(quadrado, range(5)))
