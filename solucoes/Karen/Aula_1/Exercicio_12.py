#!/usr/bin/python3

def count_digits(num):
	#num = input("Digite o número que será retornado sua quantidade de dígitos: \n")
	string=str(num)
	quant = len(string)
	print ("Quantidade de dígitos é", quant)
	return num
num2 = count_digits(12123123132123)
