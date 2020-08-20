n1 = int(input("Digite um valor para x: "))
n2 = int(input("Digite um valor para y: "))
n3 = int(input("Digite um valor para a: "))
dict = {}
dict ['x'] = n1
dict ['y'] = n2
dict ['a'] = n3

def invertdict(dict):
	inverted = {y:x for x,y in dict.items()}
	return inverted

print (f"You dictionary: {dict}")
print (f"Inverted dictionary: {invertdict(dict)}")
