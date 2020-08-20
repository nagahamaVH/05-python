def count_digits(num):
	num = abs(num)
	count=1
	while (int(num/10)) > 0:
		count += 1
		num=int(num/10)
	return count
print (count_digits(78985))
