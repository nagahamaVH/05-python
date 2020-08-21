x = 1
def f():
	y = x
	x = 2
	return x + y
print(x)   #1
print(f()) #erro porque dentro da função, nao existe um valor pra x quando y=x, se trocar de ordem funciona
print(x)   #1
