def imprimeMenosD(nomes):
    for n in nomes:
        if not n[0].lower() == "d":
            #n[0] = z
            print(n)


lista = ["André", "daniel", "Cristiano", "wana", "Duan", "harrison", "Alessandra",
 "bruna", "Alexandre", "lázaro", "Vitor", "leonardo", "Sávio", "lucas", "Rafael",
 "jéssica", "Letícia", "gabriel", "Gabriela", "felipe", "Muriel"] 

imprimeMenosD(lista)
