#!/usr/bin/python3

def speed(x):
    if (x < 70):
        print("\nOk")
    elif (x > 70):
        y = (x-70)/5
        if (y > 12):
            print ("Licen suspended")
        else:
            print ("Pontos:", y)
    else:
        print ("Erro!")
y = speed(1000)        
