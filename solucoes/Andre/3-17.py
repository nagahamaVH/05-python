def extsort(vetor):
    exts = []
    vetor_sorted = []
    # Faz uma lista contendo cada uma das extensões
    for x in vetor:
        ext = x.split(".")[1]
        if ext not in exts:
            exts.append(ext)
    # Organiza a nova lista a ser alterada
    for x in exts:
        for i in range(len(vetor)):
            if vetor[i].split(".")[1] == x:
                vetor_sorted.append(vetor[i])

    return vetor_sorted

print(extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
