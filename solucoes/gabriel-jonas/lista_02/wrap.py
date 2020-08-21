import sys
infile = open(sys.argv[1], 'r')
#infile = open('input_file.txt','r')

for line in infile:
    if len(line) > 30:
        line = line[0:30] + "\n" + line[30:len(line)]
        print (line)

