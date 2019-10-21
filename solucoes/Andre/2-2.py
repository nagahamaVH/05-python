doar = True
print("*** | Programa Místico de Doação de Sangue | ***")
idade = int(input("Digite a sua idade: "))
peso = int(input("Digite o seu peso: "))
sono = int(input("Digite a quantidade de horas dormidas nas últimas 24 horas: "))

if idade < 16 or idade > 69: doar = False
if peso < 50: doar = False
if sono < 6: doar = False

print(">>> RESULTADO <<<")
if doar:
    print("Bora arregaçar as manguinhas e arrancar esse sangue, você está LIBERADO para doar")
else:
    print("Sai pra lá, você NÃO ESTÁ LIBERADO para doar sangue! Se duvidar, talvez você até mesmo necessita receber uma transfusão, heim.")
