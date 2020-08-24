from collections import Counter

def repetidas(inFile):
	with open(inFile, 'r') as f:
		wordcount = Counter(f.read().split())
		for word, count in wordcount.items():
			if count >= 2:
        			print("{} {}".format(word, count))
			else:
				print (word, "1")
repetidas('cidades.txt')

def total(inFile):
	file = open("cidades.txt", 'r')
	data = file.read()
	words = data.split()
	print ("Total de cidades: ", len(words))
total('cidades.txt')

def unica(inFile):
	my_set = set(open('cidades.txt', 'r'))
	print ("Total de cidades únicas: ", len(my_set))
unica('cidades.txt')

def caracteres(inFile):
        file = open("cidades.txt", 'r')
        data = file.read()
        print ("Total de caracteres: ", len(data))
caracteres('cidades.txt')
