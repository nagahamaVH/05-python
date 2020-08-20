def checkSpeed(speed):
    if (speed <= 70):
        print ("Ok")
    else:
        excess = speed-70
        points = int(excess / 5)
        if (points >= 12):
            print ("Licen suspended")
        else:
            print ("Pontos: {}".format(points))

velocidade = int(input("Digite a velocidade: "))

checkSpeed(velocidade)