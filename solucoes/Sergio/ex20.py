print("-Programa para ordenar dicionários por chave-")
continuar = "S"
dicionario = {}

def valuesort(dicionario = {}):
        for i in sorted (dicionario.keys()):
                print(str(dicionario[i]))

while(continuar == "S"):
	chave = input("Digite a chave do dicionário: ")
	valor = input("Digite o valor para a chave: ")
	dicionario[chave] = valor
	continuar = input("Deseja continuar? (S p/ Sim e N p/ Não) ")

valuesort(dicionario)
