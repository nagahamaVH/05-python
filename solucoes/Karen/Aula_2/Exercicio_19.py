#!/usr/bin/python3

def Anagrama (lista):
	for line in lista:
		cont = 0
		b = list(line)
		b.sort()
		if (len(b) == len(line)):
			for i in range(len(b)):
				if ((b[i]) == (line[i])):
					print (line)
y = Anagrama (['eat', 'ate', 'done', 'tea', 'soup', 'node'])


