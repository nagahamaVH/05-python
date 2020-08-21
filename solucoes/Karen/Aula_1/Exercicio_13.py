#!/usr/bin/python3

def istrcmp(x,y):
	#a = str(x)
	#b = str(y)
	x = x.lower()
	y = y.lower()
	if (x == y):
		print ("True")
	else:
		print ("False")
	return x,y	

a,b = istrcmp('KaReN','karen')



