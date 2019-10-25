def valuesort(d):
    l_chaves = list(d.keys())
    l_chaves.sort()
    return [d[c] for c in l_chaves]

print(valuesort({'x': 1, 'y': 2, 'a': 3}))