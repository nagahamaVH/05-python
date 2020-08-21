import sys


def median(numbers):
    n = len(numbers)
    sorted_arr = sorted(numbers)
    if (n%2 ==0): # PAR
        mid = n/2
        
        med = (sorted_arr[int(mid)-1] + sorted_arr[int(mid)]) / 2
    else:
        mid = (n+1)/2
        med = sorted_arr[int(mid)-1]
    
    return med



d = int(sys.argv[1])
f = open('input_9.txt', 'r')
gastos = []

count = 0
for line in f:
    if (count < d): # grace period
        gastos.append(int(line))
        count += 1
    else:
        gasto_atual = int(line)
        mediana = median(gastos)
        if gasto_atual >= 2*mediana:
            print ("Alerta de possivel fraude: Dia {}".format(count+1))
        gastos.pop(0)
        gastos.append(gasto_atual)
        count += 1

