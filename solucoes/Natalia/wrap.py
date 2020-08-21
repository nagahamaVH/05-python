import sys
infile = open(sys.argv[1],'r')

for line in infile:
	if len(line)>30:
		line = line[:30] + "\n" + line[30:]
		print (line)
