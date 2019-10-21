def e_anagrama(a,b):
    return sorted(a) == sorted(b)

def anagramas(lista):
    lista_ana = [[y for y in lista if e_anagrama(x,y) ] for x in lista]
    lista_aux = []
    for a in lista_ana:
        a.sort()
        if a not in lista_aux: 
            lista_aux.append(a)
    return lista_aux

print(anagramas(['eat', 'ate', 'done', 'tea', 'soup', 'node']))