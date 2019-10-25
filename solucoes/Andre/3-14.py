def lensort(vetor):
    max_len = 0
    vetor_s = []

    for x in vetor:
        if len(x) > max_len:
            max_len = len(x)

    for i in range(max_len + 1):
        for j in range(len(vetor)):
            if len(vetor[j]) == i:
                vetor_s.append(vetor[j])

    return vetor_s

print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))
