f = open('users.txt','w')
id_user = 0

while True:
    name = input("Qual o nome do usuario? ")
    idade = input("Qual a idade do usuário? ")
    sexo = input("Qual o sexo do usuário? ")
    f.write("{}, {}, {}, {}\n".format(id_user, name, idade, sexo))
    op = input("Deseja cadastrar outro usuário? [s/n] ") 
    if op == 'n':
        break 
    else:
        pass
    id_user += 1

f.close()