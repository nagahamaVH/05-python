def enumerate(vetor): return [tuple([i,vetor[i]]) for i in range(len(vetor))]

for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
