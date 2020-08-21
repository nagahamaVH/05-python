n1 = int(input("Digite um valor para a: "))
n2 = int(input("Digite um valor para b: "))
n3 = int(input("Digite um valor para c: "))
dict = {}
dict ['a'] = n1
dict ['b'] = n2
dict ['c'] = n3
def valuesort(dict):
	sorted_dict = sorted(dict.values())
	print (sorted_dict)

valuesort(dict)
