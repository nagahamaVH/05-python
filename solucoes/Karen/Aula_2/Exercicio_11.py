#!/usr/bin/python3

for j in range(5):
	if ( j != 4 ) and (j != 1) and (j != 0):
		print (j)
def funcao(limit):
	i = 6
	for i in range(limit):    
		resto = i % 1
		resto1 = i % 2
		resto2 = i % 3
		resto3 = i % 5
		if ((i != 1) and (resto1 != 0) and (resto2 != 0) and (resto3 != 0) and (resto == 0)):  		
			print (i)

f = funcao(100)   

