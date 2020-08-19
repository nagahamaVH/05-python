x = [0, 1, [2]]
x[2][0] = 3     #Muda o elemento de posição [0] dentro da lista na posição [2] para 3.
print (x)         #x=[0, 1, [3]]
x[2].append(4)  #Coloca o 4 dentro da lista na posição [2]. Só dá certo pq na posição [2] tem uma lista.
print (x)         #x=[0, 1, [3, 4]]
x[2] = 2        #Muda a lista da posição [2] para 2.
print (x)         #x=[0, 1, 2]
