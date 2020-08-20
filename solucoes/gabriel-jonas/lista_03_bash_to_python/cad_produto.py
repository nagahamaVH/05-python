f = open('produtos.txt','w')
id_produto = 0

while True:
    valor = input("Qual o valor do produto? ")
    tamanho = input("Qual o tamanho do produto ")
    f.write("{}, {}, {}\n".format(id_produto,  valor, tamanho))
    op = input("Deseja cadastrar outro produto? [s/n] ") 
    if op == 'n':
        break 
    else:
        pass
    id_produto += 1

f.close()