#!/usr/bin/python3

a = (list(open("/home/karentaniguchi/05-python/solucoes/Karen/Aula2/she.txt")))
comprimento = int(input("Digite o comprimento para a quebra de linhas: "))

#print(len(a))
for line in a:
	b = len(line)
	if ( b > comprimento):
                #print (len(line))
		print (line[:comprimento])
		print (line[comprimento:].rstrip()) 
	else:
		print ("")


