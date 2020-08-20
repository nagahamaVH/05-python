print("-Programa para inverter valores e chaves no dicionário-")
continuar = "S"
dicionario = {}

def invertdict(dicionario = {}):
	dicionario_reverso = {value : key for (key, value) in dicionario.items()}
	print("\n Dicionario: " + str(dicionario))
	print(" Dicionario reverso: " + str(dicionario_reverso))

while(continuar == "S"):
	chave = input("Digite a chave do dicionário: ")
	valor = input("Digite o valor para a chave: ")
	dicionario[chave] = valor
	continuar = input("Deseja continuar? (S p/ Sim e N p/ Não) ")

invertdict(dicionario)
