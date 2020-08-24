import sys
import random

num = int(sys.argv[1])
f = open (sys.argv[2], 'w')

for i in range(num):
    f.write("{} \n".format(random.random()))

f.close()