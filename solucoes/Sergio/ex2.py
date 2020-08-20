idade = int(input("Digite a sua idade: "))
if(idade >= 16 and idade <= 69):
	peso = int(input("Digite o seu peso (em kg): "))

	if(peso >= 50):
		horas_sono = int(input("digite quantas horas dormiu na última noite: "))

		if(horas_sono >= 6):
			print("Tudo certo para sua doação de sangue, obrigado!")
		else:
			print("Horas de sono não compatível")
	else:
		print("Peso não compatível")
else:
	print("Idade não compatível")
