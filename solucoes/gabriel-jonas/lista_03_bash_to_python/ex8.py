import math

def mean(numbers):
    n = len(numbers)
    return sum(numbers)/n

def std(numbers):
    n = len(numbers)
    media = mean(numbers)
    var = sum((x-media)**2 for x in numbers)
    std = var/n
    std = std**0.5
    return std

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

numbers = []
file = open('input_8.txt', 'r')

for line in file:
    numbers.append(int(line))


print (numbers)
print ("Media {}".format(mean(numbers)))
print ("Desvio Padrão {}".format(std(numbers)))
print ("Mediana {}".format(median(numbers)))