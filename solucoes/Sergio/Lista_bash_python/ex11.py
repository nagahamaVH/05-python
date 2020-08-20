def cadastro_usuario():
    print("Cadastro de Clientes:\n")
    id_usuario = input("Digite o id do usuário (2 digitos), seguido de [ENTER]:")
    nome_usuario = input("Digite o nome do usuário, seguido de [ENTER]:")
    idade_usuario = input("Digite a idade do usuário (2 digitos), seguido de [ENTER]:")
    sexo_usuario = input("Digite o sexo do usuário (Masculino, Feminino ou Outros), seguido de [ENTER]:")
    f= open("cadastro_usuario.txt","w+")
    f.write(id_usuario+","+nome_usuario+","+idade_usuario+","+sexo_usuario+"\n")

def cadastro_produto():
    print("Cadastro de Produtos:\n")
    id_produto = input("Digite o id do Produto (2 digitos), seguido de [ENTER]:")
    valor_produto = input("Digite o valor do Produto (4 digitos), seguido de [ENTER]:")
    tamanho_produto = input("Digite o tamanho do Produto (2 digitos), seguido de [ENTER]:")
    f= open("cadastro_produto.txt","w+")
    f.write(id_produto+","+valor_produto+","+tamanho_produto+"\n")

def cadastro_venda():
    print("Cadastro de Vendas: \n")
    id_compra = input("Digite o id para a compra (2 digitos), seguido de [ENTER]:")
    id_usuario_compra = input("Digite o id do usuário que realizou a compra (2 digitos), seguido de [ENTER]:")
    data_compra = input("Digite a data para a compra (8 digitos, sem espaços e pontuações), seguido de [ENTER]:")
    f= open("cadastro_venda.txt","w+")
    f.write(id_compra+","+id_usuario_compra+","+data_compra+"\n")
    cadastro_produto_venda()

def cadastro_produto_venda():
    print( "Produtos Venda: \n")
    f= open("cadastro_produto_vendas.txt","w+")
    cadastrar_novo_produto = "S"
    while(cadastrar_novo_produto == "S"):
        id_venda_compra = input("Digite o id para a compra (2 digitos), seguido de [ENTER]:")
        id_produto_compra = input("Digite o id para o produto (2 digitos), seguido de [ENTER]:")
        quantidade_compra = input("Digite a quantidade de produtos, seguido de [ENTER}:")

        f.write(id_compra+","+id_usuario_compra+","+data_compra+"\n")
        cadastrar_novo_produto = input("Deseja cadastrar outro produto? (S p/ Sim e N p/ Não)")

def media_quantidade_usuario():
    print("Em manutenção")
def media_valor_usuario():
    print("Em manutenção")
def media_valor_categoria():
    print("Em manutenção")
def media_valor_horario():
    print("Em manutenção")

def calculos_e_filtros():
    print("-Cálculos e Filtros- \n\n")
    print("1- Média de quantidade de produtos por usuário")
    print("2- Média de valor gasto por usuário")
    print("3- Média de valor por categoria de usuário")
    print("4- Valor média de compra por horário")
    opcao = input()
    if(opcao == "1"):
        media_quantidade_usuario()
    elif(opcao == "2"):
        media_valor_usuario()
    elif(opcao == "3"):
        media_valor_categoria()
    elif(opcao == "4"):
        media_valor_horario()
    else:
        print("opção inválida")

continuar = "S"
while(continuar == "S"):
    print("-Software de Gestão- \n\n")
    print("1- Cadastro de usuário")
    print("2- Cadastro de produtos")
    print("3- Cadastro de vendas")
    print("4- Cálculos")
    opcao = input()
    if(opcao == "1"):
        cadastro_usuario()
    elif(opcao == "2"):
        cadastro_produto()
    elif(opcao == "3"):
        cadastro_venda()
    elif(opcao == "4"):
        calculos_e_filtros()
    else:
        print("opção inválida")

    continuar = input(" \n\n Deseja continuar? (S p/ sim e N p/ Não)")
