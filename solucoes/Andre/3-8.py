def soma_cumulativa(vetor):
    soma = 0
    soma_c = []
    for x in vetor:
        soma += x
        soma_c.append(soma)
    return soma_c

print(soma_cumulativa([1,2,3,4]))
print(soma_cumulativa([4,3,2,1]))
