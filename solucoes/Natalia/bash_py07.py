import random

afile = open("Random.txt", "w" )
num = int(input('How many random numbers?: '))
for i in range(num):
    line = random.randint(1, 1000)
    afile.write((str(line))+ '\n')
    print(line)

afile.close()
