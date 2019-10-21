def triplets(n):
    return [tuple([j,i,j+i]) for i in range(1,n) for j in range(1,n) if (i + j) < n and i >= j]

print(triplets(5))