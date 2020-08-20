limit=int(input("Range: "))
def summ(limit):
	sum = 0
	for i in list(range(limit+1)):
		sum += i
	return sum
print(summ(limit))
