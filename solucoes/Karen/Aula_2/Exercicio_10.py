#!/usr/bin/python3

print ("\n")

def funcao(limit):
	i=1
	cont = 0
	for i in range(limit):   
		resto3 = i % 3
		resto5 = i % 5
		if ((resto3 == 0) and (i != 0)):        
			print (i, end=' ')
		elif ((resto5 == 0) and (i != 0)):
			print (i, end=' ')
f = funcao(20)   
print ("\n")




