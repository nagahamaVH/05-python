import math

def checa_mot(vel):
    demerito = 0
    if vel < 70:
        print("Ok")
    else:
        aux = (vel - 70) / 5
        multiplier = 10 ** 0
        aux = int(math.floor(aux * multiplier) / multiplier)
        demerito += aux

        if demerito > 12:
            print("Habilitação suspensa")

checa_mot(80)
checa_mot(20)
checa_mot(84)
checa_mot(160)