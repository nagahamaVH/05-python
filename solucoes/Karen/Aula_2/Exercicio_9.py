#!/usr/bin/python3


def showNumbers(limit):
	for i in range(limit):   
		resto = i % 2
		#print (resto)
		if (resto == 0):        
			print ("*   ",	i, "PAR")
		else:
			print ("*   ",  i, "IMPAR")

f = showNumbers(10)    



