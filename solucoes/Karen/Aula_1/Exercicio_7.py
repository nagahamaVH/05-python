#!/usr/bin/python3

numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
   # print (numcalls)
    return x * x

print(square(5))
print(square(2*5))

