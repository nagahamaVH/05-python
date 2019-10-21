def agrupar(vetor, t):
    vetor_a = []
    sub_vetor = []
    for x in vetor:
        sub_vetor.append(x)
        if len(sub_vetor) == t:
            vetor_a.append(sub_vetor)
            sub_vetor = []
    if len(sub_vetor) > 0:
        vetor_a.append(sub_vetor)
    return vetor_a

print(agrupar([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(agrupar([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
