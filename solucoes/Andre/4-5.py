def soma_estranha(limite):
    s = 0
    for x in range(limite + 1):
        if x % 3 == 0 or x % 5 == 0:
            print(x)
            s += x
    
    return s

print(soma_estranha(20))