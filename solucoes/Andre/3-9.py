def prod_cumulativo(vetor):
    prod = 1
    prod_c = []
    for x in vetor:
        prod *= x
        prod_c.append(prod)
    return prod_c

print(prod_cumulativo([1,2,3,4]))
print(prod_cumulativo([4,3,2,1]))

