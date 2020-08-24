import random
n = int(input("Digite o número de ramdomizações:"))
arquivo = input("Digite o nome do arquivo:")

f = open(arquivo, "w+")
for i in range(n):
    f.write(str(random.random()) + "\n")
