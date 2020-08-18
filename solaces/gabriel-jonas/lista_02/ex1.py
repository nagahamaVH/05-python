number1 = input("Digite o primeiro número:")
number1 = int (number1)
number2 = input("Digite o segundo número:")
number2 = int(number2)

print ("O menor número é o {}".format(number2 if number1 > number2 else number1))