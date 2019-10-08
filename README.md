# python

Referências dos slides e exercícios:

* https://github.com/learnbyexample/Python_Basics
* https://python.swaroopch.com/
* https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
* https://docs.python-guide.org/
* https://anandology.com/python-practice-book/index.html?utm_source=devfreebooks&utm_medium=medium&utm_campaign=DevFreeBooks
* https://automatetheboringstuff.com/?utm_source=devfreebooks&utm_medium=medium&utm_campaign=DevFreeBooks
* https://penseallen.github.io/PensePython2e/
* https://www.practicepython.org/

# Exemplos

```
chmod +x hello_world.py

$ ./hello_world.py
Hello World
```

# Números

## Inteiros
```
num1 = 7
num2 = 42
total = num1 + num2
```

## float
```
appx_pi = 22 / 7
area = 42.16
appx_pi + area
```

## Notação Científica
```
sci_num1 = 3.982e5
```

## String
```
str1 = 'hello'
str3 = "world"
print(str1 + str3)
```

## Exemplos de operações

* arithmetic operators
    * `+` addition
    * `-` subtraction
    * `*` multiplication
    * `/` division (float output)
    * `//` division (integer output, result is not rounded)
    * `**` exponentiation
    * `%` modulo
* string operators
    * `+` string concatenation
    * `*` string repetition
* comparison operators
    * `==` equal to
    * `>` greater than
    * `<` less than
    * `!=` not equal to
    * `>=` greater than or equal to
    * `<=` less than or equal to
* boolean logic
    * `and` logical and
    * `or` logical or
    * `not` logical not
* bitwise operators
    * `&` and
    * `|` or
    * `^` exclusive or
    * `~` invert bits
    * `>>` right shift
    * `<<` left shift

## def

```
#!/usr/bin/python3

# ----- function without arguments -----
def greeting():
    print("-----------------------------")
    print("         Hello World         ")
    print("-----------------------------")

greeting()
```

## Argumentos

```
# ----- function with arguments -----
def sum_two_numbers(num1, num2):
    total = num1 + num2
    print("{} + {} = {}".format(num1, num2, total))

sum_two_numbers(3, 4)

# ----- function with return value -----
def num_square(num):
    return num * num

my_num = 3
print(num_square(2))
print(num_square(my_num))
```

## Argumento Padrão

```python
#!/usr/bin/python3

# ----- function with default valued argument -----
def greeting(style_char='-'):
    print(style_char * 29)
    print("         Hello World         ")
    print(style_char * 29)

print("Default style")
greeting()

print("\nStyle character *")
greeting('*')

print("\nStyle character =")
greeting(style_char='=')

>>> items = 15
>>> print("No. of items:", items)

```

```python
>>> import sys
>>> print("Error!! Not a valid input", file=sys.stderr)
Error!! Not a valid input
```

## Range

```python
>>> range(5)
range(0, 5)

>>> list(range(5))
[0, 1, 2, 3, 4]

>>> list(range(-2, 2))
[-2, -1, 0, 1]

>>> list(range(1, 15, 2))
[1, 3, 5, 7, 9, 11, 13]

>>> list(range(10, -5, -2))
[10, 8, 6, 4, 2, 0, -2, -4]
```

## type 

```python
>>> type(5)
<class 'int'>

>>> type('Hi there!')
<class 'str'>

>>> type(range(7))
<class 'range'>

>>> type(None)
<class 'NoneType'>

>>> type(True)
<class 'bool'>

>>> arr = list(range(4))
>>> arr
[0, 1, 2, 3]
>>> type(arr)
<class 'list'>
```

## Escopo

```
#!/usr/bin/python3

def print_num():
    print("Yeehaw! num is visible in this scope, its value is: " + str(num))

num = 25
print_num()
```

```
$ ./variable_scope_1.py 
Yeehaw! num is visible in this scope, its value is: 25
```


```python
#!/usr/bin/python3

def square_of_num(num):
    sqr_num = num * num

square_of_num(5)
print("5 * 5 = {}".format(sqr_num))
```

```
$ ./variable_scope_2.py 
Traceback (most recent call last):
  File "./variable_scope_2.py", line 7, in <module>
    print("5 * 5 = {}".format(sqr_num))
NameError: name 'sqr_num' is not defined
```

definindo variável  `global` 

```python
#!/usr/bin/python3

def square_of_num(num):
    global sqr_num
    sqr_num = num * num

square_of_num(5)
print("5 * 5 = {}".format(sqr_num))
```

```
$ ./variable_scope_3.py
5 * 5 = 25
```


```python
#!/usr/bin/python3

sqr_num = 4

def square_of_num(num):
    sqr_num = num * num
    print("5 * 5 = {}".format(sqr_num))

square_of_num(5)
print("Whoops! sqr_num is still {}!".format(sqr_num))
```


```
$ ./variable_scope_4.py 
5 * 5 = 25
Whoops! sqr_num is still 4!
```
