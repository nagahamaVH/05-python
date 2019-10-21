def produto(vetor):
    p = 1
    for x in vetor:
        p *= x
    return p

print(produto([1,2,3,4,5,6,7,8,9,10]))
