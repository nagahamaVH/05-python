#!/usr/bin/python3

print ("[", end="")

def valuesort (x):
	dicionario = ""
	dicionario = sorted(x.keys())
	for item in dicionario:
		print (x[item], end =" ")


#print (sortedDict.keys())
y = valuesort({'x': 1, 'y': 2, 'a': 3})
print ("]", end = "")
print ("\n")
