def soma(vetor):
    s = 0
    if isinstance(vetor[0],str):
        s = ""
    for x in vetor:
        s += x
    return s

print(soma([1,2,3,4,5,6,7,8,9,10]))
print(soma(["Batata", "Assada"]))

