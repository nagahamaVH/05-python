import sys
infile = open(sys.argv[1], 'r')
#lines = 0
#words = 0
#characters = 0
characters = {}
for line in infile:
    line = line.lower()
    for i in list(line):
        if (i in characters.keys()):
            characters[i] += 1
        else:
            characters[i] = 1

print (characters)