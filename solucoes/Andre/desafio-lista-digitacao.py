tamanho = int(input("Insira o tamanho da lista: "))
lista = []

for i in range(tamanho):
    lista.append(i * 2000)
lista.reverse()
print(lista)
