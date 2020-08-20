import sys
#infile = open(sys.argv[1], 'r')
infile = open('input_file.txt','r')

reversed_lines = []

for line in infile:
    reversed_lines.append(line)
reversed_lines.reverse()
for line in reversed_lines:
    print (line)
