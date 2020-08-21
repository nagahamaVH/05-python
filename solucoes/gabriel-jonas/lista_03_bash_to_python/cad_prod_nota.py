f = open('prod_nota_fiscal.txt','w')


while True:
    id_compra = input("Qual o id da compra? ")
    id_usuario = input("Qual o id do produto? ")
    quantidade = input("Qual a quantidade? ")
    f.write("{}, {}, {}\n".format(id_compra, id_usuario, quantidade))
    op = input("Deseja cadastrar outra nota fiscal? [s/n] ") 
    if op == 'n':
        break 
    else:
        pass

f.close()