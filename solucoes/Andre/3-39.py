def invertedicio(d):
    d_i = {}
    for c, v in d.items():
        d_i[v] = c
    
    return d_i

print(invertedicio({'x': 1, 'y': 2, 'z': 3}))