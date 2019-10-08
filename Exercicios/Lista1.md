# Getting Started
​
## Running Python Interpreter
​
​
**problem 1:** Open a new Python interpreter and use it to find the value of ``2 + 3``.
​
## Running Python Scripts
​
**problem 2:** Create a python script to print  ``hello, world!`` four times.
​
**problem 3:** Create a python script with the following text and see the output.
​
```
​
    1 + 2
```
If it doesn't print anything, what changes can you make to the program to print the value?
​
## Assignments
​
**problem 4:** What will be output of the following program.
​
```
​
    x = 4
    y = x + 1
    x = 2
    print x, y
```
**problem 5:** What will be the output of the following program.
​
```
​
    x, y = 2, 6
    x, y = y, x + 2
    print x, y
```
**problem 6:** What will be the output of the following program.
​
```
​
    a, b = 2, 3
    c, b = a, c + 1
    print a, b, c
​
```
## Functions
​
**problem 7:** How many multiplications are performed when each of the following
   lines of code is executed?
​
```
numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print square(5)
print square(2*5)
```

**problem 8:** What will be the output of the following program?
​
```
​
	x = 1
	def f():
            return x
	print x
	print f()
```
**problem 9:** What will be the output of the following program?
​
```
​
	x = 1
	def f():
            x = 2
            return x
	print x
	print f()
	print x
```
**problem 10:** What will be the output of the following program?
​
```
​
	x = 1
	def f():
		y = x
		x = 2
		return x + y
	print x
	print f()
	print x
```
**problem 11:** What will be the output of the following program?
​
```
​
    x = 2
    def f(a):
        x = a * a
        return x
    y = f(3)
    print x, y
```
**problem 12:** Write a function ``count_digits`` to find number of digits in the given number.
```
    >>> count_digits(5)
    1
    >>> count_digits(12345)
    5
```
**problem 13:** Write a function `istrcmp` to compare two strings, ignoring the case.
​
```
​
    >>> istrcmp('python', 'Python')
    True
    >>> istrcmp('LaTeX', 'Latex')
    True
    >>> istrcmp('a', 'b')
    False
```
## Conditional Expressions
​
​
**problem 14:** What will be output of the following program?
​
```
​
    print 2 < 3 and 3 > 1
    print 2 < 3 or 3 > 1
    print 2 < 3 or not 3 > 1
    print 2 < 3 and not 3 > 1
```
**problem 15:** What will be output of the following program?
​
```
​
    x = 4
    y = 5
    p = x < y or x < z
    print p
```
**problem 16:** What will be output of the following program?
​
```
​
    True, False = False, True
    print True, False
    print 2 < 3
​
```
**problem 17:** What happens when the following code is executed? Will it give any
   error? Explain the reasons.
​
```
​
    x = 2
    if x == 2:
        print x
    else:
        print y
```
**problem 18:** What happens the following code is executed? Will it give any error? Explain the reasons.
​
```
​
    x = 2
    if x == 2:
        print x
    else:
        x +
```
