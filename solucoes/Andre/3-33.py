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

palavras = mutar('hello')
print(palavras)
print('helo' in palavras)
print('cello' in palavras)
print('helol' in palavras)
print('batata' in palavras)