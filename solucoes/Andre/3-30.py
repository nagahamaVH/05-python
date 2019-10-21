def vetor(x,y): return [[None for _ in range(y)] for _ in range(x)]

a = vetor(2,3)
print(a)
a[0][0] = 5
print(a)
