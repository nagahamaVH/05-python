#!/usr/bin/python3

a = (list(open("/home/karentaniguchi/05-python/solucoes/Karen/Aula2/she.txt")))
from collections import Counter
cont = 0 
for line in a:
	contador = Counter(line)
	cont = cont + 1
	print ("\nLinha", cont, "\n\n", contador)
