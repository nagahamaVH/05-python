def reverter(vetor):
    r = []
    for i in range(len(vetor)):
        r.insert(0, vetor[i])
    return r

print(reverter([1,2,3,4]))
print(reverter(["Arroz","Feijão","Bife","Batata Frita"]))
