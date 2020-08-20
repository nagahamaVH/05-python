#Quantas multiplicações são executadas quando cada uma das linhas de código são executadas?
numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print(square(5))   #multiplica 1 vez 5*5
print(square(2*5)) #multiplica 1 vez 10*10
#A variavel numcalls não é usada
