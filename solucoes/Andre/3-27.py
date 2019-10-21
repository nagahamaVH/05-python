def par(x): return x %2 == 0

def filtro(f,l): return [x for x in l if f(x)]

print(filtro(par, range(10)))
