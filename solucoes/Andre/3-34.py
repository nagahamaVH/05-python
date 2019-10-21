def quase_igual(p, q):
    return p in mutar(q)

def mutar(p):
    # inserir
    m = [p[:i] + chr(c) + p[i:] for c in range(ord('a'),ord('z')+1) for i in range(len(p)+1)]
    # deletar
    m += [p[:i] + p[i+1:] for i in range(len(p))]
    # substituir
    m += [p[:i] + chr(c) + p[i+1:] for c in range(ord('a'),ord('z')+1) for i in range(len(p))]
    # trocar
    m += [p[:i] + p[i+1] + p[i] + p[i+2:] for i in range(len(p)-1)]

    return m

print(quase_igual('python', 'perl'))
print(quase_igual('perl', 'pearl'))
print(quase_igual('python', 'jython'))
print(quase_igual('man', 'woman'))