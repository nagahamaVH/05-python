import sys
infile = open(sys.argv[1],'r')
reversed = []
for line in infile:
    reversed.append(line)
reversed.reverse()
for line in reversed:
    print (line)
