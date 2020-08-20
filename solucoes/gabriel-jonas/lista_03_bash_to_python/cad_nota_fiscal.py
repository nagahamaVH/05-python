f = open('nota_fiscal.txt','w')


while True:
    id_compra = input("Qual o id da compra? ")
    id_usuario = input("Qual o id do usuario? ")
    data = input("Qual a data? ")
    f.write("{}, {}, {}\n".format(id_compra, id_usuario, data))
    op = input("Deseja cadastrar outra nota fiscal? [s/n] ") 
    if op == 'n':
        break 
    else:
        pass

f.close()