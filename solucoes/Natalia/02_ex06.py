speed=int(input("Digite a velocidade (em km/h): "))

def testevelocidade(speed):
	if (speed < 70) :
		return ("Ok.")
	else:
		points = (speed-70)//5
		if (points <= 12) :
			return (f"Pontos retirados: {points}")
		else:
			return ("Licensa suspensa.")
print (testevelocidade(speed))
